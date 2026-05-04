# Methods Template

## Study Design and Participants

This study used a de-identified clinical research dataset of participants evaluated for dementia, mild cognitive impairment, motoric cognitive risk syndrome, Alzheimer's disease-related cognitive impairment, or Parkinson's disease-related cognitive impairment. Eligibility criteria, recruitment source, study period, and IRB approval details should be specified here.

## Clinical and Cognitive Measures

Core demographic variables included age, sex, and years of education. Cognitive measures may include MMSE, MoCA, CDR global score, domain-specific neuropsychological tests, and clinician-assigned diagnostic groups. Diagnostic group definitions should be stated explicitly and kept consistent with `data_dictionary/data_dictionary_template.csv`.

## Data Preprocessing

Data preprocessing was performed using a reproducible Python workflow. The pipeline standardized missing values, coerced expected numeric variables, normalized categorical labels, flagged duplicate participant identifiers, and identified records with missing cognitive score information. Row exclusion was not performed automatically; exclusion criteria were applied and reported explicitly during analysis.

## Statistical Analysis

Descriptive statistics were summarized by diagnostic group. Continuous variables were reported as mean with standard deviation or median with interquartile range, depending on distribution. Categorical variables were reported as counts and percentages. Between-group comparisons used appropriate parametric or non-parametric tests, with adjustment for clinically relevant covariates when indicated.

## Machine Learning Analysis

Prediction models were developed using predefined predictors and outcomes. Data splitting, cross-validation, feature preprocessing, class imbalance handling, model selection, and performance metrics should be described before reporting results. Leakage checks should confirm that participant-level identifiers and post-outcome variables were excluded from model training.

## Reporting

Methods and results should be aligned with the target journal requirements, such as Alzheimer's Research & Therapy or Neurology. Include transparent reporting of missing data, diagnostic definitions, model validation, sensitivity analyses, and limitations.
