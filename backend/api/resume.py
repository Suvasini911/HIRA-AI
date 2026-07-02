from fastapi import APIRouter, UploadFile, File
import os

from backend.parsers.resume_parser import extract_text_from_pdf
from backend.services.resume_intelligence import extract_candidate_info

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)

    # AI understands the resume
    candidate = extract_candidate_info(text)

    from backend.storage.candidate_store import add_candidate
    add_candidate(candidate)

    # Return structured JSON
    return {
        "filename": file.filename,
        "candidate": candidate
    }