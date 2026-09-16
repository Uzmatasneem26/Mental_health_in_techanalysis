import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.title("📈 Interactive EDA Dashboard")

st.markdown(
    """
    Explore relationships between demographics, workplace conditions,
    and mental-health-related survey responses using interactive filters.
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
# HELPER FUNCTIONS
# =========================================================

def clean_label(column_name):
    """Convert column name into readable text."""
    return column_name.replace("_", " ").title()


def cramers_v(x, y):
    """
    Calculate Cramér's V for two categorical variables.
    """

    table = pd.crosstab(x, y)

    if table.empty:
        return np.nan

    observed = table.values

    # Calculate expected values
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    total = observed.sum()

    expected = np.outer(row_totals, col_totals) / total

    # Avoid division by zero
    expected = np.where(expected == 0, 1e-10, expected)

    chi2 = ((observed - expected) ** 2 / expected).sum()

    n = observed.sum()

    if n == 0:
        return np.nan

    phi2 = chi2 / n

    rows, cols = observed.shape

    # Bias correction
    phi2corr = max(
        0,
        phi2 - ((cols - 1) * (rows - 1)) / (n - 1)
    )

    rcorr = rows - (
        ((rows - 1) ** 2) / (n - 1)
    )

    kcorr = cols - (
        ((cols - 1) ** 2) / (n - 1)
    )

    denominator = min(
        (kcorr - 1),
        (rcorr - 1)
    )

    if denominator <= 0:
        return np.nan

    return np.sqrt(phi2corr / denominator)


def association_strength(value):
    """Interpret Cramér's V."""
    
    if pd.isna(value):
        return "Not available"

    if value < 0.10:
        return "Very weak"

    elif value < 0.20:
        return "Weak"

    elif value < 0.40:
        return "Moderate"

    elif value < 0.60:
        return "Strong"

    else:
        return "Very strong"


# =========================================================
# IDENTIFY VARIABLES
# =========================================================

categorical_columns = df.select_dtypes(
    include=["object", "string", "category"]
).columns.tolist()

# Only use categorical variables with manageable number of categories
eda_categorical_columns = [
    col
    for col in categorical_columns
    if 2 <= df[col].nunique(dropna=True) <= 20
]

# Numeric variables
numeric_columns = df.select_dtypes(
    include=np.number
).columns.tolist()

# Remove Age from numeric analysis
numeric_analysis_columns = [
    col
    for col in numeric_columns
    if col.lower() not in ["age", "id", "unnamed: 0"]
]


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🎛️ Dashboard Filters")

filtered_df = df.copy()

# Country filter
country_columns = [
    col for col in df.columns
    if col.lower() == "country"
]

if country_columns:

    country_col = country_columns[0]

    countries = sorted(
        df[country_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_countries = st.sidebar.multiselect(
        "🌍 Country",
        countries,
        default=[]
    )

    if selected_countries:
        filtered_df = filtered_df[
            filtered_df[country_col]
            .astype(str)
            .isin(selected_countries)
        ]


# Treatment filter
treatment_columns = [
    col
    for col in df.columns
    if col.lower() == "treatment"
]

if treatment_columns:

    treatment_col = treatment_columns[0]

    treatment_values = sorted(
        df[treatment_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_treatment = st.sidebar.multiselect(
        "🧠 Treatment",
        treatment_values,
        default=[]
    )

    if selected_treatment:
        filtered_df = filtered_df[
            filtered_df[treatment_col]
            .astype(str)
            .isin(selected_treatment)
        ]


# Remote work filter
remote_columns = [
    col
    for col in df.columns
    if col.lower() == "remote_work"
]

if remote_columns:

    remote_col = remote_columns[0]

    remote_values = sorted(
        df[remote_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_remote = st.sidebar.multiselect(
        "🏠 Remote Work",
        remote_values,
        default=[]
    )

    if selected_remote:
        filtered_df = filtered_df[
            filtered_df[remote_col]
            .astype(str)
            .isin(selected_remote)
        ]


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("📊 Key Metrics")

total_records = len(filtered_df)

total_variables = len(filtered_df.columns)

unique_countries = (
    filtered_df[country_columns[0]].nunique()
    if country_columns
    else 0
)

if treatment_columns:

    treatment_col = treatment_columns[0]

    treatment_yes = (
        filtered_df[treatment_col]
        .astype(str)
        .str.lower()
        .eq("yes")
        .sum()
    )

    treatment_rate = (
        treatment_yes / total_records * 100
        if total_records > 0
        else 0
    )

else:

    treatment_rate = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Respondents",
        f"{total_records:,}"
    )

with col2:
    st.metric(
        "📋 Variables",
        f"{total_variables:,}"
    )

with col3:
    st.metric(
        "🌍 Countries",
        f"{unique_countries:,}"
    )

with col4:
    st.metric(
        "🧠 Treatment Rate",
        f"{treatment_rate:.1f}%"
    )


st.divider()


# =========================================================
# RESPONSE DISTRIBUTION
# =========================================================

st.subheader("📊 Response Distribution")

st.caption(
    "Select a survey question to examine how respondents are distributed "
    "across its response categories."
)

if eda_categorical_columns:

    selected_variable = st.selectbox(
        "Select survey variable",
        eda_categorical_columns,
        format_func=clean_label
    )

    response_counts = (
        filtered_df[selected_variable]
        .dropna()
        .astype(str)
        .value_counts()
        .head(10)
    )

    response_percentage = (
        response_counts /
        response_counts.sum() *
        100
    )

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # COUNT CHART
    # -----------------------------------------------------

    with col1:

        st.markdown("### Response Count")

        fig, ax = plt.subplots(figsize=(8, 5))

        response_counts.sort_values().plot(
            kind="barh",
            ax=ax
        )

        ax.set_xlabel("Number of Respondents")
        ax.set_ylabel("")
        ax.set_title(
            f"Distribution of {clean_label(selected_variable)}"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    # -----------------------------------------------------
    # PERCENTAGE CHART
    # -----------------------------------------------------

    with col2:

        st.markdown("### Response Percentage")

        fig, ax = plt.subplots(figsize=(8, 5))

        response_percentage.sort_values().plot(
            kind="barh",
            ax=ax
        )

        ax.set_xlabel("Percentage (%)")
        ax.set_ylabel("")
        ax.set_title(
            f"Percentage Distribution"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)


st.divider()


# =========================================================
# CROSS-TAB ANALYSIS
# =========================================================

st.subheader("🔍 Mental Health & Workplace Comparison")

st.caption(
    "Compare two categorical survey variables using a percentage-based "
    "cross-tabulation."
)

if len(eda_categorical_columns) >= 2:

    col1, col2 = st.columns(2)

    with col1:

        variable_1 = st.selectbox(
            "Select first variable",
            eda_categorical_columns,
            format_func=clean_label,
            key="cross_variable_1"
        )

    with col2:

        variable_2 = st.selectbox(
            "Select second variable",
            eda_categorical_columns,
            format_func=clean_label,
            key="cross_variable_2"
        )

    if variable_1 != variable_2:

        crosstab = pd.crosstab(
            filtered_df[variable_1],
            filtered_df[variable_2],
            normalize="index"
        ) * 100

        crosstab = crosstab.round(1)

        st.markdown(
            f"### {clean_label(variable_1)} vs "
            f"{clean_label(variable_2)}"
        )

        st.dataframe(
            crosstab.style.format("{:.1f}%"),
            use_container_width=True
        )

        # -------------------------------------------------
        # HEATMAP
        # -------------------------------------------------

        st.markdown("### 🔥 Response Relationship Heatmap")

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        im = ax.imshow(
            crosstab.values,
            aspect="auto"
        )

        ax.set_xticks(
            range(len(crosstab.columns))
        )

        ax.set_xticklabels(
            crosstab.columns,
            rotation=45,
            ha="right"
        )

        ax.set_yticks(
            range(len(crosstab.index))
        )

        ax.set_yticklabels(
            crosstab.index
        )

        ax.set_xlabel(
            clean_label(variable_2)
        )

        ax.set_ylabel(
            clean_label(variable_1)
        )

        ax.set_title(
            "Percentage Distribution"
        )

        # Add values inside heatmap
        for i in range(len(crosstab.index)):

            for j in range(len(crosstab.columns)):

                ax.text(
                    j,
                    i,
                    f"{crosstab.iloc[i, j]:.1f}%",
                    ha="center",
                    va="center"
                )

        plt.colorbar(
            im,
            ax=ax,
            label="Percentage"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)


st.divider()


# =========================================================
# ASSOCIATION ANALYSIS
# =========================================================

st.subheader("📐 Categorical Association Analysis")

st.caption(
    "Cramér's V measures the strength of association between two "
    "categorical variables. It does not imply causation."
)

if len(eda_categorical_columns) >= 2:

    col1, col2 = st.columns(2)

    with col1:

        association_var_1 = st.selectbox(
            "Variable 1",
            eda_categorical_columns,
            format_func=clean_label,
            key="association_var_1"
        )

    with col2:

        association_var_2 = st.selectbox(
            "Variable 2",
            eda_categorical_columns,
            format_func=clean_label,
            key="association_var_2"
        )

    if association_var_1 != association_var_2:

        valid_data = filtered_df[
            [
                association_var_1,
                association_var_2
            ]
        ].dropna()

        if len(valid_data) > 0:

            cramers_value = cramers_v(
                valid_data[association_var_1],
                valid_data[association_var_2]
            )

            strength = association_strength(
                cramers_value
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Cramér's V",
                    f"{cramers_value:.3f}"
                )

            with col2:

                st.metric(
                    "Association",
                    strength
                )

            with col3:

                st.metric(
                    "Valid Responses",
                    f"{len(valid_data):,}"
                )

            st.info(
                "Cramér's V ranges from 0 to 1. Higher values indicate "
                "a stronger statistical association between the selected "
                "categorical variables."
            )


st.divider()


# =========================================================
# NUMERIC CORRELATION
# =========================================================

st.subheader("🔢 Numeric Relationship Analysis")

if len(numeric_analysis_columns) >= 2:

    st.caption(
        "Numeric correlation is shown only when the dataset contains "
        "multiple meaningful numeric variables. Demographic Age is "
        "excluded from this analysis."
    )

    numeric_corr = filtered_df[
        numeric_analysis_columns
    ].corr()

    st.dataframe(
        numeric_corr.round(2),
        use_container_width=True
    )

else:

    st.info(
        "This survey is primarily categorical. There are not enough "
        "meaningful numeric variables for a useful numeric correlation "
        "analysis. Age is intentionally excluded because it is better "
        "handled in the Demographics section."
    )


st.divider()


# =========================================================
# FILTERED DATA
# =========================================================

st.subheader("📋 Filtered Dataset")

st.write(
    f"Showing **{len(filtered_df):,}** records "
    f"out of **{len(df):,}** total records."
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)


# =========================================================
# DOWNLOAD
# =========================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="mental_health_filtered_data.csv",
    mime="text/csv"
)