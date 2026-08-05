"""
OKF concept frontmatter schema.

Every knowledge concept is a Markdown file whose YAML frontmatter conforms to this
schema. The repository, indexer and search layer all depend on it, so metadata stays
consistent across the knowledge base (Phase 5 of the OKF platform).

Example frontmatter:
    ---
    id: k8s-deployment
    type: concept
    title: Kubernetes Deployment
    description: Declarative controller for managing Pods
    category: kubernetes
    tags: [deployment, workload, controller]
    source:
      name: Kubernetes Documentation
      url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    updated_at: 2026-08-05
    created_at: 2026-08-05
    aliases: [Deployment, K8s Deployment]
    related: [k8s-replicaset, k8s-pod]
    ---
"""

from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

class ConceptSource(BaseModel):
    """Provenance of a concept (official documentation by default)."""

    name: str = Field(description="Name of the source documentation.")
    url: str = Field(description="Official URL of the source page.")


class OKFConcept(BaseModel):
    """Validated YAML frontmatter for a single OKF concept file."""

    id: str = Field(description="Unique, stable identifier (slug).", pattern=r"^[a-zA-Z0-9][a-zA-Z0-9-_]*$")
    type: str = Field(default="concept", description="Concept type (concept, tutorial, reference...).")
    title: str = Field(description="Human readable title.")
    description: str = Field(default="", description="One-two sentence summary.")
    category: str = Field(description="Knowledge category, e.g. kubernetes.")
    tags: List[str] = Field(default_factory=list, description="Searchable tags.")
    source: Optional[ConceptSource] = Field(default=None, description="Official documentation source.")
    updated_at: str = Field(default="", description="ISO date the concept was last updated.")
    created_at: str = Field(default="", description="ISO date the concept was created.")
    aliases: List[str] = Field(default_factory=list, description="Alternative names for lookup.")
    related: List[str] = Field(default_factory=list, description="IDs of related concepts.")

    @field_validator("tags", "aliases", "related", mode="before")
    @classmethod
    def _coerce_lists(cls, v):
        if v is None:
            return []
        if isinstance(v, str):
            return [t.strip() for t in v.split(",") if t.strip()]
        return v

    @field_validator("updated_at", "created_at", mode="before")
    @classmethod
    def _coerce_dates(cls, v):
        if v is None:
            return ""
        if hasattr(v, "isoformat"):
            return v.isoformat()
        return v

    def metadata_payload(self) -> dict:
        """Flat metadata payload stored on every Qdrant point / document."""
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "tags": self.tags,
            "aliases": self.aliases,
            "related": self.related,
            "source_name": self.source.name if self.source else "",
            "source_url": self.source.url if self.source else "",
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class OKFConceptFile(BaseModel):
    """A loaded concept: validated frontmatter plus its Markdown body."""

    metadata: OKFConcept
    content: str = Field(description="Markdown body of the concept (without frontmatter).")
    filepath: str = Field(description="Absolute path to the concept file.")

    @property
    def full_text(self) -> str:
        return f"{self.metadata.title}\n\n{self.content}"
