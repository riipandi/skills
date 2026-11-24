# Agents Instructions

This repo is an agent skill written in Markdown. `SKILL.md` is the prompt agents read. There is no build step.

## Key files

- `SKILL.md` is the source of truth. It holds the language rules, the modes, the safeguards, and
  the routing to `references/`.
- `references/` holds material loaded on demand. Every file there must be routed to from
  `SKILL.md`.
- `scripts/strip_markdown.py` and `scripts/prose_stats.py` come from upstream Clarity, reformatted
  with ruff. Do not change their logic here; pull changes from upstream, then run
  `scripts/check.sh --fix`.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` describe the Claude plugin
  and marketplace. `skills: ["./"]` points the loader at the root `SKILL.md`.
- `.cursor-plugin/plugin.json` describes the Cursor plugin. It has no `skills` path so Cursor
  loads the root `SKILL.md`.
- `package.json` makes the repo a pi package. Do not add a `version` field; pi installs from git.
- `hooks/hooks.json` is the `SessionStart` hook for Claude Code and Codex. It prints
  `hooks/session-start.md` into every session. That file repeats the language rules from
  `SKILL.md`; keep the two in sync.
- `.codex-plugin/plugin.json` describes the Codex plugin. Codex reads the marketplace from
  `.claude-plugin/marketplace.json` and sets `CLAUDE_PLUGIN_ROOT` for the hook command.
- `extensions/language-rules.ts` is the pi extension. It reads `hooks/session-start.md` and adds
  it to the system prompt as a section. Keep it free of dependencies.
- `agents/openai.yaml` holds the display name and default prompt for OpenAI-compatible agents.
- `THIRD_PARTY_NOTICES.md` records what came from each upstream skill.

## Rules for changes

- **Language.** Everything in this repo is written in English. Indonesian appears only as
  examples inside `references/indonesian.md` and `references/language.md`.
- **Mode words.** Keep the four mode rows in `SKILL.md` compatible with upstream Clarity. Add a
  synonym if needed; do not remove one.
- **Precedence.** When sources disagree, the order is: truth and the user's request, the
  author's sample, the medium, then house patterns. Do not add a rule that lets a pattern
  outrank a fact.
- **Tiers.** A new tell goes into an existing pattern in `references/patterns.md` when one
  already implies it. Mark it strong only if a careful writer would rarely do it on purpose.
- **No scores.** Do not add numeric scoring to reviews or lint output.
- **No dashes.** The prompt files follow their own hard rule. The validator fails on an em dash
  or en dash in `SKILL.md`, `README.md`, or `references/`.
- **Version.** Keep the same version in `SKILL.md` under `metadata.version`,
  `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and
  the first `CHANGELOG.md`
  heading.
- **Length.** Every word of `SKILL.md` is read on each use. Put detail in `references/`.
- **Frontmatter.** `SKILL.md` may use only `name`, `description`, `license`, `allowed-tools`,
  `metadata`, and `compatibility`. Any other key makes the `.skill` file invalid.
- **Quality.** Every file must pass `scripts/check.sh`: rumdl for Markdown, ruff for Python,
  oxlint and oxfmt for TypeScript, oxfmt for JSON, YAML, and TOML, shellcheck and shfmt for shell.
  Run `scripts/check.sh --fix` after editing.
- **Checks.** Before publishing, run `scripts/check.sh`, `python3 scripts/package_skill.py`,
  `npx skills add . --list`, and `claude plugin validate .`.
