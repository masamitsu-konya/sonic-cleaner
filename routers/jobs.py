from uuid import uuid4
from typing import Dict

from fastapi import APIRouter, HTTPException

from app.models import JobCreate, JobStatus

router = APIRouter(prefix="/jobs", tags=["jobs"])

# ───────────────────────────
# 仮置き：メモリ内ストア
# 後で DB / Cloud Tasks に置換
_JOB_DB: Dict[str, JobStatus] = {}
# ───────────────────────────

@router.post("/", response_model=JobStatus, status_code=202)
async def create_job(payload: JobCreate) -> JobStatus:
    job_id = str(uuid4())
    status = JobStatus(id=job_id, state="queued")
    _JOB_DB[job_id] = status

    # TODO: キューに投入して非同期処理へ
    return status


@router.get("/{job_id}", response_model=JobStatus)
async def get_job(job_id: str) -> JobStatus:
    job = _JOB_DB.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
