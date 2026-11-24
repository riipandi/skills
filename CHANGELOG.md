# Changelog

## 0.1.0

First release. Forked from Clarity 0.2.1 and merged with Humanizer 4.0.0, Stop Slop, and
`bahasa-indonesia-plain`.

- Kept Clarity's four modes and their mode words: co-write, rewrite, review, lint.
- Added a language policy: chat follows the user's language, artifacts are English.
- Added `references/patterns.md`, a tiered catalog merging the Humanizer and Stop Slop lists.
- Added a hard rule against em and en dashes unless the author's sample uses them.
- Added `references/indonesian.md` for Indonesian chat replies, drafts, and UI copy.
- Added file and embedded return modes to rewrite.
- Left out numeric scoring from Stop Slop. RASA is used as questions, not scores.
- Left out upstream Clarity's slash commands, evals, samples, and site.
- Added `scripts/package_skill.py` to pack the skill into `dist/clarity.skill`.
- Added a rumdl configuration for formatting and linting the Markdown files.
- Indonesian chat sessions: `references/indonesian.md` now governs every chat reply, not only writing tasks.
- Added a Claude Code `SessionStart` hook that applies the language rules from the first message.
- Added a Codex plugin manifest so Codex installs the skill and runs the same `SessionStart` hook.
- Added a pi extension that adds the language rules to the system prompt.
- Added `scripts/check.sh`: rumdl, ruff, oxlint, oxfmt, shellcheck, and shfmt in one command.
