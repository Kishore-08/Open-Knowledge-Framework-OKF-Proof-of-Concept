import threading

_lock = threading.Lock()

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
}


def update_status(**kwargs):
    with _lock:
        _status.update(kwargs)
        if "indexed" in kwargs and "indexed_documents" not in kwargs:
            _status["indexed_documents"] = kwargs["indexed"]
        if "indexed_documents" in kwargs and "indexed" not in kwargs:
            _status["indexed"] = kwargs["indexed_documents"]

        # Proactively derive the UI-ready progress bar figure.
        processed = _status.get("processed", 0) or 0
        total_documents = _status.get("total_documents") or 0
        if total_documents:
            _status["progress_percent"] = min(100, int(round((processed / total_documents) * 100)))
        elif _status.get("status") in {"completed", "success"}:
            _status["progress_percent"] = 100
        else:
            _status["progress_percent"] = _status.get("progress_percent", 0) or 0

        if "prompt_tokens_estimate" in kwargs or "completion_tokens_estimate" in kwargs:
            prompt_tokens = _status.get("prompt_tokens_estimate", 0) or 0
            completion_tokens = _status.get("completion_tokens_estimate", 0) or 0
            _status["total_tokens_estimate"] = prompt_tokens + completion_tokens


def get_status():
    with _lock:
        payload = dict(_status)
        if "indexed_documents" not in payload and "indexed" in payload:
            payload["indexed_documents"] = payload["indexed"]
        if "indexed" not in payload and "indexed_documents" in payload:
            payload["indexed"] = payload["indexed_documents"]
        if payload.get("total_documents"):
            payload["progress_percent"] = min(
                100,
                int(round((payload.get("processed", 0) / payload.get("total_documents")) * 100)),
            )
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
    )