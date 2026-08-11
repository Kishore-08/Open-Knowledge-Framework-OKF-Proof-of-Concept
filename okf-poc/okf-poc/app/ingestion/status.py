import threading

from app.jobs.manager import job_manager, compute_stage_progress

_lock = threading.Lock()

# Legacy fallback dict used when no job is active (idle state). The JobManager is
# the source of truth while a job runs; these helpers keep the old
# `/api/v1/ingest/status` contract working for callers that poll it directly.
_status = {
    "status": "idle",
    "message": "No ingestion running",
    "discovered": 0,
    "fetched": 0,
    "processed": 0,
    "failed": 0,
    "indexed": 0,
    "indexed_documents": 0,
    "total_documents": 0,
    "progress_percent": 0,
    "prompt_tokens_estimate": 0,
    "completion_tokens_estimate": 0,
    "total_tokens_estimate": 0,
    "rate_limit_hits": 0,
    "stage": "idle",
    "stage_message": "",
    "current_source": "",
}


def update_status(**kwargs):
    # Forward progress onto the active job (job manager derives the same derived
    # fields the legacy dict computed). Ignored when no job is running.
    job_manager.update_active_status(**kwargs)

    with _lock:
        _status.update(kwargs)
        if "indexed" in kwargs and "indexed_documents" not in kwargs:
            _status["indexed_documents"] = kwargs["indexed"]
        if "indexed_documents" in kwargs and "indexed" not in kwargs:
            _status["indexed"] = kwargs["indexed_documents"]

        # Stage-aware progress: the bar moves continuously from source selection
        # through download -> cache -> OKF conversion -> indexing instead of
        # staying frozen at 0 while the crawler is still running.
        _status["progress_percent"] = compute_stage_progress(
            status=_status.get("status", "idle"),
            stage=_status.get("stage", ""),
            fetched=_status.get("fetched", 0) or 0,
            discovered=_status.get("discovered", 0) or 0,
            processed=_status.get("processed", 0) or 0,
            total_documents=_status.get("total_documents", 0) or 0,
            indexed=_status.get("indexed", 0) or 0,
        )
        if _status.get("status") in {"completed", "success"}:
            _status["progress_percent"] = 100

        if "prompt_tokens_estimate" in kwargs or "completion_tokens_estimate" in kwargs:
            prompt_tokens = _status.get("prompt_tokens_estimate", 0) or 0
            completion_tokens = _status.get("completion_tokens_estimate", 0) or 0
            _status["total_tokens_estimate"] = prompt_tokens + completion_tokens


def get_status():
    # Prefer the live job when one exists so the legacy endpoint reports the
    # same progress as the new /jobs endpoints.
    active_job = job_manager.get_active_job()
    if active_job is not None:
        return active_job.to_status_dict()

    with _lock:
        payload = dict(_status)
        if "indexed_documents" not in payload and "indexed" in payload:
            payload["indexed_documents"] = payload["indexed"]
        if "indexed" not in payload and "indexed_documents" in payload:
            payload["indexed"] = payload["indexed_documents"]
        payload["progress_percent"] = compute_stage_progress(
            status=payload.get("status", "idle"),
            stage=payload.get("stage", ""),
            fetched=payload.get("fetched", 0) or 0,
            discovered=payload.get("discovered", 0) or 0,
            processed=payload.get("processed", 0) or 0,
            total_documents=payload.get("total_documents", 0) or 0,
            indexed=payload.get("indexed", 0) or 0,
        )
        if payload.get("status") in {"completed", "success"}:
            payload["progress_percent"] = 100
        return payload


def reset_status():
    update_status(
        status="running",
        message="Ingestion started",
        discovered=0,
        fetched=0,
        processed=0,
        failed=0,
        indexed=0,
        indexed_documents=0,
        total_documents=0,
        progress_percent=0,
        prompt_tokens_estimate=0,
        completion_tokens_estimate=0,
        total_tokens_estimate=0,
        rate_limit_hits=0,
        stage="starting",
        stage_message="",
        current_source="",
    )
