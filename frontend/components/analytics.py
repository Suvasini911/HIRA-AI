import streamlit as st


def analytics(total, average, top_skill, best_candidate):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Total Candidates", total)

    with c2:
        st.metric("⭐ Average Match", f"{average:.1f}%")

    with c3:
        st.metric("🔥 Top Skill", top_skill)

    with c4:
        st.metric("🥇 Best Candidate", best_candidate)