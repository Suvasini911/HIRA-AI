import streamlit as st

from utils.api import (
    upload_resume,
    analyze_job,
    rank_all,
    reset
)

from components.analytics import analytics
from components.candidate_card import candidate_card
from components.hidden_gem import hidden_gem
from components.recruiter_chat import recruiter_chat
from components.charts import score_chart
from utils.export_excel import export_results

st.set_page_config(
    page_title="HIRA AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 HIRA AI")
st.subheader("Intelligent Candidate Discovery Platform")

st.divider()

uploaded_files = st.file_uploader(
    "📂 Upload Candidate Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

job = st.text_area(
    "💼 Paste Job Description",
    height=220
)

# Initialize results
results = None

if st.button("🚀 Analyze Candidates"):

    reset()

    if uploaded_files:
        with st.spinner("Uploading resumes..."):
            for file in uploaded_files:
                upload_resume(file)

    if job:
        with st.spinner("Analyzing job description..."):
            analyze_job(job)

    with st.spinner("Ranking candidates..."):
        results = rank_all()

    # Check API response
    if not results or "ranking" not in results:
        st.error(results.get("error", "Unable to rank candidates.") if results else "No response from backend.")
        st.stop()

    # Dashboard Analytics
    total_candidates = len(results["ranking"])

    average_score = (
        round(
            sum(c["score"] for c in results["ranking"]) / total_candidates,
            1
        )
        if total_candidates else 0
    )

    skill_counter = {}

    for c in results["ranking"]:
        for skill in c["matched_skills"]:
            skill_counter[skill] = skill_counter.get(skill, 0) + 1

    top_skill = max(skill_counter, key=skill_counter.get) if skill_counter else "-"

    best_candidate = (
        results["ranking"][0]["name"]
        if total_candidates else "-"
    )

    analytics(
        total_candidates,
        average_score,
        top_skill,
        best_candidate
    )

    st.divider()

    score_chart(results["ranking"])

    st.divider()

    st.divider()

    st.header("🏆 Ranked Candidates")

    for i, candidate in enumerate(results["ranking"], start=1):
        candidate_card(candidate, i)

    st.divider()

    hidden_gem(results["ranking"])

    st.divider()

    recruiter_chat()

    excel_file = export_results(results["ranking"])

with open(excel_file, "rb") as file:
    st.download_button(
        "📥 Download Ranking Excel",
        file,
        file_name="Candidate_Ranking.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

   