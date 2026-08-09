"""
Job Management REST API.

Exposes the JobManager (app.jobs.manager) over HTTP so callers can list job
history, inspect a single job, and request cancellation. The legacy
`/ingest/status` and `/ingest/` endpoints remain unchanged and are backed by the
same JobManager singleton.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Optional

from app.jobs.manager import job_manager
from app.jobs.models import Job

router = APIRouter(prefix="/jobs", tags=["Jobs"])


def _job_payload(job: Job) -> dict:
    return job.to_dict()


@router.get("/", response_model=List[dict])
async def list_jobs(
    limit: Optional[int] = None,
    status: Optional[str] = None,
):
    """List jobs, newest first, optionally filtered by status."""
    jobs = job_manager.list_jobs(limit=limit)
    if status:
        jobs = [j for j in jobs if j.status == status]
    return [_job_payload(j) for j in jobs]


@router.get("/{job_id}", response_model=dict)
async def get_job(job_id: str):
    """Full detail of a single job (progress, timestamps, result, error)."""
    job = job_manager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found.")
    return _job_payload(job)


@router.post("/{job_id}/cancel", response_model=dict)
async def cancel_job(job_id: str):
    """Request cancellation of a queued or running job."""
    job = job_manager.cancel(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found.")
    return _job_payload(job)
