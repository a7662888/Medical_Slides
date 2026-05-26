# Dementia AI Research

This repository contains data processing, feature engineering, statistical analysis, machine learning, and manuscript preparation workflows for dementia, mild cognitive impairment, motoric cognitive risk syndrome, Alzheimer's disease, and Parkinson's disease-related cognitive impairment.

## Core Research Domains

- Dementia and mild cognitive impairment
- Motoric cognitive risk syndrome
- Alzheimer's disease biomarkers
- Parkinson's disease cognitive impairment
- Gait-cognition interaction
- Multimodal clinical prediction models

## Repository Structure

- `data_dictionary/`: variable definitions, coding rules, and data quality checks
- `notebooks/`: exploratory, statistical, and machine learning notebooks
- `src/`: reusable Python package code
- `results/`: output tables and figures for internal review and manuscripts
- `manuscript/`: methods text, analysis notes, and submission-ready drafts
- `docs/`: Codex, GitHub, and collaboration workflow notes
- `tests/`: focused tests for reusable data processing functions

## Initial Workflow

1. Define variables in `data_dictionary/data_dictionary_template.csv`.
2. Place de-identified analysis datasets outside Git or in an approved secure storage location.
3. Implement repeatable cleaning rules in `src/dementia_ai_research/preprocessing/pipeline.py`.
4. Use `notebooks/01_statistical_analysis_template.ipynb` for descriptive and inferential analyses.
5. Use `notebooks/02_machine_learning_template.ipynb` for prediction model development.
6. Draft reproducible methods in `manuscript/methods_template.md`.

## Data Governance

Do not commit patient identifiers, raw clinical datasets, exported hospital records, IRB documents containing identifiable information, or access credentials. Keep the repository focused on code, templates, dictionaries, aggregate outputs, and manuscript text.

## Suggested Codex Tasks

- Check duplicate IDs, missing cognitive scores, and group definitions.
- Generate a data dictionary from a cleaned dataset schema.
- Refactor repeated preprocessing logic into reusable functions.
- Draft methods text for Alzheimer's Research & Therapy or Neurology.
- Review analysis notebooks for reproducibility and leakage risk.

## Public Slide Decks

- [NCMEA 2026 dementia antipsychotic deprescribing interactive deck](public/ncmea-2026-antipsychotic-deprescribing/)
