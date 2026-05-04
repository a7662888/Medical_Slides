# iPad Codex and GitHub Collaboration Workflow

## Purpose

This repository is designed so iPad Codex can work through GitHub without relying on local files stored only on one computer. GitHub is the source of truth; the Google Drive folder is a local synchronized working copy.

## Recommended Pattern

1. Create or select the GitHub repository in Codex.
2. Ask Codex to make one focused change per task.
3. Review the changed files in Codex or GitHub.
4. Commit changes with a clear message.
5. Push to GitHub so the iPad Codex environment can open the same repo.

## Repo Naming Plan

Use separate repositories when the data, audience, or release cycle differs:

- `dementia-ai-research`: core dementia, MCI, MCR, AD-MCI, PD-MCI research
- `clinical-ai-toolkit`: reusable cleaning, statistics, plotting, and ML utilities
- `nhia-drug-query-system`: NHIA medication query app and database
- `biomarker-analysis-pipeline`: plasma biomarker and assay analysis
- `gait-cognition-analysis`: gait, TUG, and dual-task cognition analysis
- `literature-review-agent`: PubMed, PRISMA, extraction, and evidence grading workflows
- `dementia-social-prescription`: workflow, matching, tracking, and policy documents
- `medical-slide-generator`: medical slide and lecture generation tools

## Suggested Codex Task Format

Use this structure when asking Codex from iPad:

```text
Repo: dementia-ai-research
Goal: Check duplicate IDs and missing cognitive scores.
Scope: src/dementia_ai_research/preprocessing and notebooks only.
Output: Explain changed files, tests run, and remaining risks.
Constraints: Do not touch raw data or commit identifiable patient data.
```

## Data Safety Rules

- Keep identifiable clinical data outside GitHub.
- Commit only code, templates, dictionaries, synthetic examples, aggregate tables, and manuscript text.
- Use `.gitignore` to block raw datasets and credentials.
- Prefer de-identified variable names and participant IDs in examples.

## GitHub Setup Note

For Codex iPad repository selection, the repository must already exist on GitHub and Codex must have repository access. If a repo does not appear in Codex, confirm that the GitHub organization/account is selected and that the Codex GitHub app has permission to that repository.
