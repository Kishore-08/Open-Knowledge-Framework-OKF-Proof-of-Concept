"""
Track which knowledge files have been embedded into Qdrant.

The filesystem knowledge repository is the source of truth; this state file
(`cache/.state/vector_index.json`) is a disposable acceleration cache that lets
the pipeline skip unchanged documents and avoid burning Gemini embedding quota
on every docker compose restart or re-ingestion run.
"""

from __future__ import annotations

import hashlib
import json
import os
from typing import Dict, List, Optional, Set, Tuple

from llama_index.core import Document

from app.core.config import settings


def content_hash_for_document(doc: Document) -> str:
    """Stable hash of a concept's embeddable text + id."""
    digest = hashlib.sha256()
    digest.update(doc.text.encode("utf-8"))
    digest.update((doc.metadata.get("id") or "").encode("utf-8"))
    return digest.hexdigest()


class VectorIndexState:
    """On-disk map of knowledge `source_file` -> last indexed content hash."""

    VERSION = 1

    def __init__(self, entries: Optional[Dict[str, Dict[str, str]]] = None):
        self.entries: Dict[str, Dict[str, str]] = entries or {}

    @classmethod
    def load(cls, cache_dir: Optional[str] = None) -> "VectorIndexState":
        cache_dir = cache_dir or settings.CACHE_DIR
        path = cls._state_path(cache_dir)
        if not os.path.exists(path):
            return cls()
        try:
            with open(path, "r", encoding="utf-8") as handle:
                payload = json.load(handle) or {}
            entries = payload.get("entries") if isinstance(payload, dict) else {}
            return cls(entries if isinstance(entries, dict) else {})
        except (OSError, json.JSONDecodeError) as exc:
            print(f"⚠️ Could not load vector index state from {path}: {exc}")
            return cls()

    def save(self, cache_dir: Optional[str] = None) -> None:
        cache_dir = cache_dir or settings.CACHE_DIR
        state_dir = os.path.join(cache_dir, ".state")
        os.makedirs(state_dir, exist_ok=True)
        path = self._state_path(cache_dir)
        temp_path = f"{path}.tmp"
        payload = {"version": self.VERSION, "entries": self.entries}
        with open(temp_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
        os.replace(temp_path, path)

    def clear(self) -> None:
        self.entries.clear()

    def is_current(self, source_file: str, content_hash: str) -> bool:
        entry = self.entries.get(source_file) or {}
        return entry.get("content_hash") == content_hash

    def mark_indexed(self, source_file: str, content_hash: str) -> None:
        if not source_file:
            return
        self.entries[source_file] = {"content_hash": content_hash}

    def remove(self, source_file: str) -> None:
        self.entries.pop(source_file, None)

    @staticmethod
    def _state_path(cache_dir: str) -> str:
        return os.path.join(cache_dir, ".state", "vector_index.json")


def filter_documents_for_indexing(
    docs: List[Document],
    *,
    updated_paths: Optional[Set[str]] = None,
    force_full: bool = False,
    cache_dir: Optional[str] = None,
) -> Tuple[List[Document], int]:
    """
    Return documents that still need embedding, plus a skip count.

    A document is indexed when any of the following is true:
      - `force_full` is set,
      - its knowledge `source_file` was written/updated in this pipeline run,
      - it is missing from Qdrant (e.g. after a partial run or volume wipe),
      - its content hash differs from the last successful index recorded locally.
    """
    if force_full:
        return docs, 0

    # Local import avoids a circular import through app.retrieval -> app.ingestion.
    from app.retrieval.hybrid_search import get_indexed_source_files

    updated_paths = updated_paths or set()
    state = VectorIndexState.load(cache_dir)
    qdrant_indexed = get_indexed_source_files()

    # Qdrant was wiped but local state survived — treat everything as stale.
    if state.entries and not qdrant_indexed:
        print(
            "ℹ️ Qdrant collection is empty but vector index state exists; "
            "re-indexing all concepts."
        )
        state.clear()

    need: List[Document] = []
    skipped = 0
    for doc in docs:
        source_file = doc.metadata.get("source_file")
        if not source_file:
            need.append(doc)
            continue

        content_hash = content_hash_for_document(doc)
        if (
            source_file in updated_paths
            or source_file not in qdrant_indexed
            or not state.is_current(source_file, content_hash)
        ):
            need.append(doc)
        else:
            skipped += 1

    return need, skipped


def mark_documents_indexed(
    docs: List[Document],
    *,
    cache_dir: Optional[str] = None,
) -> None:
    """Persist successful indexing results for incremental future runs."""
    state = VectorIndexState.load(cache_dir)
    for doc in docs:
        source_file = doc.metadata.get("source_file")
        if not source_file:
            continue
        state.mark_indexed(source_file, content_hash_for_document(doc))
    state.save(cache_dir)
