import streamlit as st


def hidden_gem(results):
    st.write("Results type:", type(results))
    st.write(results)

    if not results:
        return

    hidden = None

    for candidate in results:

        score = candidate.get("score", 0)
        missing = len(candidate.get("missing_skills", []))

        # Hidden gem:
        # medium score but only a few missing skills
        if 40 <= score <= 70 and missing <= 4:
            hidden = candidate
            break

    st.subheader("💎 Hidden Gem")

    if hidden:

        st.success(
f"""
### 💎 {hidden['name']}

📊 Match Score: **{hidden['score']}%**

🧠 AI Insight

This candidate is not among the top-ranked profiles,
but demonstrates strong core technical alignment with
the job requirements.

Only a few critical skills are missing, making this
candidate a high-potential hire after short-term
training.

**Recommendation:** Consider for interview despite
not being the highest-ranked applicant.
"""
)

    else:
        st.info("No hidden gem detected.")