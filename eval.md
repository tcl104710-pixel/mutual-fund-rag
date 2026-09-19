# Evaluation Strategy (Phase-wise)

This document outlines the evaluation criteria and testing strategies for each phase of the Mutual Fund FAQ Assistant implementation plan.

## Phase 1: Project Setup & Configuration
**Goal:** Ensure the environment is correctly initialized and all dependencies are functioning.
*   **Eval 1.1 (Environment):** Verify that the Python virtual environment (`venv`) is active.
*   **Eval 1.2 (Dependencies):** Run a test script to import `langchain_groq`, `langchain_huggingface`, `chromadb`, and `streamlit` to ensure no `ModuleNotFoundError` is thrown.
*   **Eval 1.3 (Environment Variables):** Verify that the `.env` file exists and `GROQ_API_KEY` is loaded correctly into the environment `os.environ`.

## Phase 2: Data Processing Pipeline (Offline)
**Goal:** Ensure data is correctly scraped, chunked, and embedded into the vector database.
*   **Eval 2.1 (Scraping Success Rate):** Assert that the scraper returns non-empty strings for all 5 target Groww URLs. Check for error keywords like "403 Forbidden" or "Access Denied" in the scraped text.
*   **Eval 2.2 (Chunk Integrity):** Sample 5 random chunks from the parser. Assert that their length is within the expected bounds (<= 1000 characters) and that each chunk's `metadata` dictionary contains a valid `source` URL.
*   **Eval 2.3 (Vector DB Persistence):** After running `ingest.py`, verify that the `./chroma_db` directory is created. Initialize a Chroma client and assert that `collection.count() > 0`.

## Phase 3: RAG Pipeline Core (Online)
**Goal:** Ensure the core logic accurately retrieves context and synthesizes factual answers using Groq and BGE embeddings.
*   **Eval 3.1 (Input Guardrails):**
    *   *Test Set:* 10 advisory queries (e.g., "Which fund is best?", "Should I buy HDFC Mid Cap?").
    *   *Metric:* 100% rejection rate by the `check_input_guardrails` function.
*   **Eval 3.2 (Context Retrieval Accuracy / Recall@3):**
    *   *Test Set:* 10 purely factual questions (e.g., "What is the exit load for HDFC Large Cap?").
    *   *Metric:* In at least 90% of cases, the correct answer must be present within the text of the top 3 retrieved chunks.
*   **Eval 3.3 (LLM Synthesis & Hallucination Check):**
    *   *Test Set:* Pass the retrieved context and question to the Llama-3 model via Groq.
    *   *Metric:* Human evaluation (or LLM-as-a-judge) to ensure the generated answer does not contain facts absent from the retrieved context.
*   **Eval 3.4 (Out-of-Domain Rejection):**
    *   *Test Set:* "Who is the Prime Minister of India?"
    *   *Metric:* The LLM must gracefully respond that it does not have the information in its provided sources.

## Phase 4: Output Guardrails & Formatting
**Goal:** Ensure the final output strictly adheres to the formatting constraints defined in the problem statement.
*   **Eval 4.1 (Length Constraint):** 
    *   *Test:* Force the LLM to generate a 5-sentence response.
    *   *Metric:* The output guardrail truncates the final string to exactly 3 sentences.
*   **Eval 4.2 (Citation Formatting):** 
    *   *Test:* Inspect the final output string.
    *   *Metric:* Regex match to ensure `\n\n**Source:** https://groww.in/...` is present exactly once.
*   **Eval 4.3 (Footer Formatting):** 
    *   *Test:* Inspect the final output string.
    *   *Metric:* String match to ensure `\n\n*Last updated from sources: <Current Date>*` is appended at the very end.

## Phase 5: User Interface (UI)
**Goal:** Ensure the Streamlit application is user-friendly and displays the required components.
*   **Eval 5.1 (App Launch):** The command `streamlit run app.py` executes successfully without runtime errors and binds to `localhost:8501`.
*   **Eval 5.2 (Disclaimer Visibility):** Manual visual check to ensure "Facts-only. No investment advice." is clearly visible on the main page.
*   **Eval 5.3 (Interactive Elements):** Manual check to ensure clicking the 3 example question buttons correctly populates the chat input and triggers the RAG pipeline.
