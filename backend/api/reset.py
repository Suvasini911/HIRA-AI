from fastapi import APIRouter
from backend.storage.candidate_store import clear_candidates
from backend.storage.job_store import set_job

router = APIRouter()

@router.post("/reset")
def reset():

    clear_candidates()

    set_job(None)

    return {
        "message": "System reset successfully."
    }