# Changelog

Entries are headed by a local timestamp in `YYYYMMDD-HHMM` form, newest first.

## 20261125-0125

- Added an argument hint to both skills, shown in the Claude Code slash menu. The packer strips it
  from `.skill` files, which do not accept the key.

## 20261125-0113

- Renamed the repo to `riipandi/skills` and the plugin to `riipandi`. Skills are now
  `/riipandi:clarity` and `/riipandi:prompt-optimizer`. The marketplace is `riipandi-skills`.
- Moved Clarity to `skills/clarity/`, with its references, lint scripts, and evals.
- Added the `prompt-optimizer` skill, adapted from github/awesome-copilot.
- Added an always-on prompt optimizer through the session hook, with `on`, `off`, and `status`.
- Replaced the `cat` hook with `hooks/hook.sh`, which also handles the toggle.
- Renamed the Clarity commands to `/riipandi:clarity-interview`, `-rewrite`, `-review`, `-lint`.
- `scripts/package_skill.py` now packs every skill into `dist/<name>.skill`.

## 20261125-0101

- Added Claude Code slash commands for each mode, with descriptions and argument hints.
- `/clarity` with nothing to work on now replies with the list of modes.

## 20261125-0047

- Added six eval cases under `evals/` and ran the first with-skill and without-skill comparison.
- Reviews now name patterns in plain words instead of catalog codes, and cap passage findings.
- Reviews are laid out as plain `Label: text` lines, with no bold labels and no code blocks.
- The dash rule now binds only text the skill writes. In a review it is a weak-alone pattern.
- A reason or consequence the user did not state now counts as an invented claim in new documents.

## 20261125-0038

- Added a Codex plugin manifest so Codex installs the skill and runs the same `SessionStart` hook.
- Added a pi extension that adds the language rules to the system prompt.
- Added `scripts/check.sh`: rumdl, ruff, oxlint, oxfmt, shellcheck, and shfmt in one command.
- Changed the changelog headings from version numbers to timestamps.

## 20261125-0030

First release, version 0.1.0. Forked from Clarity 0.2.1 and merged with Humanizer 4.0.0, Stop
Slop, and `bahasa-indonesia-plain`.

- Kept Clarity's four modes and their mode words: co-write, rewrite, review, lint.
- Added a language policy: chat follows the user's language, artifacts are English.
- Added `references/patterns.md`, a tiered catalog merging the Humanizer and Stop Slop lists.
- Added a hard rule against em and en dashes unless the author's sample uses them.
- Added `references/indonesian.md` for Indonesian chat replies, drafts, and UI copy.
- Indonesian chat sessions: `references/indonesian.md` governs every chat reply, not only writing tasks.
- Added file and embedded return modes to rewrite.
- Added a Claude Code `SessionStart` hook that applies the language rules from the first message.
- Added `scripts/package_skill.py` to pack the skill into `dist/clarity.skill`.
- Added a rumdl configuration for formatting and linting the Markdown files.
- Left out numeric scoring from Stop Slop. RASA is used as questions, not scores.
- Left out upstream Clarity's slash commands, evals, samples, and site.
