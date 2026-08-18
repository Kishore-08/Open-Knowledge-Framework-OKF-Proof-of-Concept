import os
import re
import asyncio
import hashlib
import json
import threading
from pathlib import Path
from datetime import date
from typing import Optional

# Internal imports
from .loaders import load_raw_documents
from .crawler import crawl_configured_sources
from .metadata_extractor import generate_okf_metadata
from app.ingestion.status import update_status
from app.indexing.indexer import concepts_to_documents
from app.indexing.vector_state import filter_documents_for_indexing
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
    load_concepts_from_paths,
    delete_concepts_by_source_urls,
)
from app.retrieval.hybrid_search import (
    index_documents,
    delete_points_by_field,
)
from app.storage.state_manager import StateManager

from app.jobs.manager import JobCancelledError

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

def _check_cancelled(cancel_event: Optional[threading.Event]) -> None:
    """Cooperative cancellation check between pipeline stages."""
    if cancel_event is not None and cancel_event.is_set():
        update_status(
            status="failed",
            message="Ingestion cancelled by user",
        )
        raise JobCancelledError


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


def _knowledge_has_concepts(knowledge_dir: str) -> bool:
    """True when the knowledge repository already contains OKF concept files."""
    if not os.path.isdir(knowledge_dir):
        return False
    for dirpath, _dirnames, filenames in os.walk(knowledge_dir):
        if "_quarantine" in dirpath:
            continue
        if any(name.endswith(".md") for name in filenames):
            return True
    return False


def _track_knowledge_path(knowledge_dir: str, path: str, updated_paths: set[str]) -> None:
    """Record a knowledge file (absolute or relative) for incremental indexing."""
    if not path:
        return
    if os.path.isabs(path):
        rel = os.path.relpath(path, knowledge_dir)
    else:
        rel = path
    updated_paths.add(rel.replace("\\", "/"))


def _process_crawled_html(
    cache_dir: str,
    knowledge_dir: str,
    changed_pages: list[dict],
    cancel_event: Optional[threading.Event] = None,
    source_names: Optional[list] = None,
    updated_knowledge_paths: Optional[set[str]] = None,
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

    if source_names is None:
        # Default behaviour: only convert pages that changed in this crawl.
        # Recover the full cached crawl ONLY on first bootstrap when knowledge/
        # is still empty — otherwise every re-run would re-convert hundreds of
        # pages and trigger a full Qdrant re-embed (expensive Gemini quota).
        if changed_pages:
            pages_to_process = changed_pages
        elif not _knowledge_has_concepts(knowledge_dir):
            pages_to_process = _discover_cached_crawl_pages(cache_dir)
        else:
            pages_to_process = []
    else:
        # Explicit source selection: process ONLY what was freshly downloaded for
        # the selected sources. Never fall back to cached pages from earlier
        # runs — the user asked for a fresh crawl of the official documentation.
        if not source_names:
            pages_to_process = []
        else:
            selected = {s.lower() for s in source_names}
            candidates = changed_pages or []
            if not candidates and not _knowledge_has_concepts(knowledge_dir):
                candidates = _discover_cached_crawl_pages(cache_dir)
            pages_to_process = [
                p for p in candidates
                if (p.get("source_name") or "").lower() in selected
            ]

    # Keep the live UI honest while the HTML->Markdown conversion is happening:
    # the crawler discovered a list of candidate source URLs, and the conversion
    # step can immediately report a progress denominator to the shared status object.
    update_status(
        stage="converting",
        stage_message="Starting the ingestion pipeline from the cache folder",
        message="Processing crawled documentation",
        discovered=len(pages_to_process) if pages_to_process else 0,
        total_documents=max(0, len(pages_to_process)),
        processed=0,
    )

    processed = 0
    written_paths = []

    for page in pages_to_process:
        _check_cancelled(cancel_event)
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
                written_path = write_concept_file(
                    knowledge_dir=knowledge_dir,
                    category=category,
                    concept_id=concept_id,
                    content=content,
                )

                written_paths.append(written_path)

                if updated_knowledge_paths is not None:
                    _track_knowledge_path(knowledge_dir, written_path, updated_knowledge_paths)

            processed += 1
            update_status(
                stage="converting",
                stage_message="Converting cached raw data into OKF knowledge files",
                message="Formatting crawled HTML into OKF knowledge",
                processed=processed,
                total_documents=max(0, len(pages_to_process)),
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

    return processed, written_paths

def run_ingestion_pipeline(
    cache_dir: str = None,
    knowledge_dir: str = None,
    cancel_event: Optional[threading.Event] = None,
    source_names: Optional[list] = None,
    only_files: Optional[list] = None,
):
    """
    The master orchestration function.
    1. Crawls official documentation (stored in cache) for the selected sources.
    2. Loads local raw documents from cache.
    3. Extracts OKF Metadata via LLM.
    4. Converts to OKF-compliant frontmatter.
    5. Saves physical OKF Markdown files to knowledge directory (source of truth).
    6. Chunks and indexes into Qdrant.
    
    Args:
        cache_dir: Disposable cache for HTML and raw files (default: settings.CACHE_DIR)
        knowledge_dir: Source of truth for OKF Markdown (default: settings.KNOWLEDGE_DIR)
        cancel_event: Optional threading.Event; when set, the pipeline aborts at the
            next stage boundary (cooperative cancellation).
        source_names: Optional list of documentation source names (from sources.yaml)
            to crawl. None = crawl the enabled sources; an empty list = skip
            crawling entirely (process only cached/uploaded files); a non-empty
            list = crawl only those sources.
        only_files: Optional list of filenames (relative to cache_dir) to process.
            When provided the pipeline enters "upload-only" mode: crawling is
            skipped entirely and ONLY these files are converted + indexed, so an
            uploaded document is never mixed with cached crawl pages or other
            previously cached files.
    """
    if cache_dir is None:
        cache_dir = settings.CACHE_DIR
    if knowledge_dir is None:
        knowledge_dir = settings.KNOWLEDGE_DIR

    upload_only = bool(only_files)
    updated_knowledge_paths: set[str] = set()

    print("🚀 Starting OKF Ingestion Pipeline...")
    update_status(
        status="running",
        stage="starting",
        stage_message="Initializing the ingestion pipeline",
        message="Ingestion started",
        discovered=0,
        fetched=0,
        processed=0,
        failed=0,
        indexed=0,
        indexed_documents=0,
        rate_limit_hits=0,
        prompt_tokens_estimate=0,
        completion_tokens_estimate=0,
        total_tokens_estimate=0,
        current_source="",
    )

    # 0. Crawl the selected official documentation sources (skipped in
    # upload-only mode: an uploaded document must not be mixed with crawls).
    if upload_only:
        print("ℹ️ Upload-only mode: skipping documentation crawl.")
        crawl_result = {
            "sources": 0,
            "discovered": 0,
            "fetched": 0,
            "changed": 0,
            "unchanged": 0,
            "deleted": 0,
            "failed": 0,
            "changed_urls": [],
            "changed_pages": [],
            "deleted_urls": [],
        }
    else:
        crawl_result = asyncio.run(
            crawl_configured_sources(
                cache_dir=cache_dir,
                source_names=source_names,
            )
        )

    _check_cancelled(cancel_event)

    update_status(
        stage="cached",
        stage_message="Raw data downloaded and stored in the cache folder",
        message="Documentation crawl completed",
        discovered=crawl_result["discovered"],
        fetched=crawl_result["fetched"],
        failed=crawl_result["failed"],
        current_source="",
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
    _check_cancelled(cancel_event)

    crawled_count, crawled_okf_paths = _process_crawled_html(
        cache_dir=cache_dir,
        knowledge_dir=knowledge_dir,
        changed_pages=crawl_result.get("changed_pages", []),
        cancel_event=cancel_event,
        source_names=[] if upload_only else source_names,
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

    if upload_only:
        # Only the files that were just uploaded are eligible. Never fall back to
        # the whole cache tree. Still compare the selected files with processing
        # state: uploading an identical file twice must not repeat metadata LLM
        # calls or embedding work.
        local_files = []
        for filename in only_files or []:
            path = filename if os.path.isabs(filename) else os.path.join(cache_dir, filename)
            if os.path.isfile(path):
                local_files.append(path)
            else:
                print(f"⚠️ Uploaded file not found in cache: {path}")
        changed_local_files = []
        previous_files = processing_state.setdefault("files", {})
        for path in local_files:
            relative_path = os.path.relpath(path, cache_dir)
            if previous_files.get(relative_path, {}).get("content_hash") != _file_hash(path):
                changed_local_files.append(path)
        print(
            f"📂 Upload-only files: selected={len(local_files)} "
            f"changed/new={len(changed_local_files)} "
            f"unchanged={len(local_files) - len(changed_local_files)}"
        )
    elif source_names:
        # A source-triggered crawl must remain scoped to those documentation
        # sources.  Manual files sitting at the cache root belong to the
        # cached/upload flow and otherwise make `processed` exceed `fetched`
        # in the monitoring UI (and unexpectedly ingest unrelated content).
        changed_local_files = []
    else:
        changed_local_files, processing_state = state_manager.get_changed_files( processing_state )

    print(
        f"📂 Local cached files: "
        f"changed/new={len(changed_local_files)}")

    local_files = changed_local_files

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

    # `fetched` represents inputs successfully made available in cache for this
    # run. Include local/uploaded document units once they have been loaded so
    # the dashboard compares like-for-like counters and never reports more
    # processed inputs than fetched inputs.
    fetched_inputs = crawl_result.get("fetched", 0) + len(raw_docs)

    update_status(
        status="running",
        stage="formatting",
        stage_message="Extracting metadata and writing OKF knowledge files",
        message="Preparing local document conversion",
        total_documents=crawled_count + len(raw_docs),
        processed=crawled_count,
        discovered=crawl_result.get("discovered", 0),
        fetched=fetched_inputs,
        failed=crawl_result.get("failed", 0),
    )

    saved_count = 0
    changed_okf_paths = []

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

    # ThreadPoolExecutor rejects max_workers=0.  Zero local documents is normal
    # for source-only crawls and unchanged-cache runs, so simply skip this
    # optional phase and continue to indexing/reuse.
    if raw_docs:
        pool = ThreadPoolExecutor(max_workers=min(3, len(raw_docs)))
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

            category_dir = os.path.join(
                knowledge_dir,
                str(
                    okf_meta.get("category")
                    or "reference"
                ).strip()
            )

            os.makedirs(category_dir, exist_ok=True)

            format_and_save_okf(
                text=doc.text,
                metadata=okf_meta,
                output_dir=category_dir,
                filename=filename,
            )

            saved_okf_path = os.path.join(
                category_dir,
                filename,
            )

            changed_okf_paths.append(saved_okf_path)

            _track_knowledge_path(
                knowledge_dir,
                os.path.join(category_dir, filename),
                updated_knowledge_paths,
            )

            saved_count += 1
            update_status(
                status="running",
                stage="formatting",
                stage_message="Extracting metadata and writing OKF knowledge files",
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
        pool.shutdown(wait=True)

    print(
    f"💾 Local ingestion saved {saved_count} OKF documents. "
    f"Crawled documentation produced {crawled_count} source documents."
    )

    # 5. Re-read the OKF files just written from disk (the source of truth) and
    #    index them into Qdrant via the shared indexer path. This guarantees the
    #    vector store always mirrors the filesystem knowledge base — the same
    #    documents, metadata, and provenance that search + query layers consume.
    _check_cancelled(cancel_event)

    print(
        "📦 Connecting to Qdrant for incremental vector indexing..."
    )

    update_status(
        stage="indexing",
        stage_message="Indexing changed OKF knowledge into Qdrant",
        message="Indexing changed concepts into the vector database",
        current_source="",
    )

    all_changed_okf_paths = list(
        dict.fromkeys(
            crawled_okf_paths
            + changed_okf_paths
        )
    )

    print(
        f"📦 Changed OKF concepts to index: "
        f"{len(all_changed_okf_paths)}"
    )

    if not all_changed_okf_paths:
        print(
            "✅ No knowledge files changed. "
            "Existing Qdrant vectors will be reused."
        )

        update_status(
            status="completed",
            stage="completed",
            stage_message="No knowledge changes detected",
            message="Existing Qdrant index reused",
            processed=crawled_count + saved_count,
            indexed=0,
            failed=crawl_result["failed"],
            current_source="",
        )

        return {
            "status": "success",
            "indexed_documents": 0,
            "message": "No changes detected; existing Qdrant vectors reused.",
        }


    concepts = load_concepts_from_paths(
        all_changed_okf_paths
    )

    docs = concepts_to_documents(concepts)

    if not docs:
        print(
            "⚠️ Changed files produced no valid OKF concepts; "
            "nothing to index."
        )

        return {
            "status": "skipped",
            "message": "No valid changed OKF concepts were produced.",
        }

    # Conversion state and vector state are separate on purpose. A crawler or
    # upload may produce an OKF path that already has the same successfully
    # indexed content (for example after state recovery or a repeated upload).
    # Check both Qdrant presence and the last successful content hash before any
    # embedding call so those documents consume no embedding quota.
    docs_to_index, skipped = filter_documents_for_indexing(
        docs,
        cache_dir=cache_dir,
    )

    if skipped:
        print(
            f"♻️ Reusing {skipped} unchanged concept(s) already present "
            "in Qdrant; no embeddings requested."
        )

    if not docs_to_index:
        update_status(
            status="completed",
            stage="completed",
            stage_message="All changed candidates are already indexed",
            message="Existing Qdrant index reused",
            processed=crawled_count + saved_count,
            indexed=0,
            failed=crawl_result["failed"],
            current_source="",
        )
        return {
            "status": "success",
            "indexed_documents": 0,
            "skipped_documents": skipped,
            "message": "All candidate concepts were unchanged; existing Qdrant vectors reused.",
        }


    source_files = [
        d.metadata["source_file"]
        for d in docs_to_index
        if d.metadata.get("source_file")
    ]


    print(
        f"🧠 Sending only {len(docs_to_index)} new/changed "
        f"concept(s) for embedding."
    )


    _index, failed_ids = index_documents(
        docs_to_index,
        collection_name=settings.QDRANT_CONCEPTS_COLLECTION,
        source_files=source_files,
        show_progress=True,
        base_failed_count=crawl_result["failed"],
        cancel_event=cancel_event,
    )
    if failed_ids:
            print(
            f"⚠️ {len(failed_ids)}/{len(docs_to_index)} document(s) were not indexed into Qdrant "
            "after retries (see log above). Filesystem knowledge/ still has them, so "
            "keyword search will find them; re-run ingestion to retry indexing."
        )

    update_status(
        status="completed",
        stage="completed",
        stage_message="Ingestion completed — knowledge is stored in OKF format and indexed",
        message="Ingestion completed",
        processed=crawled_count + saved_count,
        indexed=len(docs_to_index) - len(failed_ids),
        failed=crawl_result["failed"] + len(failed_ids),
        current_source="",
    )

    print("✅ Ingestion Pipeline Complete!")
    return {
        "status": "success",
        "indexed_documents": len(docs_to_index) - len(failed_ids),
        "skipped_documents": skipped,
        "failed_documents": len(failed_ids),
    }
