# GitHub Remote Setup

## Current Local State

The local repository has been initialized and committed.

- Local path: `F:\我的雲端硬碟\secondbrain (1)\Codex\dementia-ai-research`
- Intended GitHub repo: `a7662888/dementia-ai-research`
- Remote URL: `https://github.com/a7662888/dementia-ai-research.git`
- Default branch: `main`

## One-Time GitHub Step

Create an empty GitHub repository named:

```text
dementia-ai-research
```

Recommended settings:

- Owner: `a7662888`
- Visibility: private unless all committed content is intended to be public
- Do not add README, `.gitignore`, or license on GitHub, because this local repo already has them

## Push After Repo Exists

From this repository folder, run:

```powershell
git push -u origin main
```

After the push succeeds, the repository should appear in Codex iPad under the GitHub account `a7662888`, assuming Codex has permission to access it.

## If It Does Not Appear in Codex

Open Codex repository access settings and confirm that the GitHub app has access to `dementia-ai-research`. Some GitHub app installations only grant access to selected repositories.
