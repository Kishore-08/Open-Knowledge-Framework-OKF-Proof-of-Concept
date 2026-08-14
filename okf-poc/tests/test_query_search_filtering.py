from app.query.search import _is_internal_job_record, _rank_and_filter


def test_internal_ingestion_status_is_not_citable():
    result = {
        "id": "936d182c9cf6",
        "title": "Qdrant Knowledge Ingestion Job Status",
        "snippet": '{"progress_percent": 95, "stage_message": "Indexing", '
        '"indexed_documents": 386, "rate_limit_hits": 0}',
        "score": 0.608,
    }
    assert _is_internal_job_record(result)
    assert _rank_and_filter([result], 5) == []


def test_results_are_relevant_sorted_deduplicated_and_limited(monkeypatch):
    monkeypatch.setattr("app.query.search.settings.CITATION_MIN_SCORE", 0.35)
    monkeypatch.setattr("app.query.search.settings.CITATION_RELATIVE_SCORE", 0.75)
    results = [
        {"id": "weak", "title": "Weak", "score": 0.40},
        {"id": "best", "title": "Best", "score": 0.90},
        {"id": "second", "title": "Second", "score": 0.72},
        {"id": "second", "title": "Second duplicate", "score": 0.60},
    ]
    filtered = _rank_and_filter(results, 5)
    assert [item["id"] for item in filtered] == ["best", "second"]


def test_never_returns_more_than_five_citations(monkeypatch):
    monkeypatch.setattr("app.query.search.settings.CITATION_MIN_SCORE", 0.0)
    monkeypatch.setattr("app.query.search.settings.CITATION_RELATIVE_SCORE", 0.0)
    results = [{"id": str(i), "title": str(i), "score": 1 - i / 100} for i in range(10)]
    assert len(_rank_and_filter(results, 20)) == 5
