import streamlit as st
import plotly.express as px
import pandas as pd


def score_chart(ranking):

    if not ranking:
        return

    df = pd.DataFrame({
        "Candidate": [c["name"] for c in ranking],
        "Score": [c["score"] for c in ranking]
    })

    fig = px.bar(
        df,
        x="Score",
        y="Candidate",
        orientation="h",
        text="Score",
        title="🏆 Candidate Match Scores"
    )

    fig.update_layout(
        height=350,
        xaxis_title="Match %",
        yaxis_title="",
        template="plotly_dark"
    )

    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")

    st.plotly_chart(fig, use_container_width=True)