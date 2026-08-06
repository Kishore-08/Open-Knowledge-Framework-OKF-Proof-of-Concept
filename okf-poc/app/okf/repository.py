"""
OKF knowledge repository.

The `knowledge/` directory is the canonical source of truth. Every concept is a
Markdown file with YAML frontmatter. This module reads, validates and searches that
repository directly from the filesystem, so the vector database is only an
acceleration layer (Phases 7 & 9).
"""

import os
import re
from typing import Dict, List, Optional

from app.core.config import settings
from app.okf.parser import parse_okf_file
from app.okf.schema import OKFConcept, OKFConceptFile


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def _concept_files(knowledge_dir: Optional[str] = None) -> List[str]:
    """Return all *.md files under the knowledge repository (non-recursive by category)."""
    root = knowledge_dir or settings.KNOWLEDGE_DIR
    if not os.path.isdir(root):
        return []
    files = []
    for dirpath, _dirnames, filenames in os.walk(root):
        # Skip the quarantine folder so junk concepts are backed up but never
        # loaded into the knowledge base.
        if "_quarantine" in dirpath:
            continue
        for name in filenames:
            if name.endswith(".md"):
                files.append(os.path.join(dirpath, name))
    return sorted(files)


def _cache_key(knowledge_dir: str) -> str:
    """Invalidate the module cache when any concept file changes."""
    files = _concept_files(knowledge_dir)
    if not files:
        return "empty"
    latest = max(os.path.getmtime(f) for f in files)
    return f"{len(files)}:{latest:.0f}"


_cache: Dict[str, List[OKFConceptFile]] = {}
_cache_knowledge_dir: Optional[str] = None
_cache_key_value: Optional[str] = None


def load_all_concepts(knowledge_dir: Optional[str] = None, use_cache: bool = True) -> List[OKFConceptFile]:
    """
    Load and validate every concept in the knowledge repository.
    Files whose frontmatter fails validation are skipped with a warning.
    """
    global _cache, _cache_knowledge_dir, _cache_key_value
    root = knowledge_dir or settings.KNOWLEDGE_DIR

    if use_cache and _cache_knowledge_dir == root and _cache_key_value == _cache_key(root):
        return _cache.get(root, [])

    concepts: List[OKFConceptFile] = []
    for path in _concept_files(root):
        try:
            raw_meta, body = parse_okf_file(path)
            meta = OKFConcept.model_validate(raw_meta)
            concepts.append(OKFConceptFile(metadata=meta, content=body.strip(), filepath=path))
        except Exception as exc:  # noqa: BLE001 - a single bad file must not break the repo
            print(f"⚠️ Skipping invalid OKF concept: {path} ({exc})")

    # cache for the duration of a process
    _cache[root] = concepts
    _cache_knowledge_dir = root
    _cache_key_value = _cache_key(root)
    return concepts


# ---------------------------------------------------------------------------
# Listing / lookup
# ---------------------------------------------------------------------------

def list_categories(knowledge_dir: Optional[str] = None) -> List[str]:
    """Sorted list of knowledge categories present in the repository."""
    return sorted({c.metadata.category for c in load_all_concepts(knowledge_dir)})


def list_concepts(category: Optional[str] = None, knowledge_dir: Optional[str] = None) -> List[dict]:
    """Lightweight metadata summaries for the concept browser."""
    out = []
    for concept in load_all_concepts(knowledge_dir):
        meta = concept.metadata
        if category and meta.category != category:
            continue
        out.append(
            {
                "id": meta.id,
                "title": meta.title,
                "description": meta.description,
                "category": meta.category,
                "tags": meta.tags,
                "type": meta.type,
                "source_url": meta.source.url if meta.source else None,
            }
        )
    return out


def get_concept(concept_id: str, knowledge_dir: Optional[str] = None) -> Optional[OKFConceptFile]:
    """Find a concept by its id or any of its aliases."""
    concept_id = concept_id.strip().lower()
    for concept in load_all_concepts(knowledge_dir):
        meta = concept.metadata
        if meta.id.lower() == concept_id:
            return concept
        for alias in meta.aliases:
            if alias.strip().lower() == concept_id:
                return concept
    return None


def get_concept_dict(concept_id: str, knowledge_dir: Optional[str] = None) -> Optional[dict]:
    """JSON-serializable view of a single concept (metadata + markdown body + source)."""
    concept = get_concept(concept_id, knowledge_dir)
    if concept is None:
        return None
    meta = concept.metadata
    return {
        "id": meta.id,
        "type": meta.type,
        "title": meta.title,
        "description": meta.description,
        "category": meta.category,
        "tags": meta.tags,
        "aliases": meta.aliases,
        "related": meta.related,
        "source": {"name": meta.source.name, "url": meta.source.url} if meta.source else None,
        "created_at": meta.created_at,
        "updated_at": meta.updated_at,
        "content": concept.content,
    }


# ---------------------------------------------------------------------------
# Search (keyword / metadata / tag)
# ---------------------------------------------------------------------------

_SEARCHABLE = ("title", "aliases", "description", "tags", "content")

_STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "do", "does",
    "did", "i", "you", "we", "they", "he", "she", "it", "is", "are", "was",
    "were", "be", "been", "how", "what", "when", "where", "which", "who", "why",
    "with", "from", "by", "at", "as", "that", "this", "these", "those", "my",
    "me", "your", "can", "could", "will", "would", "should", "not", "no", "yes",
}


def _field_text(concept: OKFConceptFile, field: str) -> str:
    meta = concept.metadata
    if field == "title":
        return meta.title
    if field == "aliases":
        return " ".join(meta.aliases)
    if field == "description":
        return meta.description
    if field == "tags":
        return " ".join(meta.tags)
    return concept.content


def search_concepts(
    query: str,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    knowledge_dir: Optional[str] = None,
) -> List[dict]:
    """
    Filesystem keyword + metadata + tag search over the knowledge repository.

    Returns concepts that match, ranked by how many searchable fields matched.
    This is intentionally dependency-free and complements semantic search.
    """
    tokens = [t.lower() for t in re.findall(r"[a-z0-9_-]+", query.lower())] if query else []
    tokens = [t for t in tokens if t not in _STOPWORDS]
    results = []

    for concept in load_all_concepts(knowledge_dir):
        meta = concept.metadata
        if category and meta.category != category:
            continue
        if tag and tag.lower() not in [t.lower() for t in meta.tags]:
            continue

        if not tokens:
            # metadata-only filter
            results.append({"id": meta.id, "title": meta.title, "category": meta.category,
                            "description": meta.description, "tags": meta.tags,
                            "source_url": meta.source.url if meta.source else None,
                            "score": 0.0, "matched_fields": []})
            continue

        matched_fields = []
        score = 0.0
        for field in _SEARCHABLE:
            text = _field_text(concept, field).lower()
            hits = sum(text.count(t) for t in tokens)
            if hits:
                matched_fields.append(field)
                score += hits * (2.0 if field in ("title", "aliases", "tags") else 1.0)

        if matched_fields:
            snippet = _snippet(concept.content, tokens)
            results.append({"id": meta.id, "title": meta.title, "category": meta.category,
                            "description": meta.description, "tags": meta.tags,
                            "source_url": meta.source.url if meta.source else None,
                            "snippet": snippet, "score": round(score, 3),
                            "matched_fields": matched_fields})

    results.sort(key=lambda r: r["score"], reverse=True)
    return results


def _snippet(content: str, tokens: List[str], radius: int = 120) -> str:
    """Small window of context around the first token match."""
    lower = content.lower()
    for token in tokens:
        idx = lower.find(token)
        if idx != -1:
            start = max(0, idx - radius)
            end = min(len(content), idx + radius)
            prefix = "..." if start > 0 else ""
            suffix = "..." if end < len(content) else ""
            return f"{prefix}{content[start:end].strip()}{suffix}"
    return content[: radius * 2]


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def knowledge_stats(knowledge_dir: Optional[str] = None) -> dict:
    """Statistics over the knowledge repository (Phase 11 /stats)."""
    concepts = load_all_concepts(knowledge_dir)
    by_category: Dict[str, int] = {}
    all_tags = set()
    source_names = set()
    for concept in concepts:
        meta = concept.metadata
        by_category[meta.category] = by_category.get(meta.category, 0) + 1
        all_tags.update(meta.tags)
        if meta.source:
            source_names.add(meta.source.name)
    return {
        "total_concepts": len(concepts),
        "categories": by_category,
        "total_tags": len(all_tags),
        "tags": sorted(all_tags),
        "sources": sorted(source_names),
        "files": [c.filepath for c in concepts],
    }
