import streamlit as st
import pandas as pd


df = pd.read_csv("data/survey_cleaned.csv")

st.title("📋 Raw Data")

st.markdown(
    "Explore and download the cleaned survey dataset."
)

st.divider()


# --------------------------------------------------
# Dataset Statistics
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )


# --------------------------------------------------
# Data
# --------------------------------------------------

st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True,
    height=600
)


# --------------------------------------------------
# Download
# --------------------------------------------------

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Cleaned Dataset",
    data=csv,
    file_name="survey_cleaned.csv",
    mime="text/csv"
)