import os
import time

import pytest

from app.jobs.manager import JobManager, JobCancelledError
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


@pytest.fixture
def manager(tmp_path):
    return JobManager(persist_dir=str(tmp_path / ".jobs"))


def test_job_defaults():
    job = Job(id="abc")
    assert job.status == STATUS_QUEUED
    assert job.type == "ingest"
    assert job.cancel_event is not None
    assert not job.cancel_event.is_set()


def test_job_to_dict_roundtrip_excludes_cancel_event():
    job = Job(id="abc", status=STATUS_COMPLETED, message="working")
    data = job.to_dict()
    assert "cancel_event" not in data
    assert data["id"] == "abc"
    restored = Job.from_dict(data)
    assert restored.status == STATUS_COMPLETED
    assert restored.message == "working"


def test_job_from_dict_marks_stale_active_as_failed():
    data = Job(id="stale", status=STATUS_RUNNING).to_dict()
    job = Job.from_dict(data)
    assert job.status == STATUS_FAILED
    assert "restart" in (job.error or "")


def test_submit_runs_handler_to_completion(manager):
    manager.register_handler("ingest", lambda job: {"indexed_documents": 2})
    job = manager.submit("ingest", {"cache_dir": "/tmp"})
    assert job.status == STATUS_QUEUED
    _wait_terminal(job)
    assert job.status == STATUS_COMPLETED
    assert job.result == {"indexed_documents": 2}
    assert job.finished_at is not None
    # Persisted to disk.
    assert os.path.exists(os.path.join(manager._persist_dir, f"{job.id}.json"))


def test_handler_failure_marks_job_failed(manager):
    def failing(job):
        raise RuntimeError("boom")

    manager.register_handler("ingest", failing)
    job = manager.submit("ingest")
    _wait_terminal(job)
    assert job.status == STATUS_FAILED
    assert "boom" in (job.error or "")


def test_missing_handler_marks_job_failed(manager):
    job = manager.submit("unknown_type")
    _wait_terminal(job)
    assert job.status == STATUS_FAILED
    assert "No handler" in (job.error or "")


def test_cancel_running_job(manager):
    def slow(job):
        job.cancel_event.wait(2.0)
        if job.cancel_event.is_set():
            raise JobCancelledError
        return "done"

    manager.register_handler("ingest", slow)
    job = manager.submit("ingest")
    time.sleep(0.2)
    cancelled = manager.cancel(job.id)
    assert cancelled.status == STATUS_CANCELLING
    assert job.cancel_event.is_set()
    _wait_terminal(job)
    assert job.status == STATUS_CANCELLED


def test_cancel_queued_job_before_start(manager):
    # A slow first job keeps the worker busy; the second stays queued.
    manager.register_handler("slow", lambda job: job.cancel_event.wait(0.5) or "first")
    manager.register_handler("fast", lambda job: {"ok": True})

    first = manager.submit("slow")
    second = manager.submit("fast")
    # second is queued behind first
    manager.cancel(second.id)
    assert second.status == STATUS_CANCELLED
    _wait_terminal(first)
    assert first.status == STATUS_COMPLETED


def test_cancel_unknown_job_returns_none(manager):
    assert manager.cancel("nope") is None


def test_update_active_status_mirrors_progress(manager):
    def handler(job):
        manager.update_active_status(
            processed=4,
            total_processed_documents=5,
            total_documents=10,
            indexed=7,
        )
        return "ok"

    manager.register_handler("ingest", handler)
    job = manager.submit("ingest")
    _wait_terminal(job)
    # Derived fields computed on the job.
    assert job.processed == 4
    assert job.total_processed_documents == 5
    assert job.to_status_dict()["total_processed_documents"] == 5
    # While a job is running the progress is stage/counter-derived, but a
    # terminal (completed) job always reports 100% so the UI progress bar
    # reaches the end when the pipeline finishes.
    assert job.progress_percent == 100
    assert job.indexed_documents == 7


def test_token_usage_accumulates_and_survives_job_completion(manager):
    def handler(job):
        manager.add_active_token_usage(100, 20)
        manager.add_active_token_usage(50, 10)
        return "ok"

    manager.register_handler("ingest", handler)
    job = manager.submit("ingest")
    _wait_terminal(job)

    assert job.prompt_tokens_estimate == 150
    assert job.completion_tokens_estimate == 30
    assert job.total_tokens_estimate == 180
    assert manager.get_job(job.id).total_tokens_estimate == 180


def test_list_jobs_newest_first(manager):
    manager.register_handler("ingest", lambda job: None)
    first = manager.submit("ingest")
    time.sleep(0.05)
    second = manager.submit("ingest")
    ids = [j.id for j in manager.list_jobs()]
    assert ids.index(second.id) < ids.index(first.id)
    assert [j.id for j in manager.list_jobs(limit=1)] == [second.id]


def _wait_terminal(job, timeout=5.0):
    deadline = time.time() + timeout
    while job.status in (STATUS_QUEUED, STATUS_RUNNING, STATUS_CANCELLING):
        if time.time() > deadline:
            raise AssertionError(f"Job did not reach a terminal state: {job.status}")
        time.sleep(0.02)
