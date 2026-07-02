from fastapi import APIRouter
from backend.storage.candidate_store import get_candidates
from backend.storage.job_store import get_job
from backend.ranking.scorer import overall_score

router = APIRouter()

@router.post("/rank-all")
def rank_all():

    candidates = get_candidates()
    job = get_job()

    print("JOB =", job)
    print("CANDIDATES =", candidates)

    if job is None:
        return {"error": "No Job Description uploaded."}

    if len(candidates) == 0:
        return {"error": "No resumes uploaded."}

    results = []

    for candidate in candidates:
        try:
            score = overall_score(candidate, job)
            results.append({

    "name": candidate.get("personal", {}).get("name","Unknown"),

    "score": score["overall_score"],

    "skill_score": score["skill_score"],

    "experience_score": score["experience_score"],

    "education_score": score["education_score"],

    "project_score": score["project_score"],

    "certification_score": score["certification_score"],

    "matched_skills": score["matched_skills"],

    "missing_skills": score["missing_skills"],

    "reason":
        f"Matched {len(score['matched_skills'])} required skills and missing {len(score['missing_skills'])} skills."

})

        except Exception as e:
            return {
                "candidate": candidate,
                "job": job,
                "error": str(e)
            }

    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "total_candidates": len(results),
        "ranking": results
    }