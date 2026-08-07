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
}


def update_status(**kwargs):
    with _lock:
        _status.update(kwargs)


def get_status():
    with _lock:
        return dict(_status)


def reset_status():
    update_status(
        status="running",
        message="Ingestion started",
        discovered=0,
        fetched=0,
        processed=0,
        failed=0,
        indexed=0,
    )