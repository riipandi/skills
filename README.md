# Riipandi Skills

Agent skills I use every day, packaged as one plugin for Claude Code, Codex, Cursor, pi, and any
agent that reads `SKILL.md`.

| Skill | What it does | Always on |
|---|---|---|
| [clarity](skills/clarity/SKILL.md) | Drafts, rewrites, and reviews prose so it is specific, useful, and recognizably the author's, without inventing facts. Chat follows your language; files are written in English. | Language rules, through the hook |
| [prompt-optimizer](skills/prompt-optimizer/SKILL.md) | Turns a rough prompt into a finished one, and reads each of your messages as a rough prompt to sharpen before acting. | Yes, through the hook. Toggle with `on` and `off`. |

## Installation

Installed as a plugin, the skills live under the `riipandi` namespace: `/riipandi:clarity` and
`/riipandi:prompt-optimizer`. Installed with the Skills CLI or as `.skill` files, they are plain
`/clarity` and `/prompt-optimizer`.

### Claude Code

```text
/plugin marketplace add riipandi/skills
/plugin install riipandi@riipandi-skills
```

The plugin also installs two hooks. `SessionStart` puts Clarity's language rules and the prompt
optimizer rules into every session from the first message. `UserPromptSubmit` handles
`/prompt-optimizer on` and `/prompt-optimizer off`.

If you installed an earlier version as `clarity@riipandi-clarity`, remove it first.

### Codex

```bash
codex plugin marketplace add riipandi/skills
```

```bash
codex plugin add riipandi@riipandi-skills
```

Codex runs a plugin hook only after you review it. Open Codex, run `/hooks`, and trust the
`riipandi` hooks. To install the skills alone, without the hooks:

```bash
npx skills add riipandi/skills --global --agent codex
```

### pi

```bash
pi install git:github.com/riipandi/skills
```

This installs both skills and the `extensions/session-rules.ts` extension. pi has no session
hook, so the extension adds the same rules to the system prompt and reads the same on/off state.

### Claude.ai and Claude Desktop

Build the `.skill` files (see [Development](#development)) and upload `dist/clarity.skill` and
`dist/prompt-optimizer.skill` as skills in Settings.

Claude.ai and Claude Desktop chat have no hooks, and a `.skill` file cannot carry one. To apply
the always-on rules from the first message, paste the contents of
[hooks/clarity-language-rules.md](hooks/clarity-language-rules.md) and
[hooks/prompt-optimizer-rules.md](hooks/prompt-optimizer-rules.md) into your personal preferences
in Settings, or into a project's custom instructions.

### Other agents

```bash
npx skills add riipandi/skills --global --agent '*'
```

Add `--skill clarity` or `--skill prompt-optimizer` to install one skill. Omit `--global` to
install in the current project only. For an agent the Skills CLI does not cover, copy the
skill's folder from `skills/` into the agent's skill folder.

These agents get the skills without a hook. To apply the always-on rules from the first message,
copy the two files in `hooks/` named above into the agent's global instructions file.

## Clarity

A personal fork of [Clarity](https://github.com/addyosmani/clarity) by Addy Osmani, merged with
three other skills:

| Source | What Clarity takes from it |
|---|---|
| [addyosmani/clarity](https://github.com/addyosmani/clarity) | The base: four modes, shared safeguards, the editing order, the interview, the review format, the lint scripts |
| [blader/humanizer](https://github.com/blader/humanizer) | The pattern catalog, the strong and weak-alone tiers, the dash rule, file and embedded return modes |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | Phrase and structure watch lists, folded into the tiers instead of applied as bans |
| [bahasa-indonesia-plain](https://gist.github.com/orepras/3e1ca8974fc51d11825f142fa6a66635) | Plain Indonesian, EYD conventions, UI copy guidance, the RASA quality lens |

I chat with agents in Indonesian and ship work in English. Those four skills each solve part of
that and disagree in places. This fork settles the disagreements once:

- **Chat follows the user's language.** Replies, questions, and review findings use the
  language I am writing in.
- **Artifacts are English.** Files, documentation, reports, code comments, commit messages,
  pull requests, issues, and drafted messages are written in English, even when the chat is
  not. The exceptions are an artifact I name a language for, and content whose language the
  product fixes, such as a locale file.
- **Truth outranks polish.** The skill never adds a detail from its own knowledge. It asks, or
  leaves `[TK: question]`.
- **Patterns are tiered, not banned.** Strong tells are edited on one sighting. Weak ones
  (passive voice, adverbs, triads) are edited only in clusters or when they hide the meaning.
- **No dashes.** Text the skill writes has no em dash or en dash unless my own writing sample
  uses them.
- **No scores.** Reviews report findings in words. RASA is four questions, not four numbers.

### Using Clarity

Start with a mode word, then a file path or pasted text. Without a mode word the skill infers
one from the request. With nothing to work on, it replies with the list of modes.

| Mode words | What happens |
|---|---|
| `interview`, `write`, `draft`, `new` | Co-write. The skill interviews you first and drafts from your own words. |
| `rewrite`, `edit`, `fix`, `humanize` | Rewrite an existing draft, preserving its facts and voice. |
| `review`, `critique`, `check` | Critique without rewriting and without changing files. |
| `lint`, `stats` | Run the diagnostic scripts. No prose changes. |

```text
/riipandi:clarity review docs/architecture.md
/riipandi:clarity interview a post about why we moved off microservices
```

In Claude Code the plugin adds one command per mode. The slash menu shows each with a
description and an argument hint:

| Command | Argument |
|---|---|
| `/riipandi:clarity-interview` | what you want to write about |
| `/riipandi:clarity-rewrite` | a file path, or the pasted draft |
| `/riipandi:clarity-review` | a file path, or the pasted draft |
| `/riipandi:clarity-lint` | a file path |

Plain requests work too, in any language:

```text
Tolong review tulisan ini, jangan diubah dulu: [text]
```

The review comes back in Indonesian. If you then ask for the result as a file, the file is in
English. To match your voice, paste two or three paragraphs of your own writing before the
draft. The sample outranks every house rule, including the dash rule.

## Prompt Optimizer

Adapted from the `prompt-optimizer` skill in
[github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/prompt-optimizer).
The original returns a finished prompt for a chat interface. This version keeps that and adds an
always-on mode for agent sessions.

### Always on

With the hooks installed, the agent reads each message as a rough prompt before acting. It works
out the goal, the audience, the constraints, and what done looks like. It fills small gaps with
a defensible assumption and asks one question only when an essential input is missing. It does
not print the rewritten prompt, and it never widens the request.

| Command | What happens |
|---|---|
| `/riipandi:prompt-optimizer off` | Turn it off, for this session and new ones |
| `/riipandi:prompt-optimizer on` | Turn it back on |
| `/riipandi:prompt-optimizer status` | Say whether it is on or off |

The state is one file, `~/.config/riipandi-skills/prompt-optimizer-off`, shared by Claude Code,
Codex, and pi. It exists when the optimizer is off. Delete it to turn the optimizer back on by
hand.

### On request

Give it anything else and it returns one finished prompt in a code block:

```text
/riipandi:prompt-optimizer I need a prompt that reviews my Python code for bugs
```

The prompt never contains a placeholder such as `[paste code here]`. If it needs content you
have not given, it tells the model to ask you for it.

## What is in the box

```text
skills/
  clarity/
    SKILL.md                The prompt: language rules, modes, safeguards, final check
    references/             Loaded on demand: language, interview, edit, patterns, review,
                            longform, medium, indonesian
    scripts/                strip_markdown.py and prose_stats.py for lint mode
    evals/                  Test cases in the `claude plugin eval` layout
  prompt-optimizer/
    SKILL.md                The prompt: arguments, toggle, always-on behavior, explicit use
    references/             principles.md and examples.md
commands/                   Claude Code slash commands, one per Clarity mode
hooks/
  hooks.json                SessionStart and UserPromptSubmit hooks for Claude Code and Codex
  hook.sh                   Prints the rules and handles the prompt-optimizer toggle
  clarity-language-rules.md, prompt-optimizer-rules.md   The rules the hook adds to a session
extensions/
  session-rules.ts          pi extension that adds the same rules to the system prompt
scripts/
  check.sh                  Lint and format check for every file type
  validate_package.py       Consistency check for skills and manifests, used by CI
  package_skill.py          Pack each skill into dist/<name>.skill
```

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

Pack every skill into `dist/<name>.skill`, or name the ones you want. The pack step runs the
validator first and leaves `evals/` out.

```bash
python3 scripts/package_skill.py
```

```bash
python3 scripts/package_skill.py clarity
```

```bash
npx skills add . --list
```

```bash
claude plugin validate .
```

See [AGENTS.md](AGENTS.md) for the rules on changing a skill or adding one.

## Credits and license

MIT. See [LICENSE](LICENSE).

Built on work by Addy Osmani, Siqi Chen, Hardik Pandya, orepras, and GitHub. Their copyright
notices and what was taken from each are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
Humanizer's pattern list draws on Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). The repo
layout follows [mattpocock/skills](https://github.com/mattpocock/skills), and the on/off toggle
follows [ponytail](https://github.com/DietrichGebert/ponytail).
