import streamlit as st
import pandas as pd


df = pd.read_csv("data/survey_cleaned.csv")

st.title("🔍 Mental Health & Work Factors")

st.markdown(
    """
    Explore relationships between workplace characteristics
    and mental-health-related responses.
    """
)

st.divider()


# --------------------------------------------------
# Treatment vs Remote Work
# --------------------------------------------------

if (
    "treatment" in df.columns
    and "remote_work" in df.columns
):

    st.subheader(
        "Mental Health Treatment vs Remote Work"
    )

    table = pd.crosstab(
        df["remote_work"],
        df["treatment"],
        normalize="index"
    ) * 100

    st.dataframe(
        table.round(2),
        use_container_width=True
    )


# --------------------------------------------------
# Treatment vs Company Size
# --------------------------------------------------

if (
    "treatment" in df.columns
    and "no_employees" in df.columns
):

    st.subheader(
        "Mental Health Treatment vs Company Size"
    )

    table = pd.crosstab(
        df["no_employees"],
        df["treatment"],
        normalize="index"
    ) * 100

    st.dataframe(
        table.round(2),
        use_container_width=True
    )


# --------------------------------------------------
# Treatment vs Family History
# --------------------------------------------------

if (
    "treatment" in df.columns
    and "family_history" in df.columns
):

    st.subheader(
        "Mental Health Treatment vs Family History"
    )

    table = pd.crosstab(
        df["family_history"],
        df["treatment"],
        normalize="index"
    ) * 100

    st.dataframe(
        table.round(2),
        use_container_width=True
    )