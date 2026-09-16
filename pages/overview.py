import streamlit as st
import pandas as pd


# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = pd.read_csv("data/survey_cleaned.csv")


# --------------------------------------------------
# Page
# --------------------------------------------------

st.title("📊 Overview Dashboard")

st.markdown(
    "High-level summary of the Mental Health in Tech Survey."
)

st.divider()


# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Respondents",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Total Variables",
        len(df.columns)
    )

with col3:
    st.metric(
        "Countries",
        df["country"].nunique()
        if "country" in df.columns else "N/A"
    )

with col4:
    st.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )


st.divider()


# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

st.subheader("📋 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Rows:**", df.shape[0])
    st.write("**Columns:**", df.shape[1])

with col2:
    st.write(
        "**Duplicate Rows:**",
        df.duplicated().sum()
    )
    st.write(
        "**Memory Usage:**",
        f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB"
    )


# --------------------------------------------------
# Preview
# --------------------------------------------------

st.subheader("🔎 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)