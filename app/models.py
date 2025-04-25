from pydantic import BaseModel, HttpUrl, Field


class JobCreate(BaseModel):
    source_url: HttpUrl
    trim_silence_ms: int = Field(400, ge=0, le=10_000)
    normalize_db: int = -3


class JobStatus(BaseModel):
    id: str
    state: str  # queued / processing / done / error
    result_url: HttpUrl | None = None
