import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/survey_cleaned.csv")

st.title("🧠 Mental Health Analysis")

st.markdown(
    """
    This page explores survey responses related to mental
    health treatment, awareness, and experiences.
    """
)

st.divider()


# --------------------------------------------------
# Treatment
# --------------------------------------------------

if "treatment" in df.columns:

    st.subheader("Mental Health Treatment")

    treatment_counts = df["treatment"].value_counts()

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(
            treatment_counts,
            use_container_width=True
        )

    with col2:

        fig, ax = plt.subplots()

        ax.bar(
            treatment_counts.index.astype(str),
            treatment_counts.values
        )

        ax.set_xlabel("Treatment")
        ax.set_ylabel("Respondents")

        st.pyplot(fig)


# --------------------------------------------------
# Mental Health Consequence
# --------------------------------------------------

if "mental_health_consequence" in df.columns:

    st.subheader("Mental Health Consequences")

    consequence = (
        df["mental_health_consequence"]
        .value_counts()
    )

    st.bar_chart(consequence)


# --------------------------------------------------
# Family History
# --------------------------------------------------

if "family_history" in df.columns:

    st.subheader("Family History of Mental Health Conditions")

    family_history = df["family_history"].value_counts()

    st.bar_chart(family_history)