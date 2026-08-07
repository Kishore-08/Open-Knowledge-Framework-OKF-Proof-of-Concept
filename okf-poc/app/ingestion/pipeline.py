import os
import re
import asyncio
from datetime import date
from typing import Optional

# Internal imports
from .loaders import load_raw_documents
from .crawler import crawl_configured_sources
from .metadata_extractor import generate_okf_metadata
from app.indexing.indexer import concepts_to_documents
from app.okf.repository import load_all_concepts
from app.retrieval.hybrid_search import index_documents
from app.retrieval.query_engine import configure_llm_settings
from app.core.config import settings
from app.okf.formatter import format_and_save_okf
from app.parser.cleaner import clean_html, extract_title
from app.converter.markdown import (
    html_to_markdown,
    split_into_concepts,
    write_concept_file,
)
from app.okf.repository import (
    load_all_concepts,
    delete_concepts_by_source_urls,
)
from app.retrieval.hybrid_search import (
    index_documents,
    delete_points_by_field,
)

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

    # Preserve provenance: the raw source filename (e.g. "docker-basics.txt")
    # becomes the `source_file` metadata used for citation + idempotent re-ingest.
    source_file = (raw_meta.get("source_file") or raw_meta.get("file_name") or "").strip()
    source_name = (raw_meta.get("source_name") or "Ingested document").strip()
    source_url = (raw_meta.get("source_url") or "").strip()

    return {
        # OKFConcept required fields
        "id": id,
        "type": "concept",
        "title": title,
        "description": (raw_meta.get("summary") or title)[:300],
        "category": category,
        "tags": tags,
        "source": {"name": source_name, "url": source_url} if source_name or source_url else None,
        "created_at": today,
        "updated_at": today,
        "aliases": [],
        "related": [],
        # Extra fields kept for Qdrant metadata (useful for /query citations)
        "document_type": raw_category,
        "trust_level": raw_meta.get("trust_level") or "Medium",
        "source_file": source_file or None,
    }

def _process_crawled_html(
    raw_dir: str,
    okf_dir: str,
    changed_pages: list[dict],
) -> int:
    """
    Convert crawled HTML files under raw_dir into OKF concept files.

    Expected layout:
        data/raw/<source>/*.html
    """
    if not os.path.isdir(raw_dir):
        return 0

    processed = 0

    for source_name in sorted(os.listdir(raw_dir)):
        source_dir = os.path.join(raw_dir, source_name)

        if not os.path.isdir(source_dir):
            continue

        for filename in sorted(os.listdir(source_dir)):
            if not filename.lower().endswith((".html", ".htm")):
                continue

            html_path = os.path.join(source_dir, filename)

            try:
                with open(
                    html_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore",
                ) as f:
                    html = f.read()

                if not html.strip():
                    continue

                cleaned_html = clean_html(html, base_url=page["url"])

                markdown = html_to_markdown(cleaned_html)

                if not markdown.strip():
                    print(
                        f"⚠️ Skipping empty crawled document: {html_path}"
                    )
                    continue

                category = source_name.lower()

                concepts = split_into_concepts(
                    markdown=markdown,
                    category=category,
                    source_name=source_name,
                    source_url="",
                )

                for concept_id, _title, content in concepts:
                    write_concept_file(
                        knowledge_dir=okf_dir,
                        category=category,
                        concept_id=concept_id,
                        content=content,
                    )

                processed += 1

            except Exception as exc:
                print(
                    f"⚠️ Failed to process crawled HTML "
                    f"{html_path}: {exc}"
                )

    return processed

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

    # 0. Crawl configured official documentation sources.
    crawl_result = asyncio.run(crawl_configured_sources())

    deleted_urls = crawl_result["deleted_urls"]

    if deleted_urls:
        delete_concepts_by_source_urls(
            deleted_urls,
            knowledge_dir=settings.KNOWLEDGE_DIR,
        )

        delete_points_by_field(
            settings.QDRANT_CONCEPTS_COLLECTION,
            "source_url",
            deleted_urls,
        )

    print(
    "🌐 Documentation crawl complete: "
    f"sources={crawl_result['sources']} "
    f"discovered={crawl_result['discovered']} "
    f"fetched={crawl_result['fetched']} "
    f"cached={crawl_result['cached']} "
    f"failed={crawl_result['failed']}"
    )

    # 1. Convert crawled HTML into OKF concept files.
    crawled_count = _process_crawled_html(
        raw_dir=raw_dir,
        okf_dir=okf_dir,
)

    print(
        f"📚 Converted {crawled_count} crawled HTML documents "
        f"into OKF concepts."
    )

    # 2. Ensure LLM and Embeddings are configured.
    configure_llm_settings()

    # 3. Load existing local raw documents.
    raw_docs = load_raw_documents(raw_dir)

    if not raw_docs:
        print(
            "ℹ️ No additional local raw documents found. "
            "Continuing with crawled OKF concepts."
        )

    saved_count = 0

    # 2, 3 & 4. Extract Metadata (in parallel), Bridge to OKF Schema, Save Files.
    # Metadata extraction is the slowest step (LLM calls); running it across a
    # small thread pool keeps ingestion fast instead of timing out in the UI.
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _extract(item):
        i, doc = item
        source_name = (doc.metadata or {}).get("file_name") or (
            os.path.basename((doc.metadata or {}).get("file_path", ""))
        )
        raw_meta = generate_okf_metadata(doc.text, source_name=source_name) or {}
        # Carry provenance from the raw document loader into the frontmatter builder.
        raw_meta["source_file"] = source_name
        return i, doc, raw_meta

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

            # Use the slug id as the filename for consistency
            filename = f"{okf_meta['id']}_{i}.md"

            # Physically save the OKF-formatted Markdown file to disk
            format_and_save_okf(text=doc.text, metadata=okf_meta, output_dir=okf_dir, filename=filename)

            saved_count += 1

    print(
    f"💾 Local ingestion saved {saved_count} OKF documents. "
    f"Crawled documentation produced {crawled_count} source documents."
    )

    # 5. Re-read the OKF files just written from disk (the source of truth) and
    #    index them into Qdrant via the shared indexer path. This guarantees the
    #    vector store always mirrors the filesystem knowledge base — the same
    #    documents, metadata, and provenance that search + query layers consume.
    print("📦 Re-reading OKF files and connecting to Qdrant for vector indexing...")
    concepts = load_all_concepts(okf_dir, use_cache=False)
    docs = concepts_to_documents(concepts)
    if not docs:
        print("⚠️ No valid OKF concepts were produced; nothing to index.")
        return {"status": "skipped", "message": "No valid OKF concepts were produced."}

    source_files = [d.metadata["source_file"] for d in docs if d.metadata.get("source_file")]
    index_documents(
        docs,
        collection_name=settings.QDRANT_CONCEPTS_COLLECTION,
        source_files=source_files,
    )

    print("✅ Ingestion Pipeline Complete!")
    return {"status": "success", "indexed_documents": len(docs)}