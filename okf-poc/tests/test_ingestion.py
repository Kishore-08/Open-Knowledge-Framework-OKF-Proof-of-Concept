import pytest
from app.okf.formatter import format_okf_string
from app.okf.parser import parse_okf_string

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