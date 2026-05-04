# Codex Instructions for Dementia AI Research

## Working Style

- Keep changes focused on the user's requested analysis or workflow.
- Preserve patient privacy. Never commit raw clinical datasets, identifiable records, credentials, or IRB files with personal information.
- Prefer reproducible Python code over manual spreadsheet transformations.
- Keep exclusion rules explicit and auditable.

## Research Quality Checks

Before finalizing analysis code, check:

- duplicate participant identifiers
- missing or inconsistent cognitive scores
- diagnostic group definitions
- train-test leakage risk
- model features that encode the outcome
- manuscript methods consistency with actual code

## Repository Boundaries

This repo owns dementia research workflows and project-specific notebooks. Reusable utilities that benefit multiple repositories should eventually move to `clinical-ai-toolkit`.
