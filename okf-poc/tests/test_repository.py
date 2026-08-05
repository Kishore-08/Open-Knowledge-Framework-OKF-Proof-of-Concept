import pytest

from app.okf.schema import OKFConcept
from app.okf.repository import (
    load_all_concepts,
    list_categories,
    list_concepts,
    get_concept,
    get_concept_dict,
    search_concepts,
    knowledge_stats,
)


@pytest.fixture(scope="module")
def repo():
    # Uses the checked-in knowledge/ directory (source of truth for tests)
    concepts = load_all_concepts()
    assert concepts, "knowledge/ repo must contain at least one valid concept"
    return concepts


def test_repository_loads_valid_concepts(repo):
    assert len(repo) >= 6  # seed knowledge base: kubernetes(3) apache(1) linux(2) langchain(1)
    for concept in repo:
        assert concept.metadata.id
        assert concept.metadata.category
        assert concept.content


def test_categories_and_listing(repo):
    cats = list_categories()
    assert "kubernetes" in cats
    assert "linux" in cats

    k8s = list_concepts(category="kubernetes")
    assert all(c["category"] == "kubernetes" for c in k8s)
    assert len(k8s) == 3


def test_get_concept_by_id_and_alias(repo):
    by_id = get_concept("k8s-deployment")
    assert by_id is not None
    assert by_id.metadata.title == "Kubernetes Deployment"

    by_alias = get_concept("Deployment")  # alias lookup
    assert by_alias is not None
    assert by_alias.metadata.id == "k8s-deployment"

    assert get_concept("does-not-exist") is None


def test_get_concept_dict_serializable(repo):
    d = get_concept_dict("k8s-service")
    assert d is not None
    assert d["source"]["url"].startswith("https://")
    assert "content" in d


def test_search_concepts_ranking(repo):
    results = search_concepts("scale a deployment")
    assert results, "expected at least one hit"
    # deployment should rank highest for 'deployment'
    top = results[0]["id"]
    assert top in ("k8s-deployment", "k8s-service", "k8s-pod")


def test_search_tag_filter(repo):
    results = search_concepts("", tag="networking")
    assert results
    assert all("networking" in c.get("tags", []) for c in results)


def test_knowledge_stats(repo):
    stats = knowledge_stats()
    assert stats["total_concepts"] == len(repo)
    assert "kubernetes" in stats["categories"]
    assert stats["total_tags"] > 0
