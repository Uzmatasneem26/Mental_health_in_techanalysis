import streamlit as st


st.title("🧠 Mental Health in Tech Survey")

st.markdown(
    """
    ## Welcome to the Mental Health in Tech Dashboard

    This interactive dashboard explores mental health,
    workplace environment, demographics, and work-related
    factors among technology workers.
    """
)

st.divider()

st.subheader("📌 Dashboard Sections")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 📊 Data Analysis

    - 📊 Overview Dashboard
    - 👥 Demographics
    - 🧠 Mental Health Analysis
    - 🏢 Workplace Analysis
    """)

with col2:

    st.markdown("""
    ### 🔍 Advanced Exploration

    - 🔍 Mental Health & Work Factors
    - 📈 Interactive EDA
    - 📋 Raw Data
    - ℹ️ About Project
    """)

st.divider()

st.subheader("🎯 Project Objective")

st.write(
    """
    The objective of this project is to analyze survey responses
    related to mental health in the technology workplace and
    explore patterns across demographics, workplace conditions,
    and mental-health-related factors.
    """
)

st.info(
    "👈 Use the sidebar to navigate through the dashboard."
)