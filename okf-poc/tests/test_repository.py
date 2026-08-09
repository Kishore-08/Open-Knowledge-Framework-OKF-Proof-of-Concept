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
    # The checked-in `knowledge/` directory now contains the full ingested
    # corpus (kubernetes/tutorial/reference + the original linux/apache/
    # langchain concepts) restored from the previously-orphaned
    # `data/knowledge/` path - see ISSUE_RESOLUTION_2.md §1. This is just a
    # sanity floor, not an exact count, since the corpus grows as ingestion
    # runs.
    assert len(repo) >= 6
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


# ---------------------------------------------------------------------------
# NOTE: the tests below intentionally do NOT depend on the real, checked-in
# `knowledge/` corpus (unlike `repo` above). That corpus is real ingested
# content (600+ Kubernetes docs) that changes shape whenever the pipeline is
# re-run, so asserting on specific IDs/tags within it (e.g. a hardcoded
# "k8s-deployment" concept or a "networking" tag) is brittle and was in fact
# broken: those exact seed concepts never shipped in this repository, so
# these tests failed unconditionally before this fix. Each test below builds
# its own tiny, deterministic fixture repository under tmp_path instead,
# using the same `format_and_save_okf` round-trip as
# `test_pipeline_written_okf_roundtrips_through_repository` below.
# ---------------------------------------------------------------------------

def _write_concept(output_dir, filename, **overrides) -> None:
    metadata = {
        "id": "k8s-deployment",
        "type": "concept",
        "title": "Kubernetes Deployment",
        "description": "Declarative controller for managing Pods.",
        "category": "kubernetes",
        "tags": ["networking"],
        "source": {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"},
        "created_at": "2026-08-05",
        "updated_at": "2026-08-05",
        "aliases": ["Deployment", "K8s Deployment"],
        "related": [],
    }
    metadata.update(overrides)
    format_and_save_okf(
        text=f"# {metadata['title']}\nBody text for {metadata['id']}.",
        metadata=metadata,
        output_dir=str(output_dir),
        filename=filename,
    )


def test_get_concept_by_id_and_alias(tmp_path):
    _write_concept(tmp_path, "k8s-deployment.md")

    by_id = get_concept("k8s-deployment", knowledge_dir=str(tmp_path))
    assert by_id is not None
    assert by_id.metadata.title == "Kubernetes Deployment"

    by_alias = get_concept("Deployment", knowledge_dir=str(tmp_path))  # alias lookup
    assert by_alias is not None
    assert by_alias.metadata.id == "k8s-deployment"

    assert get_concept("does-not-exist", knowledge_dir=str(tmp_path)) is None


def test_get_concept_dict_serializable(tmp_path):
    _write_concept(
        tmp_path, "k8s-service.md",
        id="k8s-service", title="Kubernetes Service",
        source={"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/concepts/services-networking/service/"},
    )

    d = get_concept_dict("k8s-service", knowledge_dir=str(tmp_path))
    assert d is not None
    assert d["source"]["url"].startswith("https://")
    assert "content" in d


def test_search_concepts_ranking(tmp_path):
    _write_concept(tmp_path, "k8s-deployment.md")
    _write_concept(
        tmp_path, "k8s-pod.md",
        id="k8s-pod", title="Kubernetes Pod", tags=["workload"],
        source={"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/concepts/workloads/pods/"},
    )

    results = search_concepts("scale a deployment", knowledge_dir=str(tmp_path))
    assert results, "expected at least one hit"
    top = results[0]
    assert top["category"] == "kubernetes"
    assert top["id"] == "k8s-deployment"


def test_search_concepts_score_is_normalized(tmp_path):
    # Regression test: keyword scores used to be an unbounded sum of weighted
    # token-hit counts (observed values of 27.0 and 135.0 in production for
    # the same query), while semantic search reports 0.0-1.0 cosine
    # similarity and both get merged into one list exposed via the API's
    # `Citation.score` field, documented as "0.0 to 1.0". search_concepts()
    # must now return scores in that same range so the two are comparable
    # and the API contract holds regardless of which path answered.
    _write_concept(tmp_path, "k8s-deployment.md")
    _write_concept(
        tmp_path, "k8s-pod.md",
        id="k8s-pod", title="Kubernetes Pod", tags=["workload"],
        source={"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/concepts/workloads/pods/"},
    )

    results = search_concepts("kubernetes deployment pod", knowledge_dir=str(tmp_path))
    assert results
    for r in results:
        assert 0.0 <= r["score"] < 1.0

    # A definition-style query triggers the strongest boosts (up to 15x) -
    # this is exactly the case that used to produce scores like 135.0.
    boosted = search_concepts("what is a deployment", knowledge_dir=str(tmp_path))
    assert boosted
    for r in boosted:
        assert 0.0 <= r["score"] < 1.0


def test_search_tag_filter(tmp_path):
    _write_concept(tmp_path, "k8s-deployment.md")  # tagged "networking"
    _write_concept(
        tmp_path, "k8s-pod.md",
        id="k8s-pod", title="Kubernetes Pod", tags=["workload"],
        source={"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/concepts/workloads/pods/"},
    )

    results = search_concepts("", tag="networking", knowledge_dir=str(tmp_path))
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