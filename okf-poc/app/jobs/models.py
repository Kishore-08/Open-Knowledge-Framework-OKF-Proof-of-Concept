"""
Ingestion job model.

A `Job` represents one long-running pipeline run (ingest, upload-and-ingest, ...).
It carries its own progress counters, lifecycle timestamps, and a cancellation
event so a run can be tracked, persisted, and aborted independently of any HTTP
request or FastAPI event loop.

The progress fields deliberately mirror the legacy `app.ingestion.status` dict so
the existing UI endpoints (`/api/v1/ingest/status`) keep working unchanged while
the new `/api/v1/jobs` endpoints expose the full job history.
"""

import threading
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

# Lifecycle statuses
STATUS_QUEUED = "queued"
STATUS_RUNNING = "running"
STATUS_CANCELLING = "cancelling"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"
STATUS_CANCELLED = "cancelled"

ACTIVE_STATUSES = {STATUS_QUEUED, STATUS_RUNNING, STATUS_CANCELLING}

TERMINAL_STATUSES = {STATUS_COMPLETED, STATUS_FAILED, STATUS_CANCELLED}


@dataclass
class Job:
    """A single ingestion job with progress + lifecycle bookkeeping."""

    id: str
    type: str = "ingest"
    status: str = STATUS_QUEUED
    params: Dict[str, Any] = field(default_factory=dict)
    message: str = ""
    error: Optional[str] = None
    result: Optional[Dict[str, Any]] = None

    created_at: float = field(default_factory=time.time)
    started_at: Optional[float] = None
    finished_at: Optional[float] = None

    # Progress counters (mirror the legacy status dict)
    discovered: int = 0
    fetched: int = 0
    processed: int = 0
    failed: int = 0
    indexed: int = 0
    indexed_documents: int = 0
    # Input pages/files have a different denominator from generated OKF
    # concepts. Keep it stable when total_documents switches to the indexing
    # denominator.
    total_processed_documents: int = 0
    total_documents: int = 0
    progress_percent: int = 0
    prompt_tokens_estimate: int = 0
    completion_tokens_estimate: int = 0
    total_tokens_estimate: int = 0
    # Count of Gemini 429/quota rate-limit hits during embedding (see
    # app.retrieval.hybrid_search.index_documents). Surfaced in the UI as a
    # distinct warning badge, since these retries can make indexing take much
    # longer than the document count alone would suggest, and previously were
    # only visible in the container logs, never in the dashboard.
    rate_limit_hits: int = 0

    # Pipeline stage for the live process-flow timeline in the UI.
    # One of: starting, discovering, downloading, cached, converting,
    # formatting, indexing, completed, failed, cancelled.
    stage: str = "starting"
    # Human readable headline for the current stage.
    stage_message: str = ""
    # The documentation source currently being processed (e.g. "kubernetes").
    current_source: str = ""

    # Not serialized: cooperative cancellation signal checked by the pipeline.
    cancel_event: Any = field(default_factory=threading.Event, repr=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
            "params": self.params,
            "message": self.message,
            "error": self.error,
            "result": self.result,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "discovered": self.discovered,
            "fetched": self.fetched,
            "processed": self.processed,
            "failed": self.failed,
            "indexed": self.indexed,
            "indexed_documents": self.indexed_documents,
            "total_processed_documents": self.total_processed_documents,
            "total_documents": self.total_documents,
            "progress_percent": self.progress_percent,
            "prompt_tokens_estimate": self.prompt_tokens_estimate,
            "completion_tokens_estimate": self.completion_tokens_estimate,
            "total_tokens_estimate": self.total_tokens_estimate,
            "rate_limit_hits": self.rate_limit_hits,
            "stage": self.stage,
            "stage_message": self.stage_message,
            "current_source": self.current_source,
        }

    def to_status_dict(self) -> dict:
        """Legacy-shaped status payload for the `/api/v1/ingest/status` endpoint."""
        return {
            "status": self.status,
            "job_id": self.id,
            "message": self.message,
            "discovered": self.discovered,
            "fetched": self.fetched,
            "processed": self.processed,
            "failed": self.failed,
            "indexed": self.indexed,
            "indexed_documents": self.indexed_documents,
            "total_processed_documents": self.total_processed_documents,
            "total_documents": self.total_documents,
            "progress_percent": self.progress_percent,
            "prompt_tokens_estimate": self.prompt_tokens_estimate,
            "completion_tokens_estimate": self.completion_tokens_estimate,
            "total_tokens_estimate": self.total_tokens_estimate,
            "rate_limit_hits": self.rate_limit_hits,
            "stage": self.stage,
            "stage_message": self.stage_message,
            "current_source": self.current_source,
            "error": self.error,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Job":
        known_fields = {k for k in cls.__annotations__ if k != "cancel_event"}
        job = cls(**{k: v for k, v in data.items() if k in known_fields})
        # Stale queued/running jobs from a previous process cannot resume.
        if job.status in ACTIVE_STATUSES:
            job.status = STATUS_FAILED
            job.error = job.error or "Job was interrupted by a process restart."
            job.finished_at = job.finished_at or time.time()
        return job
