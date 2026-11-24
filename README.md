# Clarity

An agent skill for drafting, rewriting, and reviewing prose so it is specific, useful, and
recognizably the author's, without inventing facts or performing humanness.

This is a personal fork of [Clarity](https://github.com/addyosmani/clarity) by Addy Osmani. It
keeps Clarity's modes and safeguards and merges in three other skills:

| Source | What this skill takes from it |
|---|---|
| [addyosmani/clarity](https://github.com/addyosmani/clarity) | The base: four modes, shared safeguards, the editing order, the interview, the review format, the lint scripts |
| [blader/humanizer](https://github.com/blader/humanizer) | The pattern catalog, the strong and weak-alone tiers, the dash rule, file and embedded return modes |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | Phrase and structure watch lists, folded into the tiers instead of applied as bans |
| [bahasa-indonesia-plain](https://gist.github.com/orepras/3e1ca8974fc51d11825f142fa6a66635) | Plain Indonesian, EYD conventions, UI copy guidance, the RASA quality lens |

## Why a fork

I chat with agents in Indonesian and ship work in English. The four skills above each solve
part of that, and they disagree with each other in places. This skill settles the
disagreements once:

- **Chat follows the user's language.** Replies, questions, and review findings use the
  language I am writing in.
- **Artifacts are English.** Files, documentation, reports, code comments, commit messages,
  pull requests, issues, and drafted messages are written in English, even when the chat is
  not. The exceptions are an artifact I name a language for, and content whose language the
  product fixes, such as a locale file.
- **Truth outranks polish.** Clarity's rule wins over Humanizer's: the skill never adds a
  detail from its own knowledge. It asks, or leaves `[TK: question]`.
- **Patterns are tiered, not banned.** Strong tells are edited on one sighting. Weak ones
  (passive voice, adverbs, triads) are edited only in clusters or when they hide the meaning.
- **No dashes.** Final text has no em dash or en dash unless my own writing sample uses them.
- **No scores.** Reviews report findings in words. RASA is four questions, not four numbers.

## Installation

Once installed, run it with `/clarity`.

This skill uses the same name as the original Clarity. Remove the original first if you have
it installed, or the two will collide.

### Claude Code

```text
/plugin marketplace add riipandi/skill-clarity
/plugin install clarity@riipandi-clarity
```

The plugin also installs a `SessionStart` hook. It puts the language rules into every session
from the first message, so chat replies in Indonesian follow them before the skill itself is
loaded. Codex and pi get the same rules through their own mechanisms, described below.

### Codex

Install it as a plugin to get the skill and the `SessionStart` hook:

```bash
codex plugin marketplace add riipandi/skill-clarity
```

```bash
codex plugin add clarity@riipandi-clarity
```

Codex runs a plugin hook only after you review it. Open Codex, run `/hooks`, and trust the
`clarity` hook. To install the skill alone, without the hook:

```bash
npx skills add riipandi/skill-clarity --global --agent codex
```

### pi

```bash
pi install git:github.com/riipandi/skill-clarity
```

This installs the skill and the `extensions/language-rules.ts` extension. pi has no session
hook, so the extension adds the language rules to the system prompt as a section.

### Claude.ai and Claude Desktop

Build `dist/clarity.skill` (see [Development](#development)) and upload it as a skill in
Settings.

Claude.ai and Claude Desktop chat have no hooks, and a `.skill` file cannot carry one. To apply
the language rules from the first message, paste the contents of
[hooks/session-start.md](hooks/session-start.md) into your personal preferences in Settings, or
into a project's custom instructions.

### Other agents

```bash
npx skills add riipandi/skill-clarity --global --agent '*'
```

Omit `--global` to install in the current project only. For an agent the Skills CLI does not
cover, copy `SKILL.md`, `references/`, and `scripts/` into its skill folder.

These agents get the skill without a hook. To apply the language rules from the first message,
copy `hooks/session-start.md` into the agent's global instructions file.

## Usage

Start with a mode word, then a file path or pasted text. Without a mode word the skill infers
one from the request.

| Mode words | What happens |
|---|---|
| `interview`, `write`, `draft`, `new` | Co-write. The skill interviews you first and drafts from your own words. |
| `rewrite`, `edit`, `fix`, `humanize` | Rewrite an existing draft, preserving its facts and voice. |
| `review`, `critique`, `check` | Critique without rewriting and without changing files. |
| `lint`, `stats` | Run the diagnostic scripts. No prose changes. |

```text
/clarity review docs/architecture.md
/clarity rewrite docs/launch-post.md
/clarity interview a post about why we moved off microservices
/clarity lint README.md
```

In Claude Code the plugin also adds one command per mode. Type `/clarity` and the menu lists
them with a description and an argument hint:

| Command | Argument |
|---|---|
| `/clarity:interview` | what you want to write about |
| `/clarity:rewrite` | a file path, or the pasted draft |
| `/clarity:review` | a file path, or the pasted draft |
| `/clarity:lint` | a file path |

In any agent, `/clarity` with no argument replies with the list of modes.

Plain requests work too, in any language:

```text
Tolong review tulisan ini, jangan diubah dulu: [text]
```

The review comes back in Indonesian. If you then ask for the result as a file, the file is in
English.

To match your voice, paste two or three paragraphs of your own writing before the draft. The
sample outranks every house rule, including the dash rule.

## What is in the box

```text
SKILL.md                    The prompt: language rules, modes, safeguards, final check
references/
  language.md               Which language each kind of output uses, with edge cases
  interview.md              The co-write interview and provenance note
  edit.md                   Order of work and high-value diagnoses for rewrites
  patterns.md               Numbered surface patterns, tiers, and the dash rule
  review.md                 Review format and verdicts
  longform.md               Essays, articles, talks, narrative
  medium.md                 Per-medium routing: docs, academic, email, UI, commits
  indonesian.md             Plain Indonesian, calques, AI tells, EYD, UI copy, RASA
commands/
  interview.md, rewrite.md, review.md, lint.md   Claude Code slash commands, one per mode
hooks/
  hooks.json                SessionStart hook for Claude Code and Codex
  session-start.md          The language rules the hook adds to every session
extensions/
  language-rules.ts         pi extension that adds the same rules to the system prompt
scripts/
  strip_markdown.py         Strip Markdown before measuring prose
  prose_stats.py            Diagnostics for lint mode (no composite score)
  validate_package.py       Package consistency check used by CI
  package_skill.py          Pack the skill into dist/clarity.skill
  check.sh                  Lint and format check for every file type
```

The agent loads only the references a task needs.

## Development

One script lints and format-checks every file type. It needs `uv` and Node, and it pins each
tool's version.

```bash
scripts/check.sh
```

```bash
scripts/check.sh --fix
```

| Files | Tools | Config |
|---|---|---|
| Markdown | [rumdl](https://github.com/rvben/rumdl) | `.rumdl.toml` |
| Python | [ruff](https://docs.astral.sh/ruff/) (lint and format) | `ruff.toml` |
| TypeScript | [oxlint](https://oxc.rs/docs/guide/usage/linter) and [oxfmt](https://oxc.rs/docs/guide/usage/formatter) | `.oxlintrc.json`, `.oxfmtrc.json` |
| JSON, YAML, TOML | oxfmt | `.oxfmtrc.json` |
| Shell | shellcheck and shfmt | none |

Check the package, then pack it into `dist/clarity.skill`. The pack step runs the check first
and includes only `SKILL.md`, `references/`, the two lint scripts, and the license files.

```bash
python3 scripts/validate_package.py
```

```bash
python3 scripts/package_skill.py
```

```bash
npx skills add . --list
```

```bash
claude plugin validate .
```

See [AGENTS.md](AGENTS.md) for the rules on changing the skill.

## Credits and license

MIT. See [LICENSE](LICENSE).

Built on work by Addy Osmani, Siqi Chen, Hardik Pandya, and orepras. Their copyright notices
and what was taken from each are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
Humanizer's pattern list draws on Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
