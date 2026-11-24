# Review format

Review the piece the user supplied. Do not create a replacement draft or change files unless
asked. Lead with the largest material issue; line edits come second.

## Layout

Write the review as plain text the author can read in a chat window:

- Open with two or three sentences that state the largest issue. No heading above them.
- Write each field as its own line: the label, a colon, then the text. Put a blank line between
  fields so each one renders as its own paragraph.
- Do not bold the labels, do not turn fields into bullets, and do not wrap the review in a code
  block. The `txt` blocks below show the fields, not the markup.
- Number the passage findings 1, 2, 3 and separate them with a blank line.
- End with the questions the author must answer, as a numbered list. Ask each question once: a
  finding with the verdict `ask-author` points to its number in this list.

## Piece-level diagnosis

Use these fields when relevant, omitting fields that would add ceremony rather than information.
Keep each field to one or two sentences. A field that only repeats another is ceremony: when
Substance already names what is strong, Voice does not need to list it again.

```txt
Job:          the medium, reader, and intended outcome
Substance:    what the piece specifically contributes, or what is missing
Trust:        factual support, attribution, uncertainty, and any preservation risk
Development:  how the material progresses and where it becomes list-like or repetitive
Voice:        what reads as the author's and where generic model register takes over
Ending:       whether it stops on the last useful thought
Top fixes:    the two or three changes with the largest expected gain, ranked
```

For reference, procedural, academic, legal, or message-oriented prose, do not demand an
authorial thesis. Evaluate whether the text performs its actual job.

If the substance is too thin to support a useful rewrite, say so plainly and offer the
interview. Continue with requested line feedback, but explain that surface edits cannot supply
missing evidence or experience.

## Passage-level finding

Use one block per material issue:

```txt
Passage:      the shortest quote that locates the issue
Verdict:      keep / revise / ask-author / cut
Pattern:      the plain name of the pattern, such as "staged contrast" or "borrowed authority"
Why:          what the passage does instead of its intended job
Suggestion:   a supported replacement, a precise author question, or the reason to cut
Safety check: whether the suggestion preserves facts, attribution, scope, and voice
```

Write the Safety check line only when the suggestion proposes new wording. A cut or a question
to the author changes no fact, so the line would say nothing.

Verdicts:

- `keep`: a pattern is present but earned, required by the medium, or preferable to the
  proposed alternatives. State what earns it.
- `revise`: the source already contains enough material for an honest improvement.
- `ask-author`: improvement needs a fact, mechanism, example, opinion, or experience the source
  does not supply. Ask exactly for that information and offer a cut or plain fallback.
- `cut`: the passage adds only repetition, ceremony, unsupported emphasis, or closure.

Do not invent the missing material in a suggested rewrite. Check your own replacement for the
same formula, inflated claim, meaning drift, or fabricated detail you identified in the source.

## Review discipline

- Distinguish errors from likely improvements and both from taste.
- Quote the previous sentence when context determines whether a contrast, adjective, passive,
  list, or closing beat is earned.
- Prefer a few high-impact findings to an exhaustive word watchlist. Five passage findings is
  usually enough, and the whole review of a piece under 500 words should fit in about 400
  words. Fold several hits of one pattern into a single finding, and give a full line
  edit only when the user asks for one.
- Name patterns in plain words. The codes in `patterns.md` (S1, W4, H1) are an index for you.
  The author has not seen that file, so a code in a review is noise.
- House rules bind the text you write, not the author's draft. The dash rule is the clearest
  case: a dash in the draft is a weak-alone pattern like any other, worth a finding only when
  dashes are everywhere or one hides how two clauses relate. Never tell an author that a dash
  must go.
- Report no finding when the prose already performs its job.
- Do not use a detector verdict as evidence that a passage is good, bad, human, or generated.
- Do not attach a numeric score. A number invites optimizing toward the count instead of the
  reader. For Indonesian text, use the RASA lens in `indonesian.md` as four questions, not four
  scores.
- A weak-alone pattern from `patterns.md` is a finding only when it clusters with other tells or
  obscures the meaning. Report a lone one as `keep`, or leave it out.

## Language of the review

A review delivered in chat is conversation: write it in the language the user is using. Keep
the field labels above in English so the format stays stable. Quote each passage in its original
language, and write any suggested replacement in the language of the piece under review. A
review the user asks you to save to a file is an artifact and follows `language.md`.
