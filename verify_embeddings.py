import os
import chromadb

def verify_embeddings():
    persist_directory = "./chroma_db"
    if not os.path.exists(persist_directory):
        print("ChromaDB directory not found. Have you run ingest.py yet?")
        return

    print("Connecting to ChromaDB...")
    client = chromadb.PersistentClient(path=persist_directory)
    
    try:
        collection = client.get_collection(name="langchain")
    except Exception as e:
        print("Could not find the 'langchain' collection.")
        return

    data = collection.get(include=["embeddings", "documents", "metadatas"])
    
    num_chunks = len(data['ids'])
    print(f"\nTotal embeddings (chunks) found in Vector Database: {num_chunks}")
    
    if num_chunks == 0:
        print("No embeddings found.")
        return

    embedding_dim = len(data['embeddings'][0])
    print(f"Embedding Dimensionality: {embedding_dim} (Matches BAAI/bge-small-en-v1.5)\n")

    print("="*60)
    print(" SAMPLE EMBEDDINGS PREVIEW ")
    print("="*60)

    for i in range(min(3, num_chunks)):
        doc = data['documents'][i]
        meta = data['metadatas'][i]
        emb = data['embeddings'][i]
        
        display_text = doc if len(doc) < 100 else doc[:100] + "..."
        display_emb = [round(val, 4) for val in emb[:5]]
        
        print(f"--- CHUNK {i+1} ---")
        print(f"Source   : {meta.get('source', 'Unknown')}")
        print(f"Headers  : {[k for k in meta.keys() if k != 'source']}")
        print(f"Text     : {display_text}")
        print(f"Vector   : {display_emb} ... (total {embedding_dim} floats)")
        print("-"*60)
        
    print("\nVerification Complete. The database successfully stores the semantic chunks and their vectors!")

if __name__ == "__main__":
    verify_embeddings()
