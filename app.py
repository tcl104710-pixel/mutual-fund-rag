import os
from datetime import datetime
from flask import Flask, request, jsonify, send_file
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

app = Flask(__name__, static_folder='stitch_mutual_fund_faq_chatbot', static_url_path='/assets')

# Setup Vector Store
persist_directory = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

if os.path.exists(persist_directory):
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5, "fetch_k": 20})
else:
    vectorstore = None
    retriever = None

# Initialize LLM
if os.environ.get("GROQ_API_KEY") and os.environ.get("GROQ_API_KEY") != "your_groq_api_key_here":
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
else:
    llm = None

# Prompt Template enforcing constraints
RAG_PROMPT_TEMPLATE = """You are a strictly factual mutual fund FAQ assistant.
Use ONLY the following pieces of retrieved context to answer the question.
If you don't know the answer or the context does not contain the answer, politely state that you do not have that information in your provided sources.
DO NOT provide any investment advice, recommendations, opinions, or performance comparisons.
Keep your answer to a MAXIMUM of 3 sentences.

Context:
{context}

Question: {question}

Factual Answer:"""

PROMPT = PromptTemplate(template=RAG_PROMPT_TEMPLATE, input_variables=["context", "question"])

def check_input_guardrails(query):
    """Simple heuristic filter to reject advisory or comparative queries."""
    advisory_keywords = ["should i", "which is better", "recommend", "advice", "invest in", "good investment", "better fund"]
    query_lower = query.lower()
    for kw in advisory_keywords:
        if kw in query_lower:
            return False
    return True

def generate_response(query):
    if not retriever or not llm:
        return "System is not properly configured. Please check your API keys and ensure data ingestion is complete."
    
    if not check_input_guardrails(query):
        return "I can only provide factual information based on official documents. I cannot provide investment advice, recommendations, or fund comparisons. For guidance, please refer to AMFI or SEBI resources."

    docs = retriever.invoke(query)
    
    if not docs:
        return "I do not have this information in my provided sources."

    context_text = "\n\n".join([doc.page_content for doc in docs])
    
    prompt_value = PROMPT.format(context=context_text, question=query)
    
    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
    def invoke_llm(prompt):
        return llm.invoke(prompt)

    try:
        response = invoke_llm(prompt_value)
        answer_text = response.content.strip()
    except Exception as e:
        return f"I'm sorry, but I'm currently receiving too many requests (API Rate Limit). Please try again in a few seconds."

    sentences = [s.strip() for s in answer_text.split('.') if s.strip()]
    if len(sentences) > 3:
        answer_text = '. '.join(sentences[:3]) + '.'

    source_url = docs[0].metadata.get("source", "Unknown Source")
    current_date = datetime.now().strftime("%B %d, %Y")
    
    return {
        "answer": answer_text,
        "docName": "Groww MF Directory",
        "docMeta": source_url + " • Updated " + current_date,
        "copyCitation": f"{answer_text} (Source: {source_url})"
    }

@app.route("/")
def index():
    # Serve the stitch generated HTML file
    return send_file(os.path.join("stitch_mutual_fund_faq_chatbot", "code.html"))

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"answer": "Please ask a question.", "docName": "Error", "docMeta": "", "copyCitation": ""})
    
    response_data = generate_response(query)
    # If generate_response returned a string (e.g. guardrail refusal), wrap it
    if isinstance(response_data, str):
        return jsonify({
            "answer": response_data,
            "docName": "System Guardrail",
            "docMeta": "Internal constraint triggered",
            "copyCitation": response_data
        })
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(port=5000)
