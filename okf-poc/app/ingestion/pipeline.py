import os
import re
import asyncio
import hashlib
import json
from pathlib import Path
from datetime import date
from typing import Optional

# Internal imports
from .loaders import load_raw_documents
from .crawler import crawl_configured_sources
from .metadata_extractor import generate_okf_metadata
from app.ingestion.status import update_status
from app.indexing.indexer import concepts_to_documents
from app.retrieval.query_engine import configure_llm_settings
from app.core.config import settings
from app.okf.formatter import format_and_save_okf
from app.parser.cleaner import clean_html
from llama_index.core import SimpleDirectoryReader
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
from app.storage.state_manager import StateManager

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
    raw_title = (raw_meta or {}).get("title") or ""
    title = str(raw_title).strip() if raw_title is not None else ""
    placeholder_titles = {
        "unknown document",
        "unknown",
        "unclassified",
        "metadata extraction failed",
        "none",
        "null",
        "n/a",
        "na",
        "",
    }
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

def _processing_state_path(cache_dir: str) -> str:
    state_dir = os.path.join(cache_dir, ".state")
    os.makedirs(state_dir, exist_ok=True)
    return os.path.join(state_dir, "processing.json")


def _load_processing_state(cache_dir: str) -> dict:
    path = _processing_state_path(cache_dir)

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _save_processing_state(cache_dir: str, state: dict) -> None:
    path = _processing_state_path(cache_dir)
    temp_path = f"{path}.tmp"

    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)

    os.replace(temp_path, path)

def _discover_local_raw_files(cache_dir: str) -> list[str]:
    """Find manually supplied raw documents in cache, excluding crawler HTML."""
    supported = {".pdf", ".md", ".txt", ".json"}
    files = []

    if not os.path.isdir(cache_dir):
        return files

    for root, _, filenames in os.walk(cache_dir):
        # Never treat crawler state as an input document.
        if ".state" in Path(root).parts:
            continue

        for filename in filenames:
            path = os.path.join(root, filename)

            if Path(filename).suffix.lower() in supported:
                files.append(path)

    return sorted(files)


def _get_changed_local_files(cache_dir: str, state: dict) -> tuple[list[str], dict]:
    """
    Return only local cached files whose content changed since the previous run.
    """
    previous_files = state.setdefault("files", {})
    changed_files = []

    current_files = set()

    for path in _discover_local_raw_files(cache_dir):
        relative_path = os.path.relpath(path, cache_dir)
        current_files.add(relative_path)

        content_hash = _file_hash(path)
        previous = previous_files.get(relative_path, {})

        if previous.get("content_hash") != content_hash:
            changed_files.append(path)

    # Remove state entries for files that no longer exist.
    for relative_path in list(previous_files):
        if relative_path not in current_files:
            del previous_files[relative_path]

    return changed_files, state

def _file_hash(path: str) -> str:
    digest = hashlib.sha256()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()

def _discover_cached_crawl_pages(cache_dir: str) -> list[dict]:
    """
    Recover crawl pages from the on-disk crawler state so that a rerun can rebuild
    the knowledge output from already downloaded cached HTML when a cache hit (
    304 Not Modified) means the changed_pages set is empty.

    The state files live under cache/.state/*.json and map URLs to a relative
    raw_file path that should be re-read from disk.
    """
    pages: list[dict] = []
    state_dir = os.path.join(cache_dir, ".state")
    if not os.path.isdir(state_dir):
        return pages

    for filename in sorted(os.listdir(state_dir)):
        if not filename.endswith(".json"):
            continue
        state_path = os.path.join(state_dir, filename)
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                payload = json.load(f) or {}
            source_name = payload.get("source") or os.path.splitext(filename)[0]
            for url, meta in (payload.get("pages") or {}).items():
                raw_file = (meta or {}).get("raw_file")
                if not raw_file:
                    continue
                html_path = os.path.join(cache_dir, raw_file)
                if os.path.isfile(html_path):
                    pages.append(
                        {
                            "source_name": source_name,
                            "url": url,
                            "raw_path": html_path,
                        }
                    )
        except Exception as exc:
            print(f"⚠️ Could not read crawler state {state_path}: {exc}")

    return pages


def _process_crawled_html(
    cache_dir: str,
    knowledge_dir: str,
    changed_pages: list[dict],
) -> int:
    """
    Process the crawler output into OKF concept files. The legacy code only read
    the changed pages produced from the latest HTTP downloads. That means a
    cache-driven crawl that receives 304 responses can leave cache/ populated
    but the knowledge repo empty because `changed_pages` is empty. This function now
    recovers the cached crawler pages from the on-disk state whenever the latest
    crawl didn't actually change any pages.
    """
    state_manager = StateManager(cache_dir)
    pages_to_process = changed_pages or state_manager.get_all_crawler_states()

    # Keep the live UI honest while the HTML->Markdown conversion is happening:
    # the crawler discovered a list of candidate source URLs, and the conversion
    # step can immediately report a progress denominator to the shared status object.
    update_status(
        message="Processing crawled documentation",
        discovered=len(pages_to_process) if pages_to_process else 0,
        total_documents=max(0, len(pages_to_process)),
        processed=0,
    )

    processed = 0

    for page in pages_to_process:
        html_path = page["raw_path"]
        source_name = page["source_name"]
        source_url = page["url"]

        if not os.path.isfile(html_path):
            continue

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

            cleaned_html = clean_html(
                html,
                base_url=source_url,
            )

            markdown = html_to_markdown(cleaned_html)

            if not markdown.strip():
                print(f"⚠️ Skipping empty crawled document: {html_path}")
                continue

            category = source_name.lower()

            concepts = split_into_concepts(
                markdown=markdown,
                category=category,
                source_name=source_name,
                source_url=source_url,
            )

            # Remove previous concepts belonging to this URL.
            delete_concepts_by_source_urls(
                [source_url],
                knowledge_dir=settings.KNOWLEDGE_DIR,
            )

            for concept_id, _title, content in concepts:
                write_concept_file(
                    knowledge_dir=knowledge_dir,
                    category=category,
                    concept_id=concept_id,
                    content=content,
                )

            processed += 1
            update_status(
                message="Formatting crawled HTML into OKF knowledge",
                processed=processed,
                total_documents=max(0, len(pages_to_process)),
                progress_percent=min(
                    100,
                    int(round((processed / max(1, len(pages_to_process))) * 100)),
                ),
            )

        except Exception as exc:
            update_status(
                status="failed",
                message=str(exc),
            )
            print(
                f"⚠️ Failed to process crawled HTML "
                f"{html_path}: {exc}"
            )

    return processed

def run_ingestion_pipeline(cache_dir: str = None, knowledge_dir: str = None):
    """
    The master orchestration function.
    1. Crawls official documentation (stored in cache).
    2. Loads local raw documents from cache.
    3. Extracts OKF Metadata via LLM.
    4. Converts to OKF-compliant frontmatter.
    5. Saves physical OKF Markdown files to knowledge directory (source of truth).
    6. Chunks and indexes into Qdrant.
    
    Args:
        cache_dir: Disposable cache for HTML and raw files (default: settings.CACHE_DIR)
        knowledge_dir: Source of truth for OKF Markdown (default: settings.KNOWLEDGE_DIR)
    """
    if cache_dir is None:
        cache_dir = settings.CACHE_DIR
    if knowledge_dir is None:
        knowledge_dir = settings.KNOWLEDGE_DIR

    print("🚀 Starting OKF Ingestion Pipeline...")
    update_status(
        status="running",
        message="Ingestion started",
        discovered=0,
        fetched=0,
        processed=0,
        failed=0,
        indexed=0,
        indexed_documents=0,
    )

    # 0. Crawl configured official documentation sources.
    crawl_result = asyncio.run(crawl_configured_sources(cache_dir=cache_dir))

    update_status(
        message="Documentation crawl completed",
        discovered=crawl_result["discovered"],
        fetched=crawl_result["fetched"],
        failed=crawl_result["failed"],
    )

    print(
        "🌐 Documentation crawl complete: "
        f"sources={crawl_result['sources']} "
        f"discovered={crawl_result['discovered']} "
        f"changed={crawl_result['changed']} "
        f"unchanged={crawl_result['unchanged']} "
        f"deleted={crawl_result['deleted']} "
        f"failed={crawl_result['failed']}"
    )

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

    # 1. Convert crawled HTML into OKF concept files.
    crawled_count = _process_crawled_html(
        cache_dir=cache_dir,
        knowledge_dir=knowledge_dir,
        changed_pages=crawl_result.get("changed_pages", []),
    )

    update_status(
        message="Processing crawled documentation",
        processed=crawled_count,
    )

    print(
        f"📚 Converted {crawled_count} crawled HTML documents "
        f"into OKF concepts."
    )

    # 2. Ensure LLM and Embeddings are configured.
    configure_llm_settings()

    # 3. Load existing local raw documents using StateManager.
    state_manager = StateManager(cache_dir)
    processing_state = state_manager.load_processing_state()

    changed_local_files, processing_state = state_manager.get_changed_files(processing_state)

    print(
        f"📂 Local cached files: changed/new={len(changed_local_files)}"
    )

    # Re-run the local raw conversion whenever the pipeline is invoked from the
    # API even for a cache hit crawl. The incremental state only tells us which
    # inputs changed. However a fresh call into the API should still have the
    # filesystem authoritative input count at its disposal. When the state
    # indicates 'no changed files' we can fall back to the full cache tree rather
    # than silently treating the repository as empty.
    if changed_local_files:
        local_files = changed_local_files
    else:
        local_files = state_manager.discover_local_files()

    raw_docs = []
    for file_path in local_files:
        try:
            reader = SimpleDirectoryReader(
                input_files=[file_path]
            )
            raw_docs.extend(reader.load_data())
        except Exception as exc:
            print(
                f"⚠️ Failed to load local file "
                f"{file_path}: {exc}"
            )

    print(
        f"📄 Loading {len(raw_docs)} local documents for processing."
    )

    update_status(
        status="running",
        message="Preparing local document conversion",
        total_documents=len(raw_docs),
        processed=crawled_count,
        discovered=crawl_result.get("discovered", 0),
        fetched=crawl_result.get("fetched", 0),
        failed=crawl_result.get("failed", 0),
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
            category_dir = os.path.join(knowledge_dir, str(okf_meta.get("category") or "reference").strip())
            os.makedirs(category_dir, exist_ok=True)

            # Physically save the OKF-formatted Markdown file to disk
            format_and_save_okf(
                text=doc.text,
                metadata=okf_meta,
                output_dir=category_dir,
                filename=filename,
            )

            saved_count += 1
            update_status(
                status="running",
                message=f"Saving OKF file {saved_count}/{len(raw_docs)}",
                processed=crawled_count + saved_count,
                total_documents=len(raw_docs) + max(0, crawled_count),
                indexed_documents=0,
            )

            source_file = okf_meta.get("source_file")

            if source_file:
                for changed_path in changed_local_files:
                    relative_path = os.path.relpath(changed_path, cache_dir)

                    if (
                        source_file == os.path.basename(changed_path)
                        or source_file == relative_path
                    ):
                        processing_state = state_manager.update_file_state(
                            changed_path,
                            filename,
                            processing_state
                        )
                        break

            state_manager.save_processing_state(processing_state)

    print(
    f"💾 Local ingestion saved {saved_count} OKF documents. "
    f"Crawled documentation produced {crawled_count} source documents."
    )

    # 5. Re-read the OKF files just written from disk (the source of truth) and
    #    index them into Qdrant via the shared indexer path. This guarantees the
    #    vector store always mirrors the filesystem knowledge base — the same
    #    documents, metadata, and provenance that search + query layers consume.
    print("📦 Re-reading OKF files and connecting to Qdrant for vector indexing...")
    concepts = load_all_concepts(knowledge_dir, use_cache=False)
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

    update_status(
        status="completed",
        message="Ingestion completed",
        processed=crawled_count + saved_count,
        indexed=len(docs),
        failed=crawl_result["failed"],
    )

    print("✅ Ingestion Pipeline Complete!")
    return {"status": "success", "indexed_documents": len(docs)}