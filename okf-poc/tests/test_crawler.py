"""
Tests for app.ingestion.crawler.DocsCrawler.crawl_source.

The previous version of this file was not a test at all: it was a sequence
of bare module-level `assert` statements referencing an undefined `result`
variable, which raised a NameError during test *collection* and silently
aborted the entire `pytest` run (no test in the whole `tests/` package was
ever executed). This rewrite exercises `crawl_source`'s new/changed/
unchanged/deleted bookkeeping against a mocked HTTP layer, so it runs fully
offline and deterministically.
"""

import pytest

from app.ingestion.crawler import DocsCrawler


SOURCE = "example-docs"
URL = "https://example.com/page"


def _patch_fetch(monkeypatch, responses):
    """
    Replace DocsCrawler._fetch_with_metadata with a stub that returns the
    next queued response for a URL, so no real network call is made.
    """
    async def fake_fetch(self, url, headers=None):
        return responses[url].pop(0)

    monkeypatch.setattr(DocsCrawler, "_fetch_with_metadata", fake_fetch)


def _page(content: bytes, status_code: int = 200):
    return {
        "status_code": status_code,
        "content": content,
        "etag": None,
        "last_modified": None,
    }


@pytest.mark.asyncio
async def test_new_page_is_recorded_as_changed(tmp_path, monkeypatch):
    _patch_fetch(monkeypatch, {URL: [_page(b"<html>hello</html>")]})
    crawler = DocsCrawler(delay=0.0)

    result = await crawler.crawl_source(SOURCE, [URL], str(tmp_path))

    assert result.changed == 1
    assert result.changed_urls == [URL]
    assert result.unchanged == 0
    assert result.failed == 0


@pytest.mark.asyncio
async def test_unchanged_content_is_not_recounted(tmp_path, monkeypatch):
    # First crawl: new page.
    _patch_fetch(monkeypatch, {URL: [_page(b"<html>same</html>")]})
    crawler = DocsCrawler(delay=0.0)
    first = await crawler.crawl_source(SOURCE, [URL], str(tmp_path))
    assert first.changed == 1

    # Second crawl: identical content hash -> should be counted as unchanged,
    # not changed again.
    _patch_fetch(monkeypatch, {URL: [_page(b"<html>same</html>")]})
    second = await crawler.crawl_source(SOURCE, [URL], str(tmp_path))
    assert second.changed == 0
    assert second.unchanged == 1


@pytest.mark.asyncio
async def test_changed_content_is_detected(tmp_path, monkeypatch):
    _patch_fetch(monkeypatch, {URL: [_page(b"<html>v1</html>")]})
    crawler = DocsCrawler(delay=0.0)
    await crawler.crawl_source(SOURCE, [URL], str(tmp_path))

    _patch_fetch(monkeypatch, {URL: [_page(b"<html>v2</html>")]})
    second = await crawler.crawl_source(SOURCE, [URL], str(tmp_path))

    assert second.changed == 1
    assert URL in second.changed_urls


@pytest.mark.asyncio
async def test_url_missing_from_next_crawl_is_marked_deleted(tmp_path, monkeypatch):
    url_a = "https://example.com/page-a"
    url_b = "https://example.com/page-b"

    # First crawl discovers both pages.
    _patch_fetch(monkeypatch, {
        url_a: [_page(b"<html>a</html>")],
        url_b: [_page(b"<html>b</html>")],
    })
    crawler = DocsCrawler(delay=0.0)
    await crawler.crawl_source(SOURCE, [url_a, url_b], str(tmp_path))

    # Second crawl only discovers page-a; page-b is no longer in the sitemap.
    _patch_fetch(monkeypatch, {url_a: [_page(b"<html>a</html>")]})
    result = await crawler.crawl_source(SOURCE, [url_a], str(tmp_path))

    assert result.deleted == 1
    assert result.deleted_urls == [url_b]


@pytest.mark.asyncio
async def test_fetch_failure_is_recorded_without_crashing(tmp_path, monkeypatch):
    async def failing_fetch(self, url, headers=None):
        raise RuntimeError("connection reset")

    monkeypatch.setattr(DocsCrawler, "_fetch_with_metadata", failing_fetch)
    crawler = DocsCrawler(delay=0.0)

    result = await crawler.crawl_source(SOURCE, [URL], str(tmp_path))

    assert result.failed == 1
    assert result.changed == 0
    assert any(URL in err for err in result.errors)
