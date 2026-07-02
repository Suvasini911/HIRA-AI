import streamlit as st


def recruiter_chat():

    st.subheader("🤖 Recruiter Copilot")

    question = st.text_input(
        "Ask anything about the candidates"
    )

    if question:

        q = question.lower()

        if "python" in q:

            st.success(
                "Candidates with Python:\n\n• Suvasini\n• Smit"
            )

        elif "aws" in q:

            st.success(
                "AWS Experience:\n\n• Suvasini"
            )

        elif "best" in q:

            st.success(
                "Best Candidate:\n\n🏆 Suvasini"
            )

        else:

            st.info(
                "LLM-powered recruiter assistant will answer this soon."
            )