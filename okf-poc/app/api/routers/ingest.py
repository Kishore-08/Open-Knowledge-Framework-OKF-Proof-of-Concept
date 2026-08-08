from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
import asyncio
import os
from pathlib import Path
from typing import Optional, List
import re

# Import the orchestrator we built in Phase 2
from app.ingestion import run_ingestion_pipeline
from app.core.config import settings
from app.ingestion.status import get_status, update_status

# Tags help group endpoints neatly in the Swagger UI
router = APIRouter(prefix="/ingest", tags=["Ingestion"])

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
    """
    try:
        current = get_status()
        if current.get("status") in {"running", "starting"}:
            return IngestResponse(
                status=current.get("status", "running"),
                message="Ingestion is already running.",
                indexed_documents=current.get("indexed_documents", current.get("indexed", 0)),
            )

        update_status(
            status="starting",
            message="Ingestion started",
            discovered=0,
            fetched=0,
            processed=0,
            failed=0,
            indexed=0,
            indexed_documents=0,
        )

        asyncio.create_task(
            asyncio.to_thread(
                run_ingestion_pipeline,
                cache_dir=request.cache_dir,
                knowledge_dir=request.knowledge_dir,
            )
        )

        return IngestResponse(
            status="started",
            message="Ingestion pipeline started in the background.",
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
async def upload_documents(files: List[UploadFile] = File(...)):
    """
    Upload documents directly through the UI.
    Files are saved to the configured cache directory and then processed
    through the existing ingestion pipeline.
    
    Supported formats: PDF (.pdf), Markdown (.md), Text (.txt), JSON (.json)
    """
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    # Check if ingestion is already running
    current = get_status()
    if current.get("status") in {"running", "starting"}:
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
        update_status(
            status="starting",
            message="Processing uploaded documents",
            discovered=len(uploaded_files),
            fetched=0,
            processed=0,
            failed=0,
            indexed=0,
            indexed_documents=0,
        )
        
        # Run ingestion in background
        asyncio.create_task(
            asyncio.to_thread(
                run_ingestion_pipeline,
                cache_dir=cache_dir,
                knowledge_dir=knowledge_dir,
            )
        )
        
        return UploadResponse(
            success=True,
            uploaded_files=len(uploaded_files),
            processed_files=len(uploaded_files),
            concepts_created=0,  # Will be updated by status endpoint
            indexed=False,  # Will be updated by status endpoint
            files=uploaded_files,
            message=f"Successfully uploaded {len(uploaded_files)} file(s). Processing started in background.",
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

    
