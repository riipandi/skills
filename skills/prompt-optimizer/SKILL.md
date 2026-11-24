---
name: prompt-optimizer
description: "Turn a rough prompt, half-formed idea, or task description into a finished prompt, and read every user message as a rough prompt to sharpen before acting. Use when the user wants to write, rewrite, optimize, improve, or polish a prompt, pastes a draft prompt, or describes a task they plan to send to an LLM. Also use when you write a brief for a subagent or another model. Toggle the always-on behavior with `on`, `off`, or `status`."
argument-hint: "[on|off|status|<prompt to optimize>]"
license: MIT
metadata:
  version: "0.1.0"
---

# Prompt optimizer

A rough prompt leaves the model to guess the goal, the audience, the format, and what done looks
like. This skill closes those gaps. It works in two ways: as an always-on habit applied to the
user's own messages, and as an explicit tool that returns a finished prompt.

## Arguments

```txt
on        Turn the always-on behavior on, for this session and new ones.
off       Turn it off, for this session and new ones.
status    Say whether it is on or off.
<text>    Anything else is a prompt to optimize. Return the finished prompt.
```

With no argument and nothing to optimize in the conversation, reply with these four lines in the
user's language and ask what they want to do.

## Toggle: on, off, status

The always-on behavior is on by default wherever this repo's hooks or extensions are installed.
The state lives in one flag file: `~/.config/riipandi-skills/prompt-optimizer-off` (under
`$XDG_CONFIG_HOME` when that is set). The file exists when the behavior is off.

1. If a hook already handled the command, this turn's context holds a line starting with
   `PROMPT OPTIMIZER ON`, `PROMPT OPTIMIZER OFF`, or `PROMPT OPTIMIZER STATUS`. The state is
   saved. Do not touch the file.
2. If no such line is present and you have a shell, create the flag file for `off` or delete it
   for `on`. For `status`, check whether it exists.
3. If you have no shell, apply the change to this session only and say that it will not persist.

Then confirm in one short line, in the user's language, and follow the new state for the rest of
the session. `on` and `off` change nothing else: do not optimize anything in the same turn.

## Always-on behavior

When it is on, read each user message as a rough prompt before you act on it.

1. Work out, silently: the goal, who or what the result is for, the constraints, and what done
   looks like.
2. Fill a non-essential gap with the most defensible assumption, grounded in what the user wrote
   and in the project in front of you.
3. Ask one concise question only when an essential input is missing and a wrong guess would
   waste real work or be hard to undo.
4. Act on the sharpened reading. When an assumption changed what you did, say so in one line.

Limits that keep this from getting in the way:

- Do not print the rewritten prompt. The user asked for the work, not for their prompt back.
- Never widen the request. Sharpening removes ambiguity; it does not add tasks, features, or
  files the user did not ask for.
- The user's explicit words win over your reading of their intent.
- Skip it for messages that are already precise, and for greetings, confirmations, and
  one-word answers.
- When you write a prompt for a subagent or another model, apply `references/principles.md` to
  that brief. A delegate knows only what the brief says.

## Explicit use: return a finished prompt

When the user asks for a prompt, or gives text to optimize, read `references/principles.md`.
Read `references/examples.md` when you are unsure what a finished prompt looks like.

Two rules override everything else in this mode.

**No placeholders.** The prompt never contains `[paste X here]`, `{topic}`, `<your_input>`,
`___`, or any other blank the user must fill. They must be able to copy it, paste it, and send
it. If you are typing square brackets around a noun, stop and rewrite.

**Ship a finished prompt whatever the user gave you.**

- The user gave real content (a draft, code, a document, numbers, a specific question): bake it
  into the prompt. Content and instructions go in together.
- The user only described a kind of task ("a prompt to triage my email"): write a complete,
  self-contained instruction. End it by telling the model to ask for the inputs it needs, or
  phrase it so the user supplies them in the next turn ("I will paste the emails next").

Work through this before writing. Do not show the steps.

1. Name the goal: a document, a decision, code, a list, an analysis.
2. Name the audience and what they will do with the output.
3. Decide which case applies: real content, or a kind of task.
4. List the gaps: audience, format, length, constraints, examples, edge cases.
5. Fill non-essential gaps with defensible assumptions. For essential inputs the user has not
   given, make the prompt ask for them.
6. Choose a structure: one paragraph for a simple task, tagged sections when the prompt mixes
   instructions, context, examples, and input.
7. Write the prompt.
8. Scan the result for brackets and blanks. Remove every one.

What to return:

- One fenced code block holding the prompt, and nothing else. No preamble, no note on what
  changed. Explain the changes only if the user asks afterward.
- Keep structure in proportion to the task. A haiku request does not need a role, tags, or
  sections.
- Match the target. A prompt for a chat interface carries everything in one message, because
  there is no system prompt or parameter to lean on. If the user gives an API-style prompt,
  translate its intent into that one message and drop the API-only mechanics.
- For a task that needs careful reasoning, end the prompt with one line that asks for it, such
  as "Take time to think this through before answering." Leave it out of simple tasks, and do
  not add competing thinking instructions earlier in the prompt.
- Write the prompt in the language of the user's input unless they name another. A prompt saved
  to a file follows the project's rules for files.

Edge cases:

- "Is this prompt good?" is a rewrite request. Return the optimized version.
- A prompt that is already excellent gets tightened and returned. Do not add ceremony.
- Many small asks become one coherent prompt with clear sections, not a list of micro-tasks.
- Never invent facts about the user, their product, or their data to make the prompt richer.
  Make the prompt ask for them.
