# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`clip.grid` is an Ansible Collection (namespace `clip`, name `grid`) that provisions GRID services for the VBC CERN Tier2 site. It contains five roles, each independently installable via `ansible-galaxy`:

- `roles/cvmfs` — CVMFS fuse mount
- `roles/eosxd` — EOS fusex client
- `roles/grid` — base GRID configuration (IGTF/UMD/WLCG repos, fetch-crl, VOMS, host certificates, UI/WN node setup)
- `roles/htcondor_ce` — HTCondor-CE
- `roles/vobox` — WLCG VOBOX

Each role's `README.md` documents its own variables and dependencies; check the relevant one before changing a role's defaults.

## Environment setup

- Python is pinned via `.python-version` (3.11); dependencies are declared in `pyproject.toml` under `[dependency-groups].dev` (`ansible-core`, `molecule`, `ansible-lint`) and locked in `uv.lock`.
- `.envrc` uses `direnv` + `uv`: entering the directory auto-creates `.venv` and runs `uv sync`. Without direnv, run `uv sync` manually and use `.venv/bin/...` or activate the venv.

## Commands

- Lint: `ansible-lint` (also run via pre-commit; config combines `ansible-lint`, `black`, `shellcheck`, and standard `pre-commit-hooks`)
- Syntax check a playbook: `ansible-playbook --syntax-check <playbook>.yml`
- Dry run with diff: `ansible-playbook -C <playbook>.yml --diff`
- Run all pre-commit hooks: `pre-commit run --all-files`
- Molecule scenarios live under `extensions/molecule/<role>/`, **not** the default `roles/<role>/molecule/` layout, and share common settings from `extensions/molecule/config.yml` (custom inventory path, `ANSIBLE_ROLES_PATH`, and the Galaxy dependency file `tests/requirements.yml`). Point molecule at that base config when running locally (e.g. `--base-config extensions/molecule/config.yml` or an equivalent `MOLECULE_GLOB`); see the reusable CI workflow (`vbc-it/github-action-workflows/.github/workflows/ansible-collection.yml`, referenced from `.github/workflows/ci.yml`) for the exact invocation used in CI.
- Run `ansible-lint` before every commit.

## Architecture notes

- Molecule test fixtures are centralized in `extensions/molecule/` rather than duplicated per role: a shared `inventory/` (with a `containers.yml` group), a shared `config.yml`, and one scenario directory per role (`cvmfs/`, `eosxd/`, `grid/`, `htcondor_ce/`) plus a bare `default/` scenario. When adding a new role or scenario, follow this shared-fixture pattern instead of adding a `molecule/` directory inside the role.
- Role variables are prefixed with the role name (e.g. `grid_enable_fetch_crl`, `grid_host_certificate`, `grid_node_type`) and role behavior branches heavily on these flags/`when:` conditions in `tasks/main.yml` — read the full task chain before assuming a feature is unconditional.
- CI (`.github/workflows/ci.yml`) delegates entirely to the org-wide reusable workflow `vbc-it/github-action-workflows`, running on a self-hosted runner, and publishes to Automation Hub on success — this repo's workflow file itself has no test logic.
- `galaxy.yml` / `meta/runtime.yml` define the collection's Galaxy metadata and minimum supported Ansible version (`>=2.15.0`); bump `galaxy.yml`'s `version` for any release.

## Agency-managed conventions

This repository's coding standards, security policy, git conventions, and Ansible-specific rules are centrally maintained in the [agency](https://github.com/vbc-it/agency) framework, mounted as a git submodule at `.agency/` (see `AGENTS.md`). For Claude Code specifically:

- Agent definition: `@.agency/agents/stack/ansible-coder.md`
- Subagents: `.claude/agents/ansible-reviewer.md` (proactive review after Ansible changes) and `.claude/agents/infra-docs-writer.md` (RFC/Confluence documentation)
- Imported rules: `@.agency/rules/global/coding-standards.md`, `@.agency/rules/global/security-policy.md`, `@.agency/rules/global/git-conventions.md`, `@.agency/rules/global/ci-cd.md`, `@.agency/rules/global/organization-context.md`, `@.agency/rules/global/agent-behavior.md`, `@.agency/rules/team/ansible/index.md`
- Key conventions from those rules: use FQCN for all modules (`ansible.builtin.copy:`, not `copy:`), every task needs a clear `name:`, use handlers for service restarts triggered by config changes, never hardcode secrets (use Ansible Vault or an external secrets lookup), and treat this repo as a **collection** (not a playbook/ops or execution-environment repo) when applying repo-shape-specific guidance.
- The `.agency` submodule is centrally updated; do not update it automatically — use its `check-agency-update` skill and get explicit confirmation first (see `.agency/skills/tactical/agency-bootstrap/SKILL.md`).

Do not overwrite `AGENTS.md`, `.github/instructions/*.instructions.md`, or `opencode.json` — they wire the same agency rules into GitHub Copilot and OpenCode and should stay in sync with the Claude Code config above.
