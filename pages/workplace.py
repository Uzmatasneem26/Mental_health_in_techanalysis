import streamlit as st
import pandas as pd


df = pd.read_csv("data/survey_cleaned.csv")

st.title("🏢 Workplace Analysis")

st.markdown(
    """
    Explore workplace characteristics and employee experiences
    related to mental health.
    """
)

st.divider()


# --------------------------------------------------
# Company Size
# --------------------------------------------------

if "no_employees" in df.columns:

    st.subheader("Company Size")

    company_size = df["no_employees"].value_counts()

    st.bar_chart(company_size)


# --------------------------------------------------
# Remote Work
# --------------------------------------------------

if "remote_work" in df.columns:

    st.subheader("Remote Work")

    remote = df["remote_work"].value_counts()

    st.bar_chart(remote)


# --------------------------------------------------
# Benefits
# --------------------------------------------------

if "benefits" in df.columns:

    st.subheader("Mental Health Benefits")

    benefits = df["benefits"].value_counts()

    st.bar_chart(benefits)


# --------------------------------------------------
# Supervisor
# --------------------------------------------------

if "supervisor" in df.columns:

    st.subheader("Supervisor Support")

    supervisor = df["supervisor"].value_counts()

    st.bar_chart(supervisor)