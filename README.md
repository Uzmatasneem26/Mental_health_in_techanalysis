# 🧠 Mental Health in Tech Survey Dashboard

An interactive **Streamlit dashboard** for exploring the Mental Health in Tech Survey dataset. The project focuses on data cleaning, exploratory data analysis, demographics, workplace factors, and mental-health-related patterns among technology workers.

---

## 📌 Project Overview

Mental health is an important aspect of employee well-being, particularly in the technology industry.

This project uses survey data to explore:

* Demographic characteristics of respondents
* Mental health treatment patterns
* Workplace conditions
* Employer and supervisor support
* Remote work
* Family history of mental health conditions
* Relationships between workplace factors and mental health
* Interactive exploratory data analysis

The project follows a structured workflow where the raw dataset is cleaned separately and the resulting cleaned dataset is used by the Streamlit dashboard.

---

## 🎯 Project Objectives

The main objectives are:

1. Clean and preprocess the survey dataset.
2. Analyze demographic characteristics of respondents.
3. Explore mental health treatment and related responses.
4. Analyze workplace-related factors.
5. Examine relationships between mental health and work factors.
6. Provide interactive exploratory data analysis.
7. Allow users to view and download the cleaned dataset.
8. Present the analysis through an easy-to-use Streamlit dashboard.

---

## 📊 Dashboard Pages

The application contains the following pages:

### 🏠 Home

Provides an introduction to the project and navigation to the different dashboard sections.

### 📊 Overview Dashboard

Provides a high-level summary of the dataset, including:

* Total respondents
* Number of variables
* Number of countries
* Missing values
* Dataset preview

### 👥 Demographics

Explores respondent demographics such as:

* Gender
* Age
* Country
* Other available demographic variables

### 🧠 Mental Health Analysis

Analyzes variables related to:

* Mental health treatment
* Mental health consequences
* Family history
* Mental health awareness
* Other relevant survey responses

### 🏢 Workplace Analysis

Explores workplace-related factors such as:

* Company size
* Remote work
* Mental health benefits
* Supervisor support
* Workplace environment

### 🔍 Mental Health & Work Factors

Examines relationships between mental-health-related responses and workplace factors.

Examples include:

* Treatment vs. remote work
* Treatment vs. company size
* Treatment vs. family history

### 📈 Interactive EDA

Provides interactive exploration of categorical and numerical variables.

Users can select variables and explore their distributions through charts.

### 📋 Raw Data

Displays the cleaned dataset and provides an option to download it as a CSV file.

### ℹ️ About Project

Provides information about the project, objectives, workflow, and technology stack.

---

## 🔄 Project Workflow

```text
Raw Dataset
     │
     ▼
data/survey.csv
     │
     ▼
clean_data.py
     │
     ├── Clean column names
     ├── Remove duplicates
     ├── Handle missing values
     ├── Clean text values
     └── Remove empty columns
     │
     ▼
data/survey_cleaned.csv
     │
     ▼
Streamlit Dashboard
     │
     ├── 🏠 Home
     ├── 📊 Overview Dashboard
     ├── 👥 Demographics
     ├── 🧠 Mental Health Analysis
     ├── 🏢 Workplace Analysis
     ├── 🔍 Mental Health & Work Factors
     ├── 📈 Interactive EDA
     ├── 📋 Raw Data
     └── ℹ️ About Project
```
### Business Problem

 Organizations in the technology industry may have limited visibility into employee mental health, workplace conditions, and the availability or awareness of mental health support. Survey data can contain valuable information, but without proper analysis, it is difficult for HR teams and management to identify patterns and understand which workplace factors are associated with employees' mental health experiences.

The business problem is therefore to analyze employee survey data and convert it into meaningful insights about mental health, workplace factors, and employee support, so organizations can better understand areas that may require attention.


## Business Use Case

* The project analyzes employee survey data to understand mental health conditions and workplace factors in the technology industry. 
* Organizations can use the insights to identify patterns related to mental health, work environment, work-life balance, and employee support.

* The dashboard helps HR teams and management identify areas of concern, understand employee needs, and make data-driven decisions about workplace policies and employee-support initiatives.

## Business Objectives
* Understand employee mental health trends: Analyze the prevalence of mental health challenges among employees.
* Identify workplace factors :Examine how factors such as work interference, remote work,  company size, and workplace support relate to mental health responses.
* Evaluate employee support systems :Understand awareness and availability of mental health benefits and workplace resources.
* Analyze demographic patterns : Explore differences across age, gender, employment characteristics, and other available demographic variables.
* Support HR decision-making: Provide data-driven insights that can help HR teams improve employee-support programs and workplace policies.
* Identify areas requiring attention : Highlight patterns that may indicate where additional awareness, resources, or organizational support could be considered.

---

## 📁 Project Structure

```text
Mental-Health-in-Tech/
│
├── app.py
├── clean_data.py
├── requirements.txt
├── README.md
│
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

---

## 🛠️ Technologies Used

* **Python** – Programming language
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Streamlit** – Interactive dashboard development

---

## 🧹 Data Cleaning

Data preprocessing is handled separately in:

```text
clean_data.py
```

The script performs operations such as:

* Loading the original CSV
* Standardizing column names
* Removing duplicate records
* Handling common missing-value indicators
* Removing completely empty columns
* Cleaning text values
* Handling missing values
* Saving the processed dataset

The cleaned dataset is saved as:

```text
data/survey_cleaned.csv
```

The Streamlit application uses this cleaned dataset instead of performing the cleaning every time the dashboard starts.

---

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Mental-Health-in-Tech
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the data cleaning script

```bash
python clean_data.py
```

This creates:

```text
data/survey_cleaned.csv
```

### 7. Start the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📈 Dashboard Features

The dashboard provides:

* Interactive navigation
* KPI cards
* Data visualizations
* Demographic analysis
* Mental health analysis
* Workplace analysis
* Cross-tabulation analysis
* Interactive EDA
* Cleaned dataset preview
* CSV download functionality

---

## 📋 Dataset

The project uses a survey dataset containing responses related to mental health in the technology workplace.

The raw dataset is stored separately from the cleaned dataset:

```text
data/survey.csv
```

The processed dataset is:

```text
data/survey_cleaned.csv
```

---

## 🔍 Key Analysis Areas

The dashboard focuses on several analytical areas:

### Demographics

Understanding who participated in the survey.

### Mental Health

Exploring treatment, family history, consequences, and other mental-health-related responses.

### Workplace

Examining company characteristics, remote work, benefits, and workplace support.

### Work & Mental Health

Exploring relationships between workplace characteristics and mental-health-related responses.

---

## 🚀 Deployment

The application can be deployed using **Streamlit Community Cloud**.

General deployment steps:

1. Push the project to GitHub.
2. Ensure `app.py` is in the repository root.
3. Ensure `requirements.txt` is included.
4. Make sure `data/survey_cleaned.csv` is included if the app is expected to run directly from the repository.
5. Connect the GitHub repository to Streamlit Community Cloud.
6. Select `app.py` as the main application file.
7. Deploy the application.

---

## ⚠️ Important

Run the cleaning script whenever the original dataset is changed:

```bash
python clean_data.py
```

Then run the dashboard:

```bash
streamlit run app.py
```

This keeps the data-cleaning process separate from the dashboard application.

---

## 📌 Future Improvements

Possible future enhancements include:

* Additional statistical analysis
* Correlation analysis
* More interactive filters
* Advanced visualizations
* Statistical hypothesis testing
* Additional workplace segmentation
* Dashboard-level filtering
* Exportable analysis reports

---

## 👩‍💻 Project Type

**Data Analytics | Exploratory Data Analysis | Data Visualization | Streamlit Dashboard**

---

## ⭐ Author

**Uzma Tasneem**

Data Analytics | Python | SQL | Power BI | Data Visualization

```
```
