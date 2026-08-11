import os
from typing import List
from llama_index.core import SimpleDirectoryReader, Document
from llama_index.readers.file import PyMuPDFReader

def load_raw_documents(cache_dir: str = "cache") -> List[Document]:
    """
    Reads raw documents from the specified cache directory.
    Satisfies Requirement #1: Ingest from 3+ sources.
    Supports: .pdf, .md, .txt, .json
    
    Args:
        cache_dir: Path to cache directory containing raw documents (default: "cache")
    """
    if not os.path.exists(cache_dir):
        print(f"⚠️ Directory {cache_dir} does not exist. Creating it now.")
        os.makedirs(cache_dir)
        return []

    print(f"📂 Scanning {cache_dir} for raw documents...")
    
    # We explicitly map the PyMuPDFReader to PDF files for better text extraction
    # compared to the default PDF parser, which is crucial for enterprise architecture docs.
    file_extractor = {
        ".pdf": PyMuPDFReader()
    }

    # SimpleDirectoryReader automatically handles routing the correct parser based on file extension
    # It supports .md, .txt, .json out of the box.
    reader = SimpleDirectoryReader(
        input_dir=cache_dir,
        file_extractor=file_extractor,
        required_exts=[".pdf", ".md", ".txt", ".json"],
        recursive=True
    )
    
    documents = reader.load_data()
    print(f"✅ Loaded {len(documents)} document pages/chunks from {cache_dir}.")
    
    return documents