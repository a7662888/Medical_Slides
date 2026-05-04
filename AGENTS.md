# Codex Instructions for Dementia AI Research

This repository follows the global workspace rules in the parent `AGENTS.md`. The notes below are project-specific additions.

## Project Scope

This repo owns dementia, MCI, MCR, AD-MCI, PD-MCI, gait-cognition, and related neurodegenerative cognitive research workflows.

## Dementia Research Quality Checks

Before finalizing analysis code, check:

- duplicate participant identifiers
- missing or inconsistent cognitive scores
- diagnostic group definitions
- CDR, MMSE, MoCA, neuropsychological domain score handling
- gait-cognition variable naming consistency when gait features are used
- train-test leakage risk
- model features that encode the outcome
- manuscript methods consistency with actual code

## Repository Boundaries

Reusable utilities that benefit multiple projects should eventually move to `clinical-ai-toolkit`.
