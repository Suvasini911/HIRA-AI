from openpyxl import Workbook


def export_results(results):

    wb = Workbook()
    ws = wb.active
    ws.title = "Candidate Ranking"

    ws.append([
        "Rank",
        "Candidate",
        "Overall Score",
        "Skill Score",
        "Experience Score",
        "Education Score",
        "Project Score",
        "Certification Score",
        "Matched Skills",
        "Missing Skills"
    ])

    for i, c in enumerate(results["ranking"], start=1):

        ws.append([
            i,
            c["name"],
            c["score"],
            c.get("skill_score", 0),
            c.get("experience_score", 0),
            c.get("education_score", 0),
            c.get("project_score", 0),
            c.get("certification_score", 0),
            ", ".join(c["matched_skills"]),
            ", ".join(c["missing_skills"])
        ])

    wb.save("Candidate_Ranking.xlsx")