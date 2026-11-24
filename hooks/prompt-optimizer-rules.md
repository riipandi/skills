# Prompt optimizer rules

These rules come from the installed `prompt-optimizer` skill and apply to this whole session.
The user can turn them off with `/prompt-optimizer off` and back on with `/prompt-optimizer on`.

Read each user message as a rough prompt before you act on it:

1. Work out silently the goal, who or what the result is for, the constraints, and what done
   looks like.
2. Fill a non-essential gap with the most defensible assumption, grounded in what the user wrote
   and in the project in front of you.
3. Ask one concise question only when an essential input is missing and a wrong guess would
   waste real work or be hard to undo.
4. Act on the sharpened reading. When an assumption changed what you did, say so in one line.

Do not print the rewritten prompt. Never widen the request: sharpening removes ambiguity, it
does not add tasks. The user's explicit words win over your reading of their intent. Skip this
for messages that are already precise and for greetings, confirmations, and one-word answers.

When message rewriting is on, some messages arrive with a block that starts `PROMPT OPTIMIZER
REWRITE`. A small model wrote it
from the message alone, without the conversation or the project. Use it as a sharper reading,
settle its open points from the project before asking the user, and let the user's own words win
wherever they differ.

When the user asks for a prompt, or you write a brief for a subagent or another model, load the
`prompt-optimizer` skill.
