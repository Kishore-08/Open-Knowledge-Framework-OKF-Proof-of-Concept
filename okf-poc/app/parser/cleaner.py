"""
Document cleaning (Phase 3).

Removes navigation, sidebars, footers, ads, scripts, styles, breadcrumbs, TOC and
edit buttons. Keeps headings, paragraphs, tables, code blocks, lists and
notes/warnings/admonitions so the resulting HTML converts cleanly to Markdown.
"""

from typing import Optional

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Selectors whose content is pure navigation / noise and must be removed.
REMOVE_SELECTORS = [
    "script",
    "style",
    "noscript",
    "iframe",
    "nav",
    "footer",
    "header",
    "aside",
    "form",
    "button",
    "svg",
    "canvas",
    "template",
    "adsbygoogle",
    "ins.adsbygoogle",
    ".ad",
    ".ads",
    ".advertisement",
    ".ad-container",
    ".breadcrumbs",
    ".breadcrumb",
    ".toc",
    ".table-of-contents",
    ".sidebar",
    ".side-bar",
    ".menu",
    ".navigation",
    ".navbar",
    ".top-nav",
    ".header-wrapper",
    ".footer",
    ".footer-wrapper",
    ".social-share",
    ".share",
    ".edit-page",
    ".edit-this-page",
    ".github-edit",
    ".search-box",
    ".search-form",
    ".skip-link",
    ".alert-cookie",
    ".cookie-banner",
    ".feedback",
    ".page-links",
    ".pagination",
    ".next-prev",
    "[aria-hidden='true']",
    "[role='navigation']",
    "[class*='cookie']",
]

# Blocks that should be *kept* even though generic heuristics might drop them.
KEEP_CONTAINERS = [
    "main",
    "article",
    ".main-content",
    ".doc-content",
    ".md-content",
    ".content",
    ".markdown-body",
    ".document",
    "[role='main']",
]

# Note / warning blocks are kept (they carry documentation meaning).
NOTE_SELECTORS = [
    "blockquote",
    ".note",
    ".admonition",
    ".warning",
    ".important",
    ".tip",
    ".caution",
    ".danger",
    ".callout",
    ".info",
    ".alert",
]


def extract_main_content(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Pick the main content container if the page defines one, else the body."""
    for selector in KEEP_CONTAINERS:
        node = soup.select_one(selector)
        if node:
            return node
    return soup.body or soup


def clean_html(html: str, base_url: Optional[str] = None) -> str:
    """
    Strip navigation/noise from a documentation HTML page and return clean HTML
    containing only semantic content. Relative links are resolved against base_url.
    """
    soup = BeautifulSoup(html, "lxml")

    # 1. Remove pure noise elements.
    for selector in REMOVE_SELECTORS:
        for node in soup.select(selector):
            node.decompose()

    # 2. Keep only the main content region.
    main = extract_main_content(soup)
    if main is not None and main is not soup:
        soup = BeautifulSoup(str(main), "lxml")

    # 3. Resolve relative links / images to absolute URLs so the markdown keeps
    #    working links and the provenance stays traceable.
    if base_url:
        for tag, attr in (("a", "href"), ("img", "src")):
            for node in soup.find_all(tag):
                value = node.get(attr)
                if value:
                    node[attr] = urljoin(base_url, value)

    # 4. Drop empty headings and empty paragraphs left over from cleanup.
    for node in soup.find_all(["h1", "h2", "h3", "h4", "h5", "p", "div"]):
        if not node.get_text(strip=True):
            node.decompose()

    return str(soup)


def extract_title(soup: BeautifulSoup, base_url: Optional[str] = None) -> str:
    """Best-effort title extraction for a cleaned page."""
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    title = soup.find("title")
    if title and title.get_text(strip=True):
        return title.get_text(strip=True)
    return ""
