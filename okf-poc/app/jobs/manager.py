"""
JobManager: a real ingestion job system for the OKF PoC.

Replaces the legacy "fire a background asyncio task and mutate a global dict"
approach with:

* a submit/queue/run lifecycle (`queued -> running -> completed/failed/cancelled`),
* cooperative cancellation via a per-job `threading.Event`,
* on-disk persistence (JSON under `cache/.jobs/`) so job history survives
  process restarts, and
* a worker thread that runs at most one job at a time while later submissions
  wait in the queue.

The pipeline still reports progress through `app.ingestion.status.update_status`
(unchanged), which this manager mirrors onto the active job so both the legacy
`/api/v1/ingest/status` endpoint and the new `/api/v1/jobs` endpoints stay in
sync.
"""

import json
import os
import threading
import time
import uuid
from typing import Any, Dict, List, Optional

from app.jobs.models import (
    Job,
    ACTIVE_STATUSES,
    STATUS_CANCELLED,
    STATUS_CANCELLING,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_QUEUED,
    STATUS_RUNNING,
)


class JobCancelledError(Exception):
    """Raised by a job handler when cooperative cancellation is requested."""


# ---------------------------------------------------------------------------
# Stage-aware progress
# ---------------------------------------------------------------------------
# The overall progress bar should move continuously from "source selected"
# through download → cache → OKF conversion → indexing, instead of staying at
# 0% for the whole crawl (which only counts documents that have been converted,
# so the old formula could not move before the crawl finished).
STAGE_PERCENT = {
    "queued": 2,
    "starting": 2,
    "discovering": 6,
    "downloading": 10,     # 10 -> 48 by fetched/discovered
    "cached": 48,
    "converting": 48,      # 48 -> 70 by processed/total
    "formatting": 70,      # 70 -> 90 by processed/total
    "indexing": 90,        # 90 -> 99 by indexed/total_documents
    "completed": 100,
    "success": 100,
}


def compute_stage_progress(
    *,
    status: str = "",
    stage: str = "",
    fetched: int = 0,
    discovered: int = 0,
    processed: int = 0,
    total_documents: int = 0,
    indexed: int = 0,
) -> int:
    """
    Return a 0-100 progress figure that reflects both the pipeline stage and the
    live counters, so the progress bar animates continuously instead of jumping.
    """
    status = (status or "").lower()
    if status in ("completed", "success"):
        return 100

    stage = (stage or "starting").lower()
    base = STAGE_PERCENT.get(stage, 2)
    total = int(total_documents or 0)

    if stage == "downloading":
        if discovered:
            ratio = min(1.0, int(fetched or 0) / int(discovered))
            return min(46, base + int(36 * ratio))
        return base
    if stage in ("converting", "formatting"):
        if total:
            ratio = min(1.0, int(processed or 0) / total)
            span = 22 if stage == "converting" else 20
            return min(base + span - 1, base + int(span * ratio))
        return base
    if stage == "indexing":
        # Embedding can be slow (429 retries with multi-second backoff per
        # document), so without this the bar sat frozen at a flat 92% for
        # the entire indexing phase - often the longest part of a run -
        # making it look stuck even while documents were actively being
        # embedded one at a time in the background.
        if total:
            ratio = min(1.0, int(indexed or 0) / total)
            return min(99, base + int(9 * ratio))
        return base
    return base


class JobManager:
    def __init__(self, persist_dir: str = "cache/.jobs"):
        self._lock = threading.RLock()
        self._persist_dir = persist_dir
        self._jobs: Dict[str, Job] = {}
        self._queue: List[str] = []
        self._active_job_id: Optional[str] = None
        self._worker: Optional[threading.Thread] = None
        self._handlers: Dict[str, Any] = {}

        os.makedirs(self._persist_dir, exist_ok=True)
        self._load_persisted_jobs()

    # ------------------------------------------------------------------ setup

    def register_handler(self, job_type: str, handler) -> None:
        """Register the callable that executes a given job type.

        The handler is invoked as ``handler(job=job)`` and should raise
        ``JobCancelledError`` (or return early) when ``job.cancel_event`` is set.
        """
        self._handlers[job_type] = handler

    # ------------------------------------------------------------- lifecycle

    def submit(self, job_type: str, params: Optional[Dict[str, Any]] = None) -> Job:
        """Create and enqueue a new job. Starts the worker if needed."""
        with self._lock:
            job = Job(
                id=uuid.uuid4().hex[:12],
                type=job_type,
                params=params or {},
                status=STATUS_QUEUED,
            )
            self._jobs[job.id] = job
            self._queue.append(job.id)
            self._persist(job)

        self._ensure_worker()
        return job

    def cancel(self, job_id: str) -> Optional[Job]:
        """Request cancellation of a queued or running job."""
        with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return None
            if job.status == STATUS_QUEUED:
                # Not started yet: cancel immediately and drop from the queue.
                if job.id in self._queue:
                    self._queue.remove(job.id)
                job.status = STATUS_CANCELLED
                job.error = "Job was cancelled before it started."
                job.finished_at = time.time()
                self._persist(job)
            elif job.status == STATUS_RUNNING:
                job.status = STATUS_CANCELLING
                job.cancel_event.set()
                job.message = "Cancellation requested"
                self._persist(job)
            return job

    # ------------------------------------------------------------------ query

    def get_job(self, job_id: str) -> Optional[Job]:
        with self._lock:
            return self._jobs.get(job_id)

    def list_jobs(self, limit: Optional[int] = None) -> List[Job]:
        with self._lock:
            jobs = sorted(
                self._jobs.values(),
                key=lambda j: j.created_at,
                reverse=True,
            )
            if limit is not None:
                jobs = jobs[:limit]
            return list(jobs)

    def has_active_jobs(self) -> bool:
        with self._lock:
            return any(j.status in ACTIVE_STATUSES for j in self._jobs.values())

    def get_active_job(self) -> Optional[Job]:
        """Return the actual currently running job, otherwise the next queued job."""
        with self._lock:
            # Always prefer the actual running job.
            if self._active_job_id:
                active = self._jobs.get(self._active_job_id)

                if active and active.status in {
                    STATUS_RUNNING,
                    STATUS_CANCELLING,
                }:
                    return active

            # If worker has not started yet, return queued job.
            for job_id in self._queue:
                job = self._jobs.get(job_id)

                if job and job.status == STATUS_QUEUED:
                    return job

            return None

    # ------------------------------------------------------------- progress

    def update_active_status(self, **kwargs) -> None:
        """Mirror a pipeline ``update_status`` call onto the running job."""
        with self._lock:
            job = self._jobs.get(self._active_job_id) if self._active_job_id else None
            if job is None or job.status not in ACTIVE_STATUSES:
                return
            for key, value in kwargs.items():
                if hasattr(job, key):
                    setattr(job, key, value)
            self._sync_derived_fields(job)
            self._persist(job)

    def add_active_token_usage(self, prompt_tokens: int, completion_tokens: int) -> None:
        """Atomically add one LLM call's estimated usage to the active run."""
        with self._lock:
            job = self._jobs.get(self._active_job_id) if self._active_job_id else None
            if job is None or job.status not in ACTIVE_STATUSES:
                return
            job.prompt_tokens_estimate += max(0, int(prompt_tokens or 0))
            job.completion_tokens_estimate += max(0, int(completion_tokens or 0))
            self._sync_derived_fields(job)
            self._persist(job)

    @staticmethod
    def _sync_derived_fields(job: Job) -> None:
        if "indexed_documents" in vars(job):
            if job.indexed_documents != job.indexed:
                job.indexed_documents = job.indexed
        job.progress_percent = compute_stage_progress(
            status=job.status,
            stage=job.stage,
            fetched=job.fetched,
            discovered=job.discovered,
            processed=job.processed,
            total_documents=job.total_documents,
            indexed=job.indexed,
        )
        job.total_tokens_estimate = (
            job.prompt_tokens_estimate + job.completion_tokens_estimate
        )

    # ------------------------------------------------------------- execution

    def _ensure_worker(self) -> None:
        with self._lock:
            if self._worker is None or not self._worker.is_alive():
                self._worker = threading.Thread(target=self._worker_loop, daemon=True)
                self._worker.start()

    def _worker_loop(self) -> None:
        while True:
            with self._lock:
                job_id = self._queue[0] if self._queue else None
            if job_id is None:
                return
            self._execute(job_id)

    def _execute(self, job_id: str) -> None:
        with self._lock:
            job = self._jobs.get(job_id)
            if job is None or job.status != STATUS_QUEUED:
                return
            job.status = STATUS_RUNNING
            job.started_at = time.time()
            job.cancel_event.clear()
            self._active_job_id = job.id
            self._persist(job)
            handler = self._handlers.get(job.type)

        if handler is None:
            self._finish(job, STATUS_FAILED, error=f"No handler registered for job type: {job.type}")
            return

        try:
            result = handler(job=job)
            self._finish(job, STATUS_COMPLETED, result=result)
        except JobCancelledError:
            self._finish(job, STATUS_CANCELLED, error="Job was cancelled by the user.")
        except Exception as exc:  # noqa: BLE001 - the job must fail, never the worker
            self._finish(job, STATUS_FAILED, error=str(exc))

    def _finish(self, job: Job, status: str, error: str = None, result=None) -> None:
        with self._lock:
            job.status = status
            job.error = error or (job.error if status == STATUS_FAILED else None)
            if status == STATUS_COMPLETED:
                job.progress_percent = 100
                if not job.stage:
                    job.stage = "completed"
            if result is not None:
                job.result = result
            job.finished_at = time.time()
            if job.id in self._queue:
                self._queue.remove(job.id)
            if self._active_job_id == job.id:
                self._active_job_id = None
            self._persist(job)

    # ------------------------------------------------------------ persistence

    def _persist(self, job: Job) -> None:
        path = os.path.join(self._persist_dir, f"{job.id}.json")
        temp_path = f"{path}.tmp"
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(job.to_dict(), f, indent=2, sort_keys=True)
        os.replace(temp_path, path)

    def _load_persisted_jobs(self) -> None:
        for filename in os.listdir(self._persist_dir):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(self._persist_dir, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not isinstance(data, dict) or "id" not in data:
                    continue
                job = Job.from_dict(data)
                self._jobs[job.id] = job
            except (OSError, json.JSONDecodeError) as exc:
                print(f"⚠️ Could not load persisted job {path}: {exc}")


job_manager = JobManager(persist_dir=os.path.join("cache", ".jobs"))
