import pytest

from app.okf.formatter import format_and_save_okf
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
    assert len(k8s) >= 3  # seed base has 3; ingested docs may add more


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
    # The top hit should be a kubernetes concept whose title/content is about
    # deployments/scaling — not tied to a specific fixed set of IDs, since the
    # real ingested knowledge base (600+ kubernetes docs) can contain a more
    # specific match than the 3 small seed concepts.
    top = results[0]
    assert top["category"] == "kubernetes"
    assert "deploy" in top["id"] or "scal" in top["id"] or top["id"] in (
        "k8s-deployment", "k8s-service", "k8s-pod"
    )


def test_search_tag_filter(repo):
    results = search_concepts("", tag="networking")
    assert results
    assert all("networking" in c.get("tags", []) for c in results)


def test_knowledge_stats(repo):
    stats = knowledge_stats()
    assert stats["total_concepts"] == len(repo)
    assert "kubernetes" in stats["categories"]
    assert stats["total_tags"] > 0


def test_pipeline_written_okf_roundtrips_through_repository(tmp_path):
    # Regression test for the ingestion drift fix: the pipeline now indexes by
    # re-reading the OKF files it wrote (load_all_concepts), instead of indexing
    # in-memory Documents. This proves files saved via format_and_save_okf with
    # the pipeline's extra frontmatter keys survive re-validation and load.
    okf_dir = tmp_path / "source_1"
    metadata = {
        "id": "reference-ingested-drift",
        "type": "concept",
        "title": "Ingested Drift Concept",
        "description": "Round-trip test for pipeline-written files.",
        "category": "reference",
        "tags": ["test"],
        "source": {"name": "pipeline", "url": "https://example.com/drift"},
        "created_at": "2026-08-06",
        "updated_at": "2026-08-06",
        "aliases": [],
        "related": [],
        "document_type": "Concept",
        "trust_level": "High",
        "source_file": "drift.txt",
    }
    format_and_save_okf(
        text="# Ingested Drift\nBody text for the drift concept.",
        metadata=metadata,
        output_dir=str(okf_dir),
        filename="reference-ingested-drift_0.md",
    )

    # use_cache=False mirrors the pipeline (which must re-read freshly written files)
    concepts = load_all_concepts(str(okf_dir), use_cache=False)
    assert len(concepts) == 1
    assert concepts[0].metadata.id == "reference-ingested-drift"
    assert concepts[0].metadata.category == "reference"
    assert "Body text for the drift concept" in concepts[0].content