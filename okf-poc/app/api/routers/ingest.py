from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import os
from pathlib import Path
from typing import Optional, List
import re

# Import the orchestrator we built in Phase 2
from app.ingestion import run_ingestion_pipeline
from app.core.config import settings
from app.ingestion.status import get_status, update_status
from app.jobs.manager import job_manager, JobCancelledError

# Tags help endpoints group neatly in the Swagger UI
router = APIRouter(prefix="/ingest", tags=["Ingestion"])


def _run_ingest_job(job):
    """JobManager handler for the 'ingest' job type."""
    params = job.params or {}
    try:
        result = run_ingestion_pipeline(
            cache_dir=params.get("cache_dir") or settings.CACHE_DIR,
            knowledge_dir=params.get("knowledge_dir") or settings.KNOWLEDGE_DIR,
            cancel_event=job.cancel_event,
            source_names=params.get("sources"),
        )
        return result
    except JobCancelledError:
        raise
    except Exception as exc:
        update_status(status="failed", message=str(exc))
        raise


# Register the ingestion handler once at import time.
job_manager.register_handler("ingest", _run_ingest_job)

@router.get("/sources")
async def list_available_sources():
    """List documentation sources available for ingestion (from sources.yaml)."""
    from app.ingestion.crawler import load_sources

    data = load_sources()
    sources = []
    for source in data.get("sources", []):
        sources.append(
            {
                "name": source.get("name"),
                "base_url": source.get("base_url"),
                "category": source.get("category"),
                "enabled": bool(source.get("enabled", False)),
            }
        )
    return {"sources": sources}

@router.get("/status")
async def get_ingestion_status():
    status = get_status()
    if "indexed_documents" not in status and "indexed" in status:
        status["indexed_documents"] = status["indexed"]
    return status

class IngestRequest(BaseModel):
    """Payload definition for triggering ingestion."""
    cache_dir: str = settings.CACHE_DIR
    knowledge_dir: str = settings.KNOWLEDGE_DIR
    sources: List[str] = []
class IngestResponse(BaseModel):
    """Structured response confirming ingestion status."""
    status: str
    message: str
    indexed_documents: int = 0


@router.post("/", response_model=IngestResponse)
async def ingest_documents(request: IngestRequest):
    """
    Triggers the OKF ingestion pipeline.
    Reads cached/raw documents from `cache_dir`, generates OKF metadata,
    saves them to `knowledge_dir`, and indexes them into Qdrant.

    Optional `sources` lists the documentation sources (from sources.yaml) to
    crawl. When omitted (None), the enabled sources are crawled. When an empty
    list is passed, crawling is skipped entirely and only cached/uploaded files
    are processed.

    The pipeline runs as a tracked Job (see /api/v1/jobs) with a queue:
    if ingestion is already running, the new request is queued instead of
    being silently dropped.
    """
    try:
        if job_manager.has_active_jobs():
            active = job_manager.get_active_job()
            return IngestResponse(
                status="queued",
                message="Ingestion is already running; your request was queued.",
                indexed_documents=active.indexed_documents if active else 0,
            )

        job = job_manager.submit(
            "ingest",
            params={
                "cache_dir": request.cache_dir,
                "knowledge_dir": request.knowledge_dir,
                "sources": request.sources or [],
            },
        )

        return IngestResponse(
            status="started",
            message="Ingestion pipeline started in the background (job id: {job.id}).".format(job=job),
            indexed_documents=0,
        )

    except Exception as e:
        print(f"❌ API Error during ingestion: {e}")
        raise HTTPException(status_code=500, detail=f"Ingestion pipeline failed: {str(e)}")


def _sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent path traversal and invalid characters.
    Returns a safe filename or raises ValueError if unsafe.
    """
    # Remove path components
    filename = os.path.basename(filename)
    
    # Check for empty or suspicious filenames
    if not filename or filename in (".", ".."):
        raise ValueError("Invalid filename")
    
    # Remove or replace dangerous characters
    # Allow: alphanumeric, dash, underscore, dot
    safe_filename = re.sub(r'[^\w\-.]', '_', filename)
    
    # Prevent hidden files
    if safe_filename.startswith('.'):
        safe_filename = 'uploaded_' + safe_filename
    
    # Ensure filename isn't too long (255 is typical filesystem limit)
    if len(safe_filename) > 255:
        name, ext = os.path.splitext(safe_filename)
        safe_filename = name[:255-len(ext)] + ext
    
    return safe_filename


def _validate_file_extension(filename: str) -> bool:
    """Check if file extension is supported."""
    supported_extensions = {'.pdf', '.md', '.txt', '.json'}
    ext = Path(filename).suffix.lower()
    return ext in supported_extensions


class UploadResponse(BaseModel):
    """Response for file upload endpoint."""
    success: bool
    uploaded_files: int
    processed_files: int
    concepts_created: int
    indexed: bool
    files: List[str]
    message: str
    errors: List[str] = []


@router.post("/upload", response_model=UploadResponse)
async def upload_documents(
    files: List[UploadFile] = File(...),
    sources: Optional[str] = Form(""),
):
    """
    Upload documents directly through the UI.
    Files are saved to the configured cache directory and then processed
    through the existing ingestion pipeline.

    Optional `sources` is a comma-separated list of documentation source
    names to crawl alongside the uploaded files.

    Supported formats: PDF (.pdf), Markdown (.md), Text (.txt), JSON (.json)
    """
    # Parse the comma-separated source list.
    source_names = []
    if sources:
        source_names = [
            s.strip()
            for s in sources.split(",")
            if s.strip()
        ]
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    # Check if ingestion is already running
    if job_manager.has_active_jobs():
        raise HTTPException(
            status_code=409,
            detail="Ingestion is already running. Please wait for it to complete."
        )
    
    cache_dir = settings.CACHE_DIR
    knowledge_dir = settings.KNOWLEDGE_DIR
    
    # Ensure cache directory exists
    os.makedirs(cache_dir, exist_ok=True)
    
    uploaded_files = []
    failed_files = []
    errors = []
    
    # Validate and save files
    for file in files:
        try:
            # Validate extension
            if not _validate_file_extension(file.filename):
                error_msg = f"{file.filename}: Unsupported file type. Only PDF, MD, TXT, and JSON are allowed."
                errors.append(error_msg)
                failed_files.append(file.filename)
                continue
            
            # Sanitize filename
            try:
                safe_filename = _sanitize_filename(file.filename)
            except ValueError as e:
                error_msg = f"{file.filename}: Invalid filename - {str(e)}"
                errors.append(error_msg)
                failed_files.append(file.filename)
                continue
            
            # Save file to cache directory
            file_path = os.path.join(cache_dir, safe_filename)
            
            # Read file content
            content = await file.read()
            
            # Validate file size (max 50MB)
            max_size = 50 * 1024 * 1024  # 50MB
            if len(content) > max_size:
                error_msg = f"{file.filename}: File too large (max 50MB)"
                errors.append(error_msg)
                failed_files.append(file.filename)
                continue
            
            # Write to cache
            with open(file_path, 'wb') as f:
                f.write(content)
            
            uploaded_files.append(safe_filename)
            print(f"✅ Uploaded: {safe_filename} ({len(content)} bytes)")
            
        except Exception as e:
            error_msg = f"{file.filename}: Upload failed - {str(e)}"
            errors.append(error_msg)
            failed_files.append(file.filename)
            print(f"❌ Upload error: {error_msg}")
    
    if not uploaded_files:
        return UploadResponse(
            success=False,
            uploaded_files=0,
            processed_files=0,
            concepts_created=0,
            indexed=False,
            files=[],
            message="No files were uploaded successfully",
            errors=errors
        )
    
    # Trigger ingestion pipeline
    try:
        job = job_manager.submit(
            "ingest",
            params={
                "cache_dir": cache_dir,
                "knowledge_dir": knowledge_dir,
                "sources": source_names,
            },
        )
        
        return UploadResponse(
            success=True,
            uploaded_files=len(uploaded_files),
            processed_files=len(uploaded_files),
            concepts_created=0,  # Will be updated by status endpoint
            indexed=False,  # Will be updated by status endpoint
            files=uploaded_files,
            message=f"Successfully uploaded {len(uploaded_files)} file(s). Processing started in background (job id: {job.id}).",
            errors=errors
        )
        
    except Exception as e:
        print(f"❌ Ingestion trigger error: {e}")
        return UploadResponse(
            success=False,
            uploaded_files=len(uploaded_files),
            processed_files=0,
            concepts_created=0,
            indexed=False,
            files=uploaded_files,
            message=f"Files uploaded but ingestion failed: {str(e)}",
            errors=errors + [str(e)]
        )

    
