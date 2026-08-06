import os
import re
from datetime import date
from typing import Optional
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter

# Internal imports
from .loaders import load_raw_documents
from .metadata_extractor import generate_okf_metadata
from app.retrieval.hybrid_search import get_qdrant_vector_store
from app.retrieval.query_engine import configure_llm_settings
from app.core.config import settings
from app.okf.formatter import format_and_save_okf


def configure_chunking():
    """
    Configures the global chunking strategy for LlamaIndex.
    Satisfies Requirement #2: Chunking Strategy.
    """
    # SentenceSplitter respects sentence boundaries, preventing cut-off words.
    Settings.transformations = [
        SentenceSplitter(chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP)
    ]


def _build_okf_frontmatter(raw_meta: dict, index: int) -> Optional[dict]:
    """
    Bridges the gap between LLM-extracted metadata (title, summary, document_type,
    topics, trust_level) and the OKFConcept schema (id, category, tags, description).

    The OKFConcept schema requires `id` and `category` as non-optional fields, but
    generate_okf_metadata() returns different keys. This function maps them correctly
    so that saved .md files pass schema validation by the repository and search layers.

    Returns None when the metadata is unusable (empty title, placeholder title, or
    placeholder category) so the pipeline can skip the document instead of writing a
    junk "Unknown Document" concept to the knowledge base.
    """
    title = (raw_meta or {}).get("title") or ""
    title = title.strip()
    placeholder_titles = {"unknown document", "unknown", "unclassified", "metadata extraction failed"}
    if not title or title.lower() in placeholder_titles:
        return None

    # Generate a slug ID from category + title (matches the converter's format).
    title_slug = re.sub(r"[^a-zA-Z0-9]+", "-", title).strip("-").lower()
    if not title_slug or not title_slug[0].isalnum():
        return None

    # Map document_type → category (normalize to lowercase slug)
    raw_category = (raw_meta or {}).get("document_type") or ""
    category = re.sub(r"[^a-zA-Z0-9]+", "-", raw_category).strip("-").lower()
    if category in ("", "unknown", "unclassified", "general", "misc"):
        category = "reference"
    id = f"{category}-{title_slug}" if not title_slug.startswith(f"{category}-") else title_slug

    # Map topics → tags (ensure it's a list of strings)
    raw_topics = raw_meta.get("topics") or []
    if isinstance(raw_topics, str):
        raw_topics = [t.strip() for t in raw_topics.split(",") if t.strip()]
    tags = [str(t) for t in raw_topics if t]
    tags = [t for t in tags if t.lower() not in ("unknown", "unclassified")]

    today = date.today().isoformat()

    return {
        # OKFConcept required fields
        "id": id,
        "type": "concept",
        "title": title,
        "description": (raw_meta.get("summary") or title)[:300],
        "category": category,
        "tags": tags,
        "source": None,
        "created_at": today,
        "updated_at": today,
        "aliases": [],
        "related": [],
        # Extra fields kept for Qdrant metadata (useful for /query citations)
        "document_type": raw_category,
        "trust_level": raw_meta.get("trust_level") or "Medium",
    }


def run_ingestion_pipeline(raw_dir: str = None, okf_dir: str = None):
    """
    The master orchestration function.
    1. Loads raw documents.
    2. Extracts OKF Metadata via LLM.
    3. Converts to OKF-compliant frontmatter.
    4. Saves physical OKF Markdown files.
    5. Chunks and indexes into Qdrant.
    """
    if raw_dir is None:
        raw_dir = settings.RAW_DATA_DIR
    if okf_dir is None:
        okf_dir = settings.OKF_DATA_DIR

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

    # 2, 3 & 4. Extract Metadata (in parallel), Bridge to OKF Schema, Save Files.
    # Metadata extraction is the slowest step (LLM calls); running it across a
    # small thread pool keeps ingestion fast instead of timing out in the UI.
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _extract(item):
        i, doc = item
        return i, doc, generate_okf_metadata(doc.text)

    with ThreadPoolExecutor(max_workers=min(3, len(raw_docs))) as pool:
        futures = [pool.submit(_extract, item) for item in enumerate(raw_docs)]
        for future in as_completed(futures):
            try:
                i, doc, raw_meta = future.result()
            except Exception as exc:  # noqa: BLE001 - a single failure must not abort the run
                print(f"⚠️ Metadata extraction failed for a document: {exc}")
                continue

            print(f"⚙️ Processing Document {i+1}/{len(raw_docs)}...")

            # Convert to OKF-schema-compliant frontmatter (adds id, category, tags, description…)
            okf_meta = _build_okf_frontmatter(raw_meta, i)

            # Skip documents with no usable content/metadata instead of writing junk concepts.
            if okf_meta is None:
                print(f"⚠️ Skipping Document {i+1}: no usable content or metadata was extracted.")
                continue

            # Attach the OKF-compliant metadata to the LlamaIndex Document.
            # This guarantees that when the document is chunked, EVERY chunk carries this
            # metadata in Qdrant — including 'title' which is used for query citations.
            doc.metadata.update(okf_meta)

            # Use the slug id as the filename for consistency
            filename = f"{okf_meta['id']}_{i}.md"

            # Physically save the OKF-formatted Markdown file to disk
            format_and_save_okf(text=doc.text, metadata=okf_meta, output_dir=okf_dir, filename=filename)

            processed_docs.append(doc)

    print(f"💾 Saved {len(processed_docs)} OKF documents to {okf_dir}")

    # 5. Chunk and Index into Qdrant Vector DB
    print("📦 Connecting to Qdrant for vector indexing...")
    # Index into the SAME concepts collection that build_index and the semantic
    # search layer read from, so ingested documents are actually retrievable.
    vector_store = get_qdrant_vector_store(settings.QDRANT_CONCEPTS_COLLECTION)

    # Storage context tells LlamaIndex to use Qdrant instead of in-memory storage
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("🔪 Chunking documents and generating embeddings… (This may take a moment)")
    # This single call handles: chunking (Settings.transformations),
    # embedding (Settings.embed_model), and uploading to Qdrant.
    index = VectorStoreIndex.from_documents(
        processed_docs,
        storage_context=storage_context
    )

    print("✅ Ingestion Pipeline Complete!")
    return {"status": "success", "indexed_documents": len(processed_docs)}