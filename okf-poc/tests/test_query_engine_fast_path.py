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


def test_llm_failure_returns_keyword_content_without_raw_provider_error(monkeypatch):
    monkeypatch.setattr(
        engine,
        "search",
        lambda *args, **kwargs: {
            "mode": "keyword",
            "results": [{
                "id": "pod",
                "title": "What is a Pod?",
                "description": "A Pod is the smallest deployable Kubernetes object.",
                "source_url": "https://kubernetes.io/docs/concepts/workloads/pods/",
                "score": 0.9,
            }],
        },
    )
    monkeypatch.setattr(engine, "get_concept_dict", lambda concept_id: None)
    monkeypatch.setattr(
        engine,
        "_call_llm",
        lambda *args: (_ for _ in ()).throw(Exception("401 secret provider detail")),
    )

    result = engine.generate_answer("what is a pod")

    assert result.retrieval_mode == "keyword"
    assert "smallest deployable Kubernetes object" in result.answer
    assert "secret provider detail" not in result.answer
    assert len(result.sources) == 1


def test_llm_failure_uses_only_best_definition_and_citation(monkeypatch):
    monkeypatch.setattr(
        engine,
        "search",
        lambda *args, **kwargs: {
            "mode": "keyword",
            "results": [
                {
                    "id": "overview",
                    "title": "Overview",
                    "snippet": "# Overview\n\nKubernetes is a portable, extensible, open source platform for managing containerized workloads and services.",
                    "score": 0.95,
                },
                {
                    "id": "pod",
                    "title": "What is a Pod?",
                    "snippet": "A Pod is a group of one or more containers.",
                    "score": 0.80,
                },
            ],
        },
    )
    monkeypatch.setattr(engine, "get_concept_dict", lambda concept_id: None)
    monkeypatch.setattr(engine, "_call_llm", lambda *args: (_ for _ in ()).throw(Exception("401")))

    result = engine.generate_answer("what is kubernetes")

    assert result.answer.startswith("Kubernetes is a portable, extensible")
    assert "Pod is" not in result.answer
    assert [source["id"] for source in result.sources] == ["overview"]
