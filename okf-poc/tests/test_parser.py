import pytest

from app.parser.cleaner import clean_html, extract_title


def test_clean_html_removes_navigation_and_footer():
    html = """
    <html><head><title>Docs</title></head>
    <body>
        <nav><a href="/">Home</a></nav>
        <div class="sidebar">nav junk</div>
        <article>
            <h1>Real Content</h1>
            <p>Actual documentation body.</p>
        </article>
        <footer>copyright 2026</footer>
    </body></html>
    """
    cleaned = clean_html(html)
    assert "<nav>" not in cleaned
    assert "sidebar" not in cleaned
    assert "<footer>" not in cleaned
    assert "Real Content" in cleaned
    assert "Actual documentation body." in cleaned


def test_clean_html_resolves_relative_links():
    html = '<a href="/docs/page">link</a><p>body</p>'
    cleaned = clean_html(html, base_url="https://example.com")
    assert 'href="https://example.com/docs/page"' in cleaned


def test_extract_title_from_h1():
    html = "<html><head><title>Fallback</title></head><body><h1>Primary Title</h1></body></html>"
    from bs4 import BeautifulSoup

    assert extract_title(BeautifulSoup(html, "lxml")) == "Primary Title"
