import pytest

from app.converter.markdown import html_to_markdown, split_into_concepts, generate_concept_file


def test_html_to_markdown_preserves_tables_and_code():
    html = """
    <h2>Rules</h2>
    <table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>
    <pre><code>kubectl get pod</code></pre>
    """
    md = html_to_markdown(html)
    assert "| A" in md          # table header preserved
    assert "| 1" in md          # table row preserved
    assert "kubectl get pod" in md


def test_split_into_concepts_keeps_preamble():
    markdown = (
        "# Intro Page\n\nThis page explains the concept.\n\n"
        "## First Section\n\nLong content about section one.\n\n"
        "## Second Section\n\nLong content about section two."
    )
    concepts = split_into_concepts(
        markdown, category="test", source_name="Docs", source_url="https://example.com", min_chars=10
    )
    titles = [t for _, t, _ in concepts]
    # preamble (before first H2) is retained as its own concept
    assert "Intro Page" in titles
    assert "First Section" in titles
    assert "Second Section" in titles


def test_generate_concept_file_has_valid_frontmatter():
    content = generate_concept_file(
        title="Deployment",
        body="A Deployment manages Pods.",
        category="kubernetes",
        source_name="K8s Docs",
        source_url="https://kubernetes.io/docs",
    )
    assert content.startswith("---")
    assert "id: kubernetes-deployment" in content
    assert "category: kubernetes" in content
    assert "source:" in content
    assert "url: https://kubernetes.io/docs" in content
    assert "A Deployment manages Pods." in content


def test_split_into_concepts_truncates_overlong_sections():
    markdown = "## Huge Section\n\n" + "word " * 1000
    concepts = split_into_concepts(
        markdown, category="test", source_name="Docs", source_url="https://example.com",
        max_chars=200,
    )
    content = concepts[0][2]
    body = content.split("---\n", 2)[-1].strip()
    # the body (after frontmatter) must be capped at max_chars
    assert len(body) <= 200 + 20
