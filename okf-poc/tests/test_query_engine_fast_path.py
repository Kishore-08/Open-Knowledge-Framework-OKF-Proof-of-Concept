from app.query import engine


def test_service_types_use_complete_curated_fast_path(monkeypatch):
    def unexpected_search(*args, **kwargs):
        raise AssertionError("exact curated match should not call semantic search")

    monkeypatch.setattr(engine, "search", unexpected_search)
    monkeypatch.setattr(engine, "_call_llm", lambda query, context: context)

    result = engine.generate_answer(
        "What are the different types of services in Kubernetes?"
    )

    assert result.retrieval_mode == "curated"
    assert len(result.sources) == 1
    for service_type in ("ClusterIP", "NodePort", "LoadBalancer", "ExternalName"):
        assert service_type in result.answer


def test_misspelled_linux_os_question_uses_distribution_grounding(monkeypatch):
    monkeypatch.setattr(
        engine,
        "search",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("curated Linux match should not call semantic search")
        ),
    )
    monkeypatch.setattr(engine, "_call_llm", lambda query, context: context)

    result = engine.generate_answer("what are the differnt types of linux OS ?")

    assert result.retrieval_mode == "curated"
    assert len(result.sources) == 1
    for distribution in ("Ubuntu", "Debian", "Fedora", "Arch Linux"):
        assert distribution in result.answer


def test_ambiguous_python_package_taxonomy_does_not_cite_app_example(monkeypatch):
    monkeypatch.setattr(
        engine,
        "search",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("ambiguous taxonomy should not retrieve examples")
        ),
    )

    result = engine.generate_answer("what are different types of python packages")

    assert result.retrieval_mode == "clarification"
    assert result.sources == []
    assert "does not contain an authoritative classification" in result.answer
