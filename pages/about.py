import streamlit as st


st.title("ℹ️ About Project")

st.markdown(
    """
    ## Mental Health in Tech Survey

    ### 📌 Project Overview

    This project analyzes survey data related to mental health
    in the technology workplace.

    ### 🎯 Objectives

    - Understand respondent demographics
    - Analyze mental health treatment patterns
    - Explore workplace conditions
    - Examine relationships between work and mental health
    - Provide interactive exploratory data analysis

    ### 🛠️ Technology Stack

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Streamlit

    ### 🔄 Project Workflow

    **1. Raw Dataset**

    Survey responses are stored in the `data` folder.

    **2. Data Cleaning**

    `clean_data.py` handles preprocessing and creates the
    cleaned dataset.

    **3. Cleaned Dataset**

    The processed data is saved as:

    `data/survey_cleaned.csv`

    **4. Dashboard**

    Streamlit uses the cleaned dataset to generate the
    interactive dashboard.

    ### 📂 Project Structure

    ```
    Mental-Health-in-Tech/
    │
    ├── app.py
    ├── clean_data.py
    ├── data/
    │   ├── survey.csv
    │   └── survey_cleaned.csv
    │
    └── pages/
        ├── home.py
        ├── overview.py
        ├── demographics.py
        ├── mental_health.py
        ├── workplace.py
        ├── work_factors.py
        ├── interactive_eda.py
        ├── raw_data.py
        └── about.py
    ```
    """
)