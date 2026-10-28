# clip.grid Ansible collection

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

## Conventions

- This is a **collection** repository (not a playbook/ops or execution-environment repo); apply collection-shaped guidance.
- Use FQCN for all modules (`ansible.builtin.copy:`, not `copy:`); every task needs a clear `name:`; use handlers for service restarts triggered by config changes; never hardcode secrets (use Ansible Vault or an external secrets lookup).
- Role variables are prefixed with the role name (e.g. `grid_enable_fetch_crl`, `grid_host_certificate`, `grid_node_type`) and role behavior branches heavily on these flags/`when:` conditions in `tasks/main.yml` — read the full task chain before assuming a feature is unconditional.
- `galaxy.yml` / `meta/runtime.yml` define the collection's Galaxy metadata and minimum supported Ansible version (`>=2.15.0`); bump `galaxy.yml`'s `version` for any release.
- When writing RFC or infrastructure documentation for changes here, prioritise reading playbooks, roles, and inventory files for technical detail.

## File structure

- Molecule test fixtures are centralized in `extensions/molecule/` rather than duplicated per role: a shared `inventory/` (with a `containers.yml` group), a shared `config.yml`, and one scenario directory per role (`cvmfs/`, `eosxd/`, `grid/`, `htcondor_ce/`) plus a bare `default/` scenario. When adding a new role or scenario, follow this shared-fixture pattern instead of adding a `molecule/` directory inside the role.
- CI (`.github/workflows/ci.yml`) delegates entirely to the org-wide reusable workflow `vbc-it/github-action-workflows`, running on a self-hosted runner, and publishes to Automation Hub on success — this repo's workflow file itself has no test logic.

<!-- agency:managed:start source=templates/ansible/AGENTS.md.tmpl -->
## Required routing

Pushing, force-pushing, opening or commenting on a PR, merging, releasing, and deploying are external actions. A request to do one is not the confirmation: state the exact command, target, and effect, and wait for a yes before running it.

Use the `vbc-standards` skill before acting on a task.

Use the `vbc-ansible-standards` skill before changing Ansible content.

## Skills

When a task matches one of these, use the skill:

- `ansible-review` — review Ansible changes for safety and best practices
- `ansible-change-plan` — plan Ansible changes by blast radius
- `code-review` — structured audit against organization rules
- `open-pr` — open a PR with conventional format
- `agentgateway-mcp` — query internal metrics, logs, inventory, and fabric state read-only

Use other skills only when their trigger matches the task.
<!-- agency:managed:end -->

## Project-local customization

Keep this repository's actual commands and facts here; organization and domain behavior comes from the agency plugins (`it`, `it-infra`, `it-ansible`), enabled in `.claude/settings.json`. Add a nested `AGENTS.md` only for subtree-specific facts or routing, never to copy agency skill content.
