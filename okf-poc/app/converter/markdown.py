"""
HTML -> OKF Markdown conversion (Phase 4).

Uses `markdownify` to turn cleaned documentation HTML into Markdown, then splits
the result into individual concept files, each with OKF YAML frontmatter, stored
under `knowledge/<category>/<concept>.md`.

Concept extraction strategy:
  - Default: heading-based splitting (robust, dependency-free). Every H2/H3 section
    that is long enough becomes its own concept.
  - Future enhancement (see config): semantic splitting via LlamaIndex
    SemanticSplitterNodeParser (needs `llama-index-node-parser-semantic` and an LLM
    API key) is signposted in `split_into_concepts`.
"""

import os
import re
import uuid
from datetime import date
from typing import List, Optional, Tuple

import markdownify

from app.core.config import settings
from app.okf.formatter import format_okf_string

HEADING_RE = re.compile(r"^(#{2,3})\s+(.*)$", re.MULTILINE)


def html_to_markdown(clean_html: str) -> str:
    """
    Convert cleaned documentation HTML to GitHub-flavored Markdown.
    Tables, code blocks, lists and admonitions are preserved.
    """
    return markdownify.markdownify(clean_html, heading_style="ATX", bullets="-")


# ---------------------------------------------------------------------------
# Heading-based concept splitting
# ---------------------------------------------------------------------------

def _split_headings(markdown: str, min_chars: int, max_chars: int) -> List[str]:
    """
    Split Markdown into sections at H2/H3 boundaries. Content before the first
    heading becomes its own section. Sections shorter than min_chars are merged
    into the previous section so tiny fragments do not become empty concepts.
    Sections longer than max_chars are truncated to keep concept files manageable.
    """
    matches = list(HEADING_RE.finditer(markdown))
    sections: List[str] = []

    # Content before the first heading (page intro) becomes its own section.
    if matches and matches[0].start() > 0:
        preamble = markdown[: matches[0].start()].strip()
        if preamble:
            sections.append(preamble)

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        section = markdown[start:end].strip()
        if section:
            sections.append(section)

    # No headings at all -> the whole page is one concept (if long enough).
    if not sections and markdown.strip():
        sections = [markdown.strip()]

    merged: List[str] = []
    for section in sections:
        if merged and len(section) < min_chars:
            merged[-1] = f"{merged[-1]}\n\n{section}"
        else:
            merged.append(section)

    return [s[:max_chars] for s in merged]


def _slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    return slug[:60] or "concept"


# ---------------------------------------------------------------------------
# Concept file generation
# ---------------------------------------------------------------------------

def _section_description(body: str) -> str:
    """First meaningful (non-heading) line of the body for the frontmatter."""
    for line in body.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped[:200]
    return ""


def generate_concept_file(
    *,
    title: str,
    body: str,
    category: str,
    source_name: str,
    source_url: str,
    tags: Optional[List[str]] = None,
    concept_id: Optional[str] = None,
) -> str:
    """
    Serialize a single concept into an OKF Markdown file (YAML frontmatter + body).
    `concept_id` defaults to a slugified version of the title.

    Serialization is delegated to `app.okf.formatter.format_okf_string` so the
    whole project writes OKF documents through one canonical code path.
    """
    today = date.today().isoformat()
    cid = concept_id or f"{_slugify(category)}-{_slugify(title)}"
    if not cid:
        cid = uuid.uuid4().hex[:10]

    frontmatter = {
        "id": cid,
        "type": "concept",
        "title": title,
        "description": _section_description(body),
        "category": category,
        "tags": tags or [],
        "source": {"name": source_name, "url": source_url},
        "updated_at": today,
        "created_at": today,
    }

    return format_okf_string(body.strip(), frontmatter)


def split_into_concepts(
    markdown: str,
    category: str,
    source_name: str,
    source_url: str,
    min_chars: Optional[int] = None,
    max_chars: Optional[int] = None,
) -> List[Tuple[str, str, str]]:
    """
    Split a converted Markdown page into OKF concept files.

    Returns a list of (concept_id, title, full_file_content) tuples.

    NOTE (future enhancement): replace the heading-based splitter with a semantic
    splitter, e.g. LlamaIndex `SemanticSplitterNodeParser`:
        from llama_index.core.node_parser import SemanticSplitterNodeParser
        splitter = SemanticSplitterNodeParser.from_defaults(service_context=...)
    This requires `llama-index-node-parser-semantic` and an LLM API key. The
    heading-based splitter below is the deterministic fallback.
    """
    min_chars = min_chars or settings.CONCEPT_MIN_CHARS
    max_chars = max_chars or settings.CONCEPT_MAX_CHARS
    sections = _split_headings(markdown, min_chars, max_chars)

    concepts: List[Tuple[str, str, str]] = []
    for section in sections:
        title = _section_title(section)
        concept_id = _slugify(f"{category}-{title}")
        body = section
        content = generate_concept_file(
            title=title, body=body, category=category,
            source_name=source_name, source_url=source_url,
            concept_id=concept_id,
        )
        concepts.append((concept_id, title, content))
    return concepts


def _section_title(section: str) -> str:
    """First heading in the section, or a truncated prefix of the first line."""
    m = HEADING_RE.match(section)
    if m:
        return m.group(2).strip()
    first_line = section.strip().splitlines()[0] if section.strip() else "concept"
    return re.sub(r"^#+\s*", "", first_line)[:80]


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def write_concept_file(knowledge_dir: str, category: str, concept_id: str, content: str) -> str:
    """
    Write a concept file to `knowledge_dir/<category>/<concept_id>.md`,
    creating the category folder if needed. Returns the written path.
    """
    category_dir = os.path.join(knowledge_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    path = os.path.join(category_dir, f"{concept_id}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
