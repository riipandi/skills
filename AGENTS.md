# Agents Instructions

This repo holds several agent skills written in Markdown and ships them as one plugin named
`riipandi`. Each `skills/<name>/SKILL.md` is a prompt agents read. There is no build step.

## Key files

- `skills/<name>/SKILL.md` is the source of truth for a skill. The folder name and the `name`
  field must match.
- `skills/<name>/references/` holds material loaded on demand. Every file there must be routed
  to from that skill's `SKILL.md`.
- `skills/<name>/agents/openai.yaml` holds the display name and default prompt for
  OpenAI-compatible agents.
- `skills/<name>/evals/` holds test cases in the `claude plugin eval` layout. They are left out
  of the `.skill` file.
- `skills/clarity/scripts/strip_markdown.py` and `prose_stats.py` come from upstream Clarity,
  reformatted with ruff. Do not change their logic here; pull changes from upstream, then run
  `scripts/check.sh --fix`.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` describe the Claude plugin
  and marketplace. `skills` lists every skill folder.
- `.codex-plugin/plugin.json` describes the Codex plugin. Codex reads the marketplace from
  `.claude-plugin/marketplace.json` and sets `CLAUDE_PLUGIN_ROOT` for the hook command.
- `.cursor-plugin/plugin.json` describes the Cursor plugin. It has no `skills` path so Cursor
  loads the `skills/` folder.
- `package.json` makes the repo a pi package. Do not add a `version` field; pi installs from git.
- `skills.sh.json` groups the skills for the Skills CLI.
- `commands/` holds Claude Code slash commands, named `<skill>-<mode>.md`
  (`/riipandi:clarity-review`). Their `description` and `argument-hint` are what the slash menu
  shows.
- `hooks/hooks.json` wires `hooks/hook.sh` to `SessionStart` and `UserPromptSubmit` for Claude
  Code and Codex. `hook.sh` prints `hooks/clarity-language-rules.md` and, unless the prompt
  optimizer is off, `hooks/prompt-optimizer-rules.md`. It also handles
  `/prompt-optimizer on|off|status`.
- `hooks/*-rules.md` repeat the always-on rules from the matching `SKILL.md`. Keep each pair in
  sync.
- `extensions/session-rules.ts` is the pi extension. It adds the same rule files to the system
  prompt and reads the same state file. Keep it free of dependencies.
- `THIRD_PARTY_NOTICES.md` records what came from each upstream source.

## Adding a skill

1. Create `skills/<name>/SKILL.md`, with `references/` and `agents/openai.yaml`.
2. Add the folder to `skills` in `.claude-plugin/plugin.json` and to `pi.skills` in
   `package.json`, and add the name to a group in `skills.sh.json`.
3. Add it to the table in `README.md` and record its sources in `THIRD_PARTY_NOTICES.md`.
4. If it has always-on rules, add `hooks/<name>-rules.md` and print it from `hooks/hook.sh` and
   `extensions/session-rules.ts`.
5. Run `scripts/check.sh --fix` and `python3 scripts/package_skill.py`.

## Rules for changes

- **Language.** Everything in this repo is written in English. Indonesian appears only as
  examples inside `skills/clarity/references/indonesian.md` and `language.md`, and in eval
  fixtures.
- **Independence.** Each skill must work when installed alone. Do not make one skill's
  `SKILL.md` depend on another skill or on the hooks being present.
- **Clarity mode words.** Keep the four mode rows in `skills/clarity/SKILL.md` compatible with
  upstream Clarity. Add a synonym if needed; do not remove one.
- **Precedence in Clarity.** When sources disagree, the order is: truth and the user's request,
  the author's sample, the medium, then house patterns. Do not add a rule that lets a pattern
  outrank a fact.
- **Tiers.** A new tell goes into an existing pattern in `skills/clarity/references/patterns.md`
  when one already implies it. Mark it strong only if a careful writer would rarely do it on
  purpose.
- **No scores.** Do not add numeric scoring to reviews or lint output.
- **No dashes.** The prompt files follow Clarity's hard rule. The validator fails on an em dash
  or en dash in `README.md`, `hooks/*.md`, any `SKILL.md`, or any `references/` file.
- **Prompt optimizer state.** The flag file `~/.config/riipandi-skills/prompt-optimizer-off`
  means off. Absent means on. `hook.sh`, the pi extension, and the skill's own instructions must
  agree on that path and meaning.
- **Always-on rules never widen a request.** A rule printed by the hook may sharpen how a
  message is read. It must not add tasks the user did not ask for.
- **Version.** Keep the same plugin version in `.claude-plugin/plugin.json`,
  `.codex-plugin/plugin.json`, and `.cursor-plugin/plugin.json`. Each skill keeps its own
  `metadata.version` and bumps it when its behavior changes.
- **Changelog.** Head each `CHANGELOG.md` entry with a local timestamp in `YYYYMMDD-HHMM` form,
  for example `## 20261125-0037`, newest first. Get it with `date +%Y%m%d-%H%M`.
- **Length.** Every word of a `SKILL.md` is read on each use, and every word of a
  `hooks/*-rules.md` file is read in every session. Put detail in `references/`.
- **Frontmatter.** A `SKILL.md` may use only `name`, `description`, `license`, `allowed-tools`,
  `metadata`, `compatibility`, and `argument-hint`. Any other key makes the `.skill` file
  invalid. `argument-hint` is what Claude Code shows after the skill name in the slash menu;
  `scripts/package_skill.py` strips it from the packed `.skill` file.
- **Quality.** Every file must pass `scripts/check.sh`: rumdl for Markdown, ruff for Python,
  oxlint and oxfmt for TypeScript, oxfmt for JSON, YAML, and TOML, shellcheck and shfmt for shell.
  Run `scripts/check.sh --fix` after editing.
- **Checks.** Before publishing, run `scripts/check.sh`, `python3 scripts/package_skill.py`,
  `npx skills add . --list`, and `claude plugin validate .`.
