import os
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter

# Internal imports
from .loaders import load_raw_documents
from .metadata_extractor import generate_okf_metadata
from app.retrieval.hybrid_search import get_qdrant_vector_store
from app.retrieval.query_engine import configure_llm_settings

# We will build this in the next step (app/okf/ folder)
from app.okf.formatter import format_and_save_okf

def configure_chunking():
    """
    Configures the global chunking strategy for LlamaIndex.
    Satisfies Requirement #2: Chunking Strategy.
    """
    # SentenceSplitter respects sentence boundaries, preventing cut-off words.
    # 512 tokens is a great sweet spot for semantic search context windows.
    Settings.transformations = [
        SentenceSplitter(chunk_size=512, chunk_overlap=50)
    ]

def run_ingestion_pipeline(raw_dir: str = "data/raw", okf_dir: str = "knowledge/source_1"):
    """
    The master orchestration function.
    1. Loads raw documents.
    2. Extracts OKF Metadata.
    3. Saves physical OKF Markdown files.
    4. Chunks and Indexes into Qdrant.
    """
    print("🚀 Starting OKF Ingestion Pipeline...")
    
    # Ensure LLM and Embeddings are configured
    configure_llm_settings()
    configure_chunking()
    
    # 1. Load Raw Documents
    raw_docs = load_raw_documents(raw_dir)
    if not raw_docs:
        print("⚠️ No documents to ingest. Pipeline aborted.")
        return {"status": "skipped", "message": "No raw documents found."}

    processed_docs = []
    
    # 2 & 3. Extract Metadata & Save Physical OKF Files
    for i, doc in enumerate(raw_docs):
        print(f"⚙️ Processing Document {i+1}/{len(raw_docs)}...")
        
        # Call LLM to get YAML frontmatter data
        meta = generate_okf_metadata(doc.text)
        
        # Attach the metadata to the LlamaIndex Document object.
        # This guarantees that when the document is chunked, EVERY chunk gets this metadata payload in Qdrant!
        doc.metadata.update(meta)
        
        # Define a safe filename
        safe_title = meta['title'].replace(" ", "_").replace("/", "-").lower()
        filename = f"{safe_title}_{i}.md"
        
        # Delegate to the OKF Formatter to physically save the file to disk
        # (We will write this logic in the app/okf folder next)
        format_and_save_okf(text=doc.text, metadata=meta, output_dir=okf_dir, filename=filename)
        
        processed_docs.append(doc)

    print(f"💾 Saved {len(processed_docs)} OKF documents to {okf_dir}")

    # 4. Chunk and Index into Qdrant Vector DB
    print("📦 Connecting to Qdrant for vector indexing...")
    vector_store = get_qdrant_vector_store()
    
    # Storage context tells LlamaIndex to use Qdrant instead of in-memory storage
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    print("🔪 Chunking documents and generating embeddings... (This may take a moment)")
    # This single line handles chunking (via Settings.transformations), 
    # embedding (via Settings.embed_model), and uploading to Qdrant!
    index = VectorStoreIndex.from_documents(
        processed_docs, 
        storage_context=storage_context
    )
    
    print("✅ Ingestion Pipeline Complete!")
    return {"status": "success", "indexed_documents": len(processed_docs)}