# Prompting principles

Use this when you write or rewrite a prompt, including a brief for a subagent. Each principle
has a reason. Apply the reason with judgment; do not paste the rules in mechanically.

Current models read prompts literally, size their effort to the complexity they perceive, and do
better with prompts that are specific, structured, and motivated.

## Core principles

### Be clear and direct

State the task. Give the output format and the hard constraints up front. If you want more than
the minimum, say so: models do not infer ambition from a vague brief. "Create an analytics
dashboard" is weaker than "Create an analytics dashboard with as many relevant features and
interactions as you can. Go beyond the basics."

### Explain the why

Give the reason with the instruction. "Avoid ellipses, because a text-to-speech engine will read
this aloud and mispronounces them" works better than "Never use ellipses." A model generalizes
from a reason and follows it more faithfully than a bare rule.

### Say what to do, not what to avoid

Positive framing works better than negative. "Write in flowing paragraphs" beats "do not use
bullet points."

### Match the prompt's style to the output you want

For prose, write the prompt in prose. For output with little Markdown, use little Markdown in
the prompt. Style leaks through.

### Use tags when sections multiply

When a prompt mixes instructions, context, examples, and input, wrap each in a descriptive tag:
`<instructions>`, `<context>`, `<examples>`, `<input>`. Nest them where there is hierarchy. This
is the highest-value structure for a complex prompt. Skip it for a simple one-shot request.

### Give a role when it sharpens behavior

One line ("You are a senior product strategist at a B2B SaaS company") tightens tone and frame.
Use a role only when it steers the output. Do not force one onto every prompt.

### Use examples for format, tone, or structure

If the user cares how the output looks, include two to four examples in `<example>` tags.
Examples steer format better than description does. Make them relevant, varied, and consistent
in structure. Use only examples the user supplied or ones that are clearly generic; never
present an invented example as the user's own. Skip examples when they would over-constrain a
generic task.

### Put long inputs first and the question last

When the prompt carries a long document, transcript, or data dump, place it at the top and the
question at the bottom. This ordering improves answers on long-context tasks.

### Ask for grounding over long documents

For analysis or questions over a long input, tell the model to pull the relevant quotes into
`<quotes>` tags first and to answer from those quotes. This reduces drift and fabrication.

### Be literal about scope

A model does not always generalize an instruction. To apply something broadly, say "apply this
to every section, not only the first." To get action instead of advice, use imperative verbs:
"Edit the function to...", not "Could you suggest improvements to...". Suggestion-shaped phrasing
produces suggestions.

### Ask for deeper reasoning once, at the end

A closing line that asks for careful thought nudges a model toward deeper work on a hard
problem. Put it at the end and nowhere else; competing thinking instructions add noise.

### Add a self-check when errors are costly

For code, math, or factual claims, add a verification line near the end: "Before you finish,
re-read your answer and check it against the criteria above."

## Moves for specific tasks

Apply these only when the task matches.

- **Frontend and design.** Models have strong stylistic defaults. Either specify a concrete
  palette, type system, and structure, or tell the model to propose three or four distinct
  visual directions before building so the user can pick one. "Make it clean and minimal" is
  not enough.
- **Code review.** Say that the job at the finding stage is coverage, not filtering: "Report
  every issue you find, including ones you are unsure about or consider minor. Give a confidence
  and a severity for each, so a later pass can rank them." Soft phrasing such as "only flag
  important issues" makes a model over-filter.
- **Research and analysis.** Ask for competing hypotheses: "Develop several hypotheses as you
  gather information. Track your confidence in each. Critique your own approach as you go."
- **Creative writing.** Specify voice, audience, length, and constraints. Include one or two
  sentences in the target voice when the user has them.
- **Documents, slides, and reports.** Ask for design intent: visual hierarchy, considered
  typography, and a structure that helps the reader.
- **Briefs for subagents.** State the goal and what done looks like, what is already known or
  ruled out, the files or sources worth reading, the limits on scope, and the form the answer
  should take. The delegate has none of your context.

## Source

Adapted from the `prompt-optimizer` skill in
[github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/prompt-optimizer)
(MIT, GitHub, Inc.). The subagent brief guidance is an addition made for this repo.
