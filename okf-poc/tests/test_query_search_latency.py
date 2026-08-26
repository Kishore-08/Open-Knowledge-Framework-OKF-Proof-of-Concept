import importlib
import threading


search_module = importlib.import_module("app.query.search")


def test_auto_search_runs_keyword_and_semantic_retrieval_concurrently(monkeypatch):
    keyword_started = threading.Event()
    semantic_started = threading.Event()

    def keyword_search(*args, **kwargs):
        keyword_started.set()
        assert semantic_started.wait(timeout=1), "semantic search did not start concurrently"
        return []

    def semantic_search(*args, **kwargs):
        semantic_started.set()
        assert keyword_started.wait(timeout=1), "keyword search did not start concurrently"
        return []

    monkeypatch.setattr(search_module, "search_concepts", keyword_search)
    monkeypatch.setattr(search_module, "_semantic_search", semantic_search)

    result = search_module.search("pod networking", mode="auto")

    assert result == {"mode": "keyword", "results": []}


def test_keyword_mode_does_not_start_semantic_retrieval(monkeypatch):
    monkeypatch.setattr(search_module, "search_concepts", lambda *args, **kwargs: [])
    monkeypatch.setattr(
        search_module,
        "_semantic_search",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("keyword mode should not start semantic retrieval")
        ),
    )

    assert search_module.search("pod", mode="keyword") == {
        "mode": "keyword",
        "results": [],
    }
