import pytest
from app.okf.formatter import format_okf_string
from app.okf.parser import parse_okf_string
from app.ingestion.pipeline import _process_crawled_html

# --- Test OKF Core Logic ---
# These tests ensure that our custom OKF formatting never corrupts data 
# and can safely transition between Dictionary/YAML/Markdown states.

def test_okf_formatter_creates_valid_string():
    """Tests if the formatter correctly weaves metadata and markdown."""
    sample_text = "This is a test OKF document regarding Kubernetes."
    sample_metadata = {
        "title": "K8s Test Doc",
        "topics": ["kubernetes", "testing"],
        "trust_level": "High"
    }
    
    result = format_okf_string(text=sample_text, metadata=sample_metadata)
    
    # Assert formatting structure
    assert result.startswith("---")
    assert "title: K8s Test Doc" in result
    assert "topics:\n- kubernetes" in result
    assert "trust_level: High" in result
    assert "This is a test OKF document" in result

def test_okf_parser_extracts_data_correctly():
    """Tests if the parser accurately separates YAML frontmatter from the body."""
    valid_okf_string = """---
title: Extracted Title
document_type: Architecture
---

# Architecture Overview
This is the body of the markdown."""

    metadata, body = parse_okf_string(valid_okf_string)
    
    # Assert extraction accuracy
    assert isinstance(metadata, dict)
    assert metadata.get("title") == "Extracted Title"
    assert metadata.get("document_type") == "Architecture"
    assert "# Architecture Overview" in body

def test_okf_parser_handles_missing_frontmatter():
    """Tests the fallback mechanism if a document lacks YAML."""
    invalid_okf_string = "# Just Markdown\nNo frontmatter here."
    
    metadata, body = parse_okf_string(invalid_okf_string)
    
    # Should safely return empty dict and unmodified text
    assert metadata == {}
    assert body == invalid_okf_string


# ---------------------------------------------------------------------------
# _process_crawled_html source-name filtering
# ---------------------------------------------------------------------------

def _make_page(source_name, url, raw_path):
    return {"source_name": source_name, "url": url, "raw_path": raw_path}


def _write_raw_html(tmp_path, source_name, page_id, body):
    import os

    source_dir = tmp_path / "cache" / source_name
    source_dir.mkdir(parents=True, exist_ok=True)
    html_path = source_dir / f"{page_id}.html"
    html_path.write_text(f"<html><body><h1>{body}</h1></body></html>", encoding="utf-8")
    return str(html_path)


def test_process_crawled_html_filters_by_source_names(tmp_path, monkeypatch):
    """Only pages belonging to the selected sources are processed."""
    kube_page = _make_page(
        "kubernetes", "https://kubernetes.io/docs/concepts/a",
        _write_raw_html(tmp_path, "kubernetes", "a", "Kube concept"),
    )
    lang_page = _make_page(
        "langchain", "https://python.langchain.com/docs/b",
        _write_raw_html(tmp_path, "langchain", "b", "Langchain concept"),
    )

    processed_urls = []

    monkeypatch.setattr("app.ingestion.pipeline.clean_html", lambda html, base_url=None: html)
    monkeypatch.setattr(
        "app.ingestion.pipeline.html_to_markdown",
        lambda cleaned: "# Converted Markdown",
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.split_into_concepts",
        lambda markdown, category, source_name, source_url: [
            (f"concept-{source_name}", "Concept", markdown)
        ],
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.delete_concepts_by_source_urls",
        lambda urls, knowledge_dir: None,
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.write_concept_file",
        lambda knowledge_dir, category, concept_id, content: processed_urls.append(
            (category, concept_id)
        ),
    )

    processed = _process_crawled_html(
        cache_dir=str(tmp_path / "cache"),
        knowledge_dir=str(tmp_path / "knowledge"),
        changed_pages=[kube_page, lang_page],
        source_names=["kubernetes"],
    )

    assert processed == 1
    assert processed_urls == [("kubernetes", "concept-kubernetes")]


def test_process_crawled_html_empty_source_names_skips_all(tmp_path, monkeypatch):
    """An empty source list means no crawled pages are processed."""
    page = _make_page(
        "kubernetes", "https://kubernetes.io/docs/concepts/a",
        _write_raw_html(tmp_path, "kubernetes", "a", "Kube concept"),
    )

    processed_urls = []

    monkeypatch.setattr("app.ingestion.pipeline.clean_html", lambda html, base_url=None: html)
    monkeypatch.setattr(
        "app.ingestion.pipeline.html_to_markdown",
        lambda cleaned: "# Converted Markdown",
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.split_into_concepts",
        lambda markdown, category, source_name, source_url: [("c", "T", markdown)],
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.write_concept_file",
        lambda knowledge_dir, category, concept_id, content: processed_urls.append(
            (category, concept_id)
        ),
    )

    processed = _process_crawled_html(
        cache_dir=str(tmp_path / "cache"),
        knowledge_dir=str(tmp_path / "knowledge"),
        changed_pages=[page],
        source_names=[],
    )

    assert processed == 0
    assert processed_urls == []


def test_process_crawled_html_explicit_source_ignores_cached_pages(tmp_path, monkeypatch):
    """Explicit source selection must NOT fall back to cached pages from earlier runs."""
    # The cache dir has a crawler state file for kubernetes pages that are NOT
    # part of changed_pages. They must be ignored because the user asked for a
    # fresh crawl of a specific source.
    import json
    import os

    state_dir = tmp_path / "cache" / ".state"
    state_dir.mkdir(parents=True, exist_ok=True)
    cached_page = _make_page(
        "kubernetes", "https://kubernetes.io/docs/concepts/cached",
        _write_raw_html(tmp_path, "kubernetes", "cached", "Old cached page"),
    )
    (state_dir / "kubernetes.json").write_text(
        json.dumps(
            {
                "source": "kubernetes",
                "pages": {
                    cached_page["url"]: {"raw_file": os.path.relpath(cached_page["raw_path"], str(tmp_path / "cache"))},
                },
            }
        ),
        encoding="utf-8",
    )

    fresh_page = _make_page(
        "kubernetes", "https://kubernetes.io/docs/concepts/fresh",
        _write_raw_html(tmp_path, "kubernetes", "fresh", "Fresh page"),
    )

    processed_urls = []

    monkeypatch.setattr("app.ingestion.pipeline.clean_html", lambda html, base_url=None: html)
    monkeypatch.setattr(
        "app.ingestion.pipeline.html_to_markdown",
        lambda cleaned: "# Converted Markdown",
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.split_into_concepts",
        lambda markdown, category, source_name, source_url: [
            (f"concept-{source_name}", "Concept", markdown)
        ],
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.write_concept_file",
        lambda knowledge_dir, category, concept_id, content: processed_urls.append(
            (category, concept_id)
        ),
    )
    monkeypatch.setattr(
        "app.ingestion.pipeline.delete_concepts_by_source_urls",
        lambda urls, knowledge_dir: None,
    )

    processed = _process_crawled_html(
        cache_dir=str(tmp_path / "cache"),
        knowledge_dir=str(tmp_path / "knowledge"),
        changed_pages=[fresh_page],
        source_names=["kubernetes"],
    )

    # Only the freshly downloaded page is processed; the cached page is ignored.
    assert processed == 1
    assert processed_urls == [("kubernetes", "concept-kubernetes")]