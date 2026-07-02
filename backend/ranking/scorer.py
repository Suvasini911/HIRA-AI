from backend.ranking.matcher import skill_match


def overall_score(candidate, job):

    # -----------------------
    # Candidate Skills
    # -----------------------
    skills = []

    if "skills" in candidate:
        for category in candidate["skills"].values():
            if isinstance(category, list):
                skills.extend(category)

    # -----------------------
    # Skill Match
    # -----------------------
    result = skill_match(
        skills,
        job["mandatory_skills"]
    )

    skill_score = result["score"]

    # -----------------------
    # Experience Score
    # -----------------------
    experience = len(candidate.get("experience", []))

    if experience >= 3:
        experience_score = 100
    elif experience == 2:
        experience_score = 80
    elif experience == 1:
        experience_score = 60
    else:
        experience_score = 30

    # -----------------------
    # Education Score
    # -----------------------
    education = candidate.get("education", [])

    if len(education) > 0:
        education_score = 100
    else:
        education_score = 40

    # -----------------------
    # Projects Score
    # -----------------------
    projects = candidate.get("projects", [])

    if len(projects) >= 3:
        project_score = 100
    elif len(projects) == 2:
        project_score = 80
    elif len(projects) == 1:
        project_score = 60
    else:
        project_score = 30

    # -----------------------
    # Certifications Score
    # -----------------------
    certs = candidate.get("certifications", [])

    certification_score = min(len(certs) * 20, 100)

    # -----------------------
    # Final Weighted Score
    # -----------------------
    overall = (
        skill_score * 0.50 +
        experience_score * 0.20 +
        education_score * 0.10 +
        project_score * 0.10 +
        certification_score * 0.10
    )

    overall = round(overall, 2)

    return {

        "overall_score": overall,

        "skill_score": skill_score,

        "experience_score": experience_score,

        "education_score": education_score,

        "project_score": project_score,

        "certification_score": certification_score,

        "matched_skills": result["matched"],

        "missing_skills": result["missing"]
    }