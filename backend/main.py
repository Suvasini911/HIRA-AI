from fastapi import FastAPI

from backend.api.resume import router as resume_router
from backend.api.job import router as job_router
from backend.api.ranking import router as ranking_router
from backend.api.rank_all import router as rank_all_router
from backend.api.reset import router as reset_router


app = FastAPI(
    title="HIRA AI"
)

app.include_router(resume_router)
app.include_router(job_router)
app.include_router(ranking_router)
app.include_router(rank_all_router)
app.include_router(reset_router)

@app.get("/")
def home():
    return {
        "message":"Welcome to HIRA 🚀"
    }