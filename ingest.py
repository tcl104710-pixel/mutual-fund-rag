import os
import requests
from document_fetcher import DocumentFetcher
from langchain_text_splitters import HTMLHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# List of the 5 Groww URLs provided in the problem statement
URLS = [
    "https://groww.in/mutual-funds/hdfc-gold-etf-fund-of-fund-direct-plan-growth",
    "https://groww.in/mutual-funds/hdfc-large-cap-fund-direct-growth",
    "https://groww.in/mutual-funds/hdfc-small-cap-fund-direct-growth",
    "https://groww.in/mutual-funds/hdfc-silver-etf-fof-direct-growth",
    "https://groww.in/mutual-funds/hdfc-mid-cap-fund-direct-growth"
]


def chunk_text(html_content, url):
    """Splits HTML into chunks semantically and attaches metadata."""
    headers_to_split_on = [
        ("h1", "Header 1"),
        ("h2", "Header 2"),
        ("h3", "Header 3"),
        ("h4", "Header 4"),
    ]
    html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    html_header_splits = html_splitter.split_text(html_content)
    
    # Secondary split for long sections
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, 
        chunk_overlap=200
    )
    
    splits = text_splitter.split_documents(html_header_splits)
    
    # Inject source URL into metadata
    for split in splits:
        split.metadata["source"] = url
        
    return splits

def process_and_ingest():
    """Main pipeline for scraping, chunking, and ingesting into Pinecone."""
    all_chunks = []
    
    print("Starting data ingestion phase...")
    fetcher = DocumentFetcher(output_dir="data")
    
    for url in URLS:
        print(f"Scraping {url}...")
        # Optional: save locally as an html file for debugging/caching
        filename = url.strip("/").split("/")[-1] + ".html"
        html_content = fetcher.fetch_and_save_html(url, filename)
        if html_content:
            print(f"Chunking {url}...")
            chunks = chunk_text(html_content, url)
            all_chunks.extend(chunks)
            
    print(f"Total chunks created: {len(all_chunks)}")
    
    # Save chunks to a file for manual review
    if all_chunks:
        chunks_file_path = os.path.join("data", "all_chunks_review.txt")
        with open(chunks_file_path, "w", encoding="utf-8") as f:
            for i, chunk in enumerate(all_chunks):
                f.write(f"--- CHUNK {i+1} | Source: {chunk.metadata.get('source')} ---\n")
                f.write(chunk.page_content + "\n\n")
        print(f"Saved {len(all_chunks)} chunks to {chunks_file_path} for manual review.")
    
    if all_chunks:
        print("Initializing Embedding Model...")
        embeddings = CohereEmbeddings(model="embed-english-light-v3.0")
        
        print("Ingesting into Pinecone Vector Store...")
        index_name = os.environ.get("PINECONE_INDEX_NAME", "mutual-fund-rag")
        PineconeVectorStore.from_documents(
            documents=all_chunks, 
            embedding=embeddings, 
            index_name=index_name
        )
        print("Ingestion complete!")
    else:
        print("No chunks to ingest.")

if __name__ == "__main__":
    process_and_ingest()
