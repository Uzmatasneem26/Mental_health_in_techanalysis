import streamlit as st


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mental Health in Tech",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Navigation
# --------------------------------------------------

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠"
)

overview = st.Page(
    "pages/overview.py",
    title="Overview Dashboard",
    icon="📊"
)

demographics = st.Page(
    "pages/demographics.py",
    title="Demographics",
    icon="👥"
)

mental_health = st.Page(
    "pages/mental_health.py",
    title="Mental Health Analysis",
    icon="🧠"
)

workplace = st.Page(
    "pages/workplace.py",
    title="Workplace Analysis",
    icon="🏢"
)

work_factors = st.Page(
    "pages/work_factors.py",
    title="Mental Health & Work Factors",
    icon="🔍"
)

interactive_eda = st.Page(
    "pages/interactive_eda.py",
    title="Interactive EDA",
    icon="📈"
)

raw_data = st.Page(
    "pages/raw_data.py",
    title="Raw Data",
    icon="📋"
)

about = st.Page(
    "pages/about.py",
    title="About Project",
    icon="ℹ️"
)


# --------------------------------------------------
# Navigation Structure
# --------------------------------------------------

pg = st.navigation(
    {
        "Mental Health in Tech": [
            home,
            overview,
            demographics,
            mental_health,
            workplace,
            work_factors,
            interactive_eda,
            raw_data,
            about
        ]
    }
)


# --------------------------------------------------
# Run Selected Page
# --------------------------------------------------

pg.run()