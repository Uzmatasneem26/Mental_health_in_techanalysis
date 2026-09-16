import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE TITLE
# =========================================================

st.title("👥 Demographics Analysis")

st.markdown(
    """
    Explore the demographic characteristics of respondents,
    including gender, age, and country distribution.
    """
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/survey_cleaned.csv")


df = load_data()

# =========================================================
# HELPER
# =========================================================

def find_column(name):
    """Find a column ignoring capitalization and spaces."""
    for col in df.columns:
        if col.lower().strip() == name.lower().strip():
            return col
    return None


gender_col = find_column("gender")
age_col = find_column("age")
country_col = find_column("country")


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("📊 Demographic Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Respondents",
        f"{len(df):,}"
    )

with col2:
    if gender_col:
        st.metric(
            "Gender Categories",
            df[gender_col].nunique()
        )
    else:
        st.metric("Gender Categories", "N/A")

with col3:
    if age_col:
        age_numeric = pd.to_numeric(
            df[age_col],
            errors="coerce"
        )

        st.metric(
            "Average Age",
            f"{age_numeric.mean():.0f}"
            if age_numeric.notna().any()
            else "N/A"
        )
    else:
        st.metric("Average Age", "N/A")

with col4:
    if country_col:
        st.metric(
            "Countries",
            df[country_col].nunique()
        )
    else:
        st.metric("Countries", "N/A")


st.divider()


# =========================================================
# GENDER DISTRIBUTION
# =========================================================

st.subheader("👤 Gender Distribution")

if gender_col:

    gender_data = (
        df[gender_col]
        .dropna()
        .astype(str)
        .str.strip()
    )

    # Group very small / unusual categories
    gender_counts = gender_data.value_counts()

    # Keep major categories and combine tiny categories
    threshold = 0.02 * len(gender_data)

    major_categories = gender_counts[
        gender_counts >= threshold
    ]

    minor_count = gender_counts[
        gender_counts < threshold
    ].sum()

    if minor_count > 0:
        gender_counts = pd.concat([
            major_categories,
            pd.Series(
                {"Other": minor_count}
            )
        ])

    # Sort for cleaner chart
    gender_counts = gender_counts.sort_values(
        ascending=True
    )

    total_gender = gender_counts.sum()

    gender_percentage = (
        gender_counts / total_gender * 100
    )

    col1, col2 = st.columns(
        [1.15, 1]
    )

    # -----------------------------
    # BAR CHART
    # -----------------------------

    with col1:

        st.markdown("### Respondents by Gender")

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        bars = ax.barh(
            gender_counts.index,
            gender_counts.values
        )

        ax.set_xlabel(
            "Number of Respondents"
        )

        ax.set_ylabel("")

        ax.set_title(
            "Gender Distribution"
        )

        # Add values to bars
        for bar, value in zip(
            bars,
            gender_counts.values
        ):

            ax.text(
                bar.get_width()
                + max(gender_counts.values) * 0.01,
                bar.get_y()
                + bar.get_height() / 2,
                f"{value:,}",
                va="center",
                fontsize=10
            )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(
            axis="x",
            alpha=0.2
        )

        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # -----------------------------
    # PERCENTAGE TABLE
    # -----------------------------

    with col2:

        st.markdown("### Gender Percentage")

        gender_table = pd.DataFrame({
            "Gender": gender_counts.index,
            "Respondents": gender_counts.values,
            "Percentage": gender_percentage.values
        })

        gender_table["Percentage"] = (
            gender_table["Percentage"]
            .round(1)
            .astype(str)
            + "%"
        )

        st.dataframe(
            gender_table,
            hide_index=True,
            use_container_width=True,
            height=250
        )

        st.info(
            "The chart groups very small gender categories "
            "into 'Other' to keep the visualization readable."
        )

else:

    st.warning(
        "Gender column was not found in the dataset."
    )


st.divider()


# =========================================================
# AGE DISTRIBUTION
# =========================================================

st.subheader("🎂 Age Distribution")

if age_col:

    age_data = pd.to_numeric(
        df[age_col],
        errors="coerce"
    )

    # Remove invalid ages
    age_data = age_data[
        (age_data >= 18) &
        (age_data <= 80)
    ].dropna()

    if len(age_data) > 0:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Minimum Age",
                f"{age_data.min():.0f}"
            )

        with col2:
            st.metric(
                "Average Age",
                f"{age_data.mean():.1f}"
            )

        with col3:
            st.metric(
                "Maximum Age",
                f"{age_data.max():.0f}"
            )


        st.markdown(
            "### Respondent Age Groups"
        )

        # -------------------------------------------------
        # AGE GROUPS
        # -------------------------------------------------

        age_bins = [
            17,
            24,
            34,
            44,
            54,
            64,
            100
        ]

        age_labels = [
            "18–24",
            "25–34",
            "35–44",
            "45–54",
            "55–64",
            "65+"
        ]

        age_groups = pd.cut(
            age_data,
            bins=age_bins,
            labels=age_labels
        )

        age_group_counts = (
            age_groups
            .value_counts()
            .sort_index()
        )

        # -------------------------------------------------
        # AGE GROUP BAR CHART
        # -------------------------------------------------

        fig, ax = plt.subplots(
            figsize=(11, 5)
        )

        bars = ax.bar(
            age_group_counts.index.astype(str),
            age_group_counts.values
        )

        ax.set_xlabel(
            "Age Group"
        )

        ax.set_ylabel(
            "Number of Respondents"
        )

        ax.set_title(
            "Respondents by Age Group"
        )

        # Add values above bars
        for bar, value in zip(
            bars,
            age_group_counts.values
        ):

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                bar.get_height()
                + max(age_group_counts.values) * 0.01,
                f"{value:,}",
                ha="center",
                va="bottom",
                fontsize=10
            )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.grid(
            axis="y",
            alpha=0.2
        )

        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


        # -------------------------------------------------
        # AGE SUMMARY TABLE
        # -------------------------------------------------

        age_percentage = (
            age_group_counts
            / age_group_counts.sum()
            * 100
        )

        age_table = pd.DataFrame({
            "Age Group":
                age_group_counts.index.astype(str),

            "Respondents":
                age_group_counts.values,

            "Percentage":
                age_percentage.round(1)
        })

        age_table["Percentage"] = (
            age_table["Percentage"]
            .astype(str)
            + "%"
        )

        st.markdown(
            "### Age Group Summary"
        )

        st.dataframe(
            age_table,
            hide_index=True,
            use_container_width=True
        )

    else:

        st.warning(
            "No valid age values were found."
        )

else:

    st.warning(
        "Age column was not found in the dataset."
    )


st.divider()


# =========================================================
# COUNTRY DISTRIBUTION
# =========================================================

st.subheader("🌍 Respondents by Country")

if country_col:

    country_counts = (
        df[country_col]
        .dropna()
        .astype(str)
        .value_counts()
        .head(15)
        .sort_values()
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    bars = ax.barh(
        country_counts.index,
        country_counts.values
    )

    ax.set_xlabel(
        "Number of Respondents"
    )

    ax.set_ylabel("")

    ax.set_title(
        "Top 15 Countries by Respondents"
    )

    for bar, value in zip(
        bars,
        country_counts.values
    ):

        ax.text(
            bar.get_width()
            + max(country_counts.values) * 0.01,
            bar.get_y()
            + bar.get_height() / 2,
            f"{value:,}",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(
        axis="x",
        alpha=0.2
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

else:

    st.warning(
        "Country column was not found in the dataset."
    )


# =========================================================
# DATA QUALITY NOTE
# =========================================================

st.divider()

st.caption(
    "Age analysis uses respondents aged 18–80 to remove clearly "
    "invalid or unrealistic values from the visualization."
)