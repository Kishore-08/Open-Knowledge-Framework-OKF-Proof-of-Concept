import os
import time
import threading
from typing import List, Optional

import qdrant_client
from qdrant_client.http import models as qdrant_models
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.core.config import settings
from app.core.retry import retry_with_backoff


def get_qdrant_vector_store(collection_name: str = None) -> QdrantVectorStore:
    """
    Initializes a connection to the Qdrant Vector Database.

    NOTE: enable_hybrid is intentionally set to False.
    fastembed 0.8.x + qdrant-client 1.18.x + llama-index-vector-stores-qdrant 0.10.x
    have a payload API mismatch that causes Qdrant to return '503 Illegal metadata'
    whenever fastembed tries to configure sparse-vector metadata on a collection.
    Dense semantic search via Gemini embeddings is used instead - it provides
    equally strong retrieval quality without the version-compatibility issue.
    """
    if collection_name is None:
        collection_name = settings.QDRANT_CONCEPTS_COLLECTION

    qdrant_url = os.getenv("QDRANT_URL", settings.QDRANT_URL)

    print(f"🔌 Connecting to Qdrant at {qdrant_url}...")

    # Use a generous timeout (300 s) so large ingestion batches don't trigger
    # "Timeout of 60.0s exceeded" errors during embedding + upsert.
    client = qdrant_client.QdrantClient(
        url=qdrant_url,
        timeout=300,
    )

    # enable_hybrid=False — avoids fastembed / Qdrant-payload 503 errors.
    # batch_size=10 keeps per-request payloads small to reduce transient failures.
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        enable_hybrid=False,
        batch_size=10,
    )

    return vector_store


def get_qdrant_client() -> qdrant_client.QdrantClient:
    """Utility function to get the raw client for checking collection stats."""
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    return qdrant_client.QdrantClient(url=qdrant_url, timeout=300)


def reset_hybrid_collection(collection_name: str = None) -> None:
    """
    Delete a Qdrant collection that was created with hybrid (sparse) vectors.

    A collection created by an earlier `enable_hybrid=True` run (or by a different
    library version) keeps sparse-vector configuration that conflicts with the
    dense-only points this codebase upserts, producing Qdrant's '503 Illegal
    metadata' error. Because the filesystem knowledge repository is the source of
    truth, it is safe to drop and rebuild such a collection.
    """
    if collection_name is None:
        collection_name = settings.QDRANT_CONCEPTS_COLLECTION
    try:
        client = get_qdrant_client()
        if not client.collection_exists(collection_name):
            print(f"ℹ️ Collection '{collection_name}' does not exist; nothing to reset.")
            return

        info = client.get_collection(collection_name)
        params = info.config.params if info.config else None
        sparse_vectors = getattr(params, "sparse_vectors", None) if params else None

        if sparse_vectors:
            print(
                f"⚠️ Collection '{collection_name}' has hybrid sparse-vector config "
                "(known cause of '503 Illegal metadata'); deleting so it is rebuilt dense-only."
            )
            client.delete_collection(collection_name)
        else:
            print(f"ℹ️ Collection '{collection_name}' is dense-only; keeping it.")
    except Exception as exc:  # noqa: BLE001 - best-effort cleanup
        print(f"ℹ️ Could not inspect/reset collection '{collection_name}': {exc}")


def delete_points_by_field(
    collection_name: str,
    field: str,
    values: List[str],
) -> None:
    """
    Delete every Qdrant point whose payload `field` matches one of `values`.

    Used to make ingestion idempotent: re-ingesting the same source file removes
    the previously stored chunks (whose node ids are random UUIDs) before the new
    chunks are upserted, preventing duplicate documents in the vector store.
    """
    values = [v for v in values if v]
    if not values:
        return
    client = get_qdrant_client()
    if not client.collection_exists(collection_name):
        return
    client.delete(
        collection_name=collection_name,
        points_selector=qdrant_models.FilterSelector(
            filter=qdrant_models.Filter(
                must=[
                    qdrant_models.FieldCondition(
                        key=field,
                        match=qdrant_models.MatchAny(any=values),
                    )
                ]
            )
        ),
    )
    print(f"🗑️ Removed previous points for {len(values)} source file(s) from '{collection_name}'.")


def index_documents(
    documents,
    *,
    collection_name: Optional[str] = None,
    source_files: Optional[List[str]] = None,
    show_progress: bool = False,
    base_failed_count: int = 0,
    cancel_event: Optional[threading.Event] = None,
):
    """
    Chunk, embed, and upsert documents into the Qdrant concept collection.

    Shared by the ingestion pipeline and the concept indexer so that both paths
    write to the vector store identically:
      1. reset any hybrid (sparse) leftovers,
      2. delete previously stored chunks for the given source files (idempotent),
      3. chunk + embed + upsert the documents, one at a time, with the same
         429/quota retry-with-backoff policy used for answer generation.

    IMPORTANT: this used to call `VectorStoreIndex.from_documents(documents, ...)`
    in one shot with no retry handling around the embedding calls. On the Gemini
    free tier that meant the *first* 429 anywhere in a batch of hundreds of
    documents raised and aborted the whole call - which is why ingestion runs
    were observed to silently stop after ~79/874 documents indexed, leaving
    semantic search permanently degraded until a full manual re-run. Indexing
    one document at a time means a transient quota error only costs that one
    document (which is retried with backoff, same as `app.query.engine`), and a
    failure that exhausts retries is skipped and reported instead of aborting
    the remaining hundreds of documents.

    Returns the VectorStoreIndex plus the list of document ids that failed to
    index after retries were exhausted (empty on full success).

    `base_failed_count` lets the caller seed the reported "failed" counter
    with failures from earlier pipeline stages (e.g. crawl failures), so the
    live UI status shows a cumulative total instead of the count visibly
    dropping back to 0 the moment indexing starts.

    `cancel_event`: checked between documents (not just once before this
    function is called) so the Stop button actually takes effect promptly
    during a long, rate-limit-heavy indexing run instead of only being
    honored once the entire batch finishes.
    """
    from app.jobs.manager import JobCancelledError
    collection_name = collection_name or settings.QDRANT_CONCEPTS_COLLECTION
    source_files = source_files or []

    vector_store = get_qdrant_vector_store(collection_name)
    reset_hybrid_collection(collection_name)
    delete_points_by_field(collection_name, "source_file", source_files)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    splitter = SentenceSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )

    index = VectorStoreIndex(
        nodes=[],
        storage_context=storage_context,
        transformations=[splitter],
    )

    # Local import: app.ingestion.status -> app.jobs.manager has no back-reference
    # to app.retrieval, but importing at module level here would still force
    # `app.ingestion`'s package __init__ (which imports pipeline.py, which
    # imports *this* module) to run first - a local import sidesteps that
    # entirely and matches the pattern already used elsewhere in this codebase
    # (e.g. app/query/search.py's "auto" mode) for the same reason.
    from app.ingestion.status import update_status

    failed_ids: List[str] = []
    rate_limit_hits = 0
    total = len(documents)

    # Report the indexing phase's real denominator up front - without this the
    # UI has no total to compute "indexed / total" progress against during
    # what is often the longest, most rate-limit-prone phase of a run.
    update_status(
        stage="indexing",
        stage_message="Indexing OKF knowledge into Qdrant",
        message=f"Embedding and indexing {total} document(s) into Qdrant",
        total_documents=total,
        current_source="",
    )

    for i, doc in enumerate(documents, start=1):
        if cancel_event is not None and cancel_event.is_set():
            print(f"🛑 Indexing cancelled after {i - 1}/{total} document(s).")
            update_status(
                stage="indexing",
                stage_message="Indexing cancelled",
                message=f"Indexing cancelled after {i - 1}/{total} document(s)",
            )
            raise JobCancelledError

        doc_id = doc.metadata.get("id") or doc.metadata.get("source_file") or f"doc-{i}"
        doc_title = doc.metadata.get("title") or doc_id

        def _on_retry(attempt: int, delay: float, exc: Exception, doc_id=doc_id, doc_title=doc_title) -> None:
            nonlocal rate_limit_hits
            rate_limit_hits += 1
            warning = (
                f"⚠️ Embedding rate limit (429) hit for '{doc_id}', retrying in "
                f"{delay:.0f}s (attempt {attempt}/{settings.LLM_MAX_RETRIES})"
            )
            print(warning)
            # This is the whole point of the callback: previously the retry
            # warning only ever reached the container logs (`print` above),
            # never the UI, so a rate-limited run - which can add many
            # minutes of retries - looked indistinguishable from "stuck".
            update_status(
                message=warning,
                stage_message=f"Rate limited on '{doc_title}' \u2014 retrying in {delay:.0f}s",
                current_source=doc_title,
                rate_limit_hits=rate_limit_hits,
            )

        try:
            retry_with_backoff(
                lambda doc=doc: index.insert(doc),
                max_retries=settings.LLM_MAX_RETRIES,
                base_delay=settings.LLM_RETRY_BASE_DELAY,
                sleep=time.sleep,
                on_retry=_on_retry,
            )
        except Exception as exc:  # noqa: BLE001 - one bad document must not abort the run
            failed_ids.append(doc_id)
            print(f"❌ Failed to index '{doc_id}' after retries, skipping: {exc}")

        # Update every document, not just every 25th: indexing is the phase
        # most likely to stall on rate limits, so this is exactly where the
        # UI most needs live feedback that something is actually happening.
        indexed_so_far = i - len(failed_ids)
        update_status(
            stage="indexing",
            stage_message="Indexing OKF knowledge into Qdrant",
            message=f"Indexed {indexed_so_far}/{total} document(s)"
                    + (f" \u2014 {len(failed_ids)} failed" if failed_ids else ""),
            indexed=indexed_so_far,
            indexed_documents=indexed_so_far,
            failed=base_failed_count + len(failed_ids),
            total_documents=total,
            current_source=doc_title,
        )

        if show_progress and (i % 25 == 0 or i == total):
            print(f"  ...indexed {indexed_so_far}/{total} documents ({len(failed_ids)} failed so far)")

    if failed_ids:
        print(
            f"⚠️ Indexing finished with {len(failed_ids)}/{total} document(s) failed "
            f"after retries: {failed_ids[:10]}{'...' if len(failed_ids) > 10 else ''}. "
            "Re-run indexing later to retry just the failures (idempotent re-ingest "
            "will replace any partially-indexed chunks for these source files)."
        )

    return index, failed_ids