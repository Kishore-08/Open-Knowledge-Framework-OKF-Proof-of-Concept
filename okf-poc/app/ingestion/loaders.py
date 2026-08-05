import os
from typing import List
from llama_index.core import SimpleDirectoryReader, Document
from llama_index.readers.file import PyMuPDFReader

def load_raw_documents(data_dir: str = "data/raw") -> List[Document]:
    """
    Reads raw documents from the specified directory.
    Satisfies Requirement #1: Ingest from 3+ sources.
    Supports: .pdf, .md, .txt, .json
    """
    if not os.path.exists(data_dir):
        print(f"⚠️ Directory {data_dir} does not exist. Creating it now.")
        os.makedirs(data_dir)
        return []

    print(f"📂 Scanning {data_dir} for raw documents...")
    
    # We explicitly map the PyMuPDFReader to PDF files for better text extraction
    # compared to the default PDF parser, which is crucial for enterprise architecture docs.
    file_extractor = {
        ".pdf": PyMuPDFReader()
    }

    # SimpleDirectoryReader automatically handles routing the correct parser based on file extension
    # It supports .md, .txt, .json out of the box.
    reader = SimpleDirectoryReader(
        input_dir=data_dir,
        file_extractor=file_extractor,
        required_exts=[".pdf", ".md", ".txt", ".json"],
        recursive=True
    )
    
    documents = reader.load_data()
    print(f"✅ Loaded {len(documents)} document pages/chunks from {data_dir}.")
    
    return documents