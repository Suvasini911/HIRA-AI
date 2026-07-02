import streamlit as st


def candidate_card(candidate, rank=1):

    score = float(candidate.get("score", 0))

    if score >= 90:
        badge = "🟢 Highly Recommended"
    elif score >= 75:
        badge = "🟡 Recommended"
    else:
        badge = "🔴 Needs Review"

    with st.container(border=True):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"## 🏆 Rank #{rank}")
            st.markdown(f"### 👤 {candidate.get('name','Unknown')}")

        with col2:
            st.metric("Overall Match", f"{score:.1f}%")

        st.progress(score / 100)

        st.success(badge)

        st.divider()

        st.markdown("## 📊 Score Breakdown")

        c1, c2 = st.columns(2)

        with c1:

            skill = candidate.get("skill_score", 0)
            st.write(f"**Skill Match : {skill:.1f}%**")
            st.progress(skill / 100)

            exp = candidate.get("experience_score", 0)
            st.write(f"**Experience : {exp:.1f}%**")
            st.progress(exp / 100)

            edu = candidate.get("education_score", 0)
            st.write(f"**Education : {edu:.1f}%**")
            st.progress(edu / 100)

        with c2:

            proj = candidate.get("project_score", 0)
            st.write(f"**Projects : {proj:.1f}%**")
            st.progress(proj / 100)

            cert = candidate.get("certification_score", 0)
            st.write(f"**Certifications : {cert:.1f}%**")
            st.progress(cert / 100)

        st.divider()

        left, right = st.columns(2)

        with left:

            st.markdown("### ✅ Matched Skills")

            matched = candidate.get("matched_skills", [])

            if matched:
                for skill in matched:
                    st.write(f"✔ {skill}")
            else:
                st.write("None")

        with right:

            st.markdown("### ❌ Missing Skills")

            missing = candidate.get("missing_skills", [])

            if missing:
                for skill in missing:
                    st.write(f"• {skill}")
            else:
                st.write("None")

        st.divider()

        st.markdown("### 🤖 AI Recommendation")

        st.markdown("### 📝 Why this Candidate?")

        st.info(
    candidate.get(
        "reason",
        "Candidate evaluated using skill, education, projects and experience."
    )
     )

        if score >= 90:
            st.success(
                "Excellent fit. Strongly recommend scheduling the interview immediately."
            )

        elif score >= 75:
            st.info(
                "Good fit. Recommended for technical interview."
            )

        elif score >= 50:
            st.warning(
                "Potential fit. Recruiter review recommended."
            )

        else:
            st.error(
                "Low match for this role."
            )