def skill_match(candidate_skills, job_skills):

    candidate = set(skill.lower() for skill in candidate_skills)
    job = set(skill.lower() for skill in job_skills)

    matched = candidate.intersection(job)

    missing = job.difference(candidate)

    score = 0

    if len(job) > 0:
        score = round(len(matched)/len(job)*100,2)

    return {
        "score":score,
        "matched":list(matched),
        "missing":list(missing)
    }