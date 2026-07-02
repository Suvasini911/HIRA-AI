from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.job_intelligence import extract_job_info

router = APIRouter()


class JobInput(BaseModel):
    text: str


@router.post("/analyze-job")
def analyze_job(job: JobInput):

    result = extract_job_info(job.text)
    from backend.storage.job_store import set_job
    set_job(result)

    return result