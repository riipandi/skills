# Surface patterns

Use this for the sentence pass of a rewrite and to name findings in a review. It merges the
pattern lists from Humanizer and Stop Slop under Clarity's rule: a pattern is a prompt to read
the passage, not a verdict. Fix truth, substance, and development first (`edit.md`).

## Tiers

- **Strong (S).** A careful writer rarely does this on purpose. Edit on one sighting.
- **Weak alone (W).** Careful writers do this often. Edit only when two unrelated tells share
  a passage, when the pattern repeats across the piece, or when it hides the meaning.
- **Hard rule (H).** Applies to every text you write or rewrite. One exception, stated in H1.

The codes (S1, W4, H1) are an index for you. In anything the user reads, name the pattern in
plain words. Every watch list below is a search aid. Fix a hit by stating the point, not by swapping in a
synonym. The same constructions exist in every language; treat the equivalent the same way.
`indonesian.md` lists the Indonesian forms.

## Hard rule

### H1. No dashes as connectors

Text you write or rewrite contains no em dash and no en dash, spaced or unspaced, and no double
hyphen used as a dash. Replace each one with a period, comma, colon, or parentheses, or rewrite the
sentence so the relation between the clauses is stated.

A dash lets the writer skip choosing how two clauses relate. Choosing is the edit.

This rule governs your output. In a review, a dash in the author's draft is a weak-alone
pattern: report it only when the draft is full of them or one hides the relation between two
clauses, and report it as a suggestion.

```txt
Before: The new policy, announced without warning (dash) affects thousands (dash) and
        nobody was told.
After:  The new policy was announced without warning. It affects thousands of workers,
        and none of them were told.
```

Exceptions: an author's sample that uses dashes (match its rate); code blocks, inline code,
commands, paths, and URLs; direct quotations; number ranges in tables or data where the house
style uses an en dash. In running prose write the range with `to`.

## A. Staging instead of stating (strong)

### S1. Not X but Y

Watch: `not X but Y`, `not just X, it's Y`, `X isn't the problem, Y is`, `the question isn't X,
it's Y`, `stops being X and starts being Y`, the same contrast split across two sentences, a
clipped negative tail (`..., no guessing`), and negative listing (`Not a X. Not a Y. A Z.`).

The negative half names something no one claimed, so the positive half sounds larger. State Y.
Keep the contrast when the negative half corrects a belief the reader really holds, or when
both halves carry information.

```txt
Before: It's not merely a song, it's a statement.
After:  The heavy beat makes the song sound more aggressive.

Before: This does not mean every choice is equal. It means no external system confirms
        which choice is right.
After:  The choices differ, but no outside system will tell you which one is right.
```

### S2. One-line closers and dramatic fragments

Watch: a one-sentence paragraph that restates the paragraph before it; `That is the real win.`
`Let that sink in.` `Full stop.` `Read that again.`; a sentence after an example that names
what it showed (`This shows the importance of...`); a row of fragments (`Speed. Quality. Cost.`
`That's it. That's the tradeoff.`); a closing `Overall` or `Ultimately` that repeats the verdict;
any line built to be quoted.

The line asks the reader to pause on a claim instead of adding to it. Cut a closer that
repeats. Keep one that adds a fact or a consequence. Merge fragments into one sentence with a
specific claim.

```txt
Before: Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff.
After:  Speed, quality, cost: pick two.
```

### S3. Sayings that sound deep

Watch: `the real question is`, `at its core`, `what really matters`, `the uncomfortable truth
is`, `the heart of the matter`, `X is the Y of Z`, `X is a feature, not a bug`, and vague
declaratives such as `the reasons are structural`, `the implications are significant`, `the
stakes are high`.

An ordinary point is dressed as a hidden truth, or a sentence announces importance without
naming the thing. Replace it with the specific claim. If the source does not contain the
specific claim, cut the sentence or leave `[TK]`.

```txt
Before: Symmetry is the language of trust.
After:  Symmetric layouts often feel more predictable to users.
```

### S4. Run-up before the point

Watch: `Here's the thing:`, `Here's what/why...`, `Let's dive in`, `Let me be clear`, `It turns
out`, `Honestly?`, `Look,`, `Can we talk about`, `What if I told you`, `Think about it:`, `Here's
what I mean:`, a question answered in the next breath, and `the hard part is` or `the part that
matters` standing in for a named thing.

The writer announces the point instead of making it. Remove the run-up and state the point.
`Honestly` inside a casual sentence is ordinary; the tell is the standalone opener.

```txt
Before: What if I told you the best teams don't optimize for productivity? Here's what I
        mean: they optimize for learning. Think about it.
After:  The best teams optimize for learning, not productivity.
```

The contrast in that rewrite stays because the reader does hold the first belief.

### S5. Arguing with no one

Watch: `This isn't about`, `I'm not saying`, `To be clear`, `Don't get me wrong`, `Some might
say... but`, `A tempting approach would be`, `You might think... but`.

The text answers an objection or rejects an option that appears nowhere else. Remove the
defense and keep any real claim inside it. Keep an objection the text attributes or answers in
full.

### S6. Chatbot residue

Watch: `Great question!`, `Certainly!`, `Of course!`, `Here is a...`, `I hope this helps`, `Let
me know if`, `Would you like me to...`, `You're absolutely right`, permission lines such as `And
that's okay`.

Remove the wrapper and keep the content. A plain `let me know` in a real message predates
chatbots and can stay.

### S7. Knowledge-limit disclaimers and guesses

Watch: `as of my last update`, `while specific details are limited`, `based on available
information`, `it is believed that`, `likely grew up`, `maintains a low profile`.

The text admits it found no source and then fills the gap with a plausible guess. State what
the source does not show, or cut the sentence.

### S8. Writing about the document

Watch: `In this section, we'll`, `As we'll see`, `The rest of this essay explains`, `Let me walk
you through`, `The table below compares`, `This function was added to replace`, a first
sentence that restates its heading.

The text describes itself instead of its subject. Delete the announcement and let the piece
move. Mention a previous version only in change logs and migration guides. Keep a source
credit the reader can follow and a caveat that changes what the reader should do.

## B. Inflation and borrowed authority (strong in clusters, weak as single words)

### S9. Inflated significance and sales language

Watch: `stands as a testament`, `a pivotal moment`, `plays a key role`, `marks a shift`, `evolving
landscape`, `despite these challenges... continues to thrive`, `the future looks bright`,
`nestled`, `in the heart of`, `breathtaking`, `renowned`, `rich heritage`, `game-changer`.

An ordinary fact is said to mark a change, prove a legacy, or promise a future. Keep the fact
and drop the significance. End on the last concrete fact. An evaluative word stays when the
same passage supplies the evidence that earns it.

```txt
Before: The institute was established in 1989, marking a pivotal moment in the evolution
        of regional statistics.
After:  The institute was established in 1989.
```

### S10. Borrowed authority and vague connection

Watch: `experts argue`, `studies show`, `industry reports suggest`, a list of prestige outlets,
`associated with`, `linked to`, `in connection with`.

A name or an unnamed authority stands in for what was said. Name the supplied source and what
it said, or cut the claim. If the source does not give the relationship, keep the vague
wording. Do not invent a specific one. A missing citation alone is not a tell.

### S11. Decorative tails and avoided verbs

Watch: trailing `-ing` phrases (`highlighting`, `underscoring`, `reflecting`, `fostering`,
`showcasing`, `ensuring`), and `serves as`, `stands as`, `boasts`, `features`, `represents a`.

An `-ing` phrase is bolted onto a fact to make it sound deeper, or a simple verb is replaced
with a longer one. Keep the fact. Keep the tail only when the source supports what it claims.
Use `is`, `are`, and `has`.

### W1. Stock vocabulary and jargon

Watch: `delve`, `tapestry`, `landscape`, `testament`, `pivotal`, `crucial`, `robust`, `seamless`,
`showcase`, `underscore`, `intricate`, `vibrant`, `additionally`, `navigate` (challenges),
`unpack`, `lean into`, `deep dive`, `double down`, `circle back`, `moving forward`.

Models use these far more than people do, mostly in clusters. One accurate use is not a tell.
A technical sense (`robust` with the failure handling named, `landscape` on a map) is not a
tell. Word habits change with each model release, so weight structure above vocabulary.

## C. Rhythm by rule (weak alone)

### W2. Forced triads

Ideas arrive in threes to sound complete: three adjectives, three parallel examples, three
short facts and a lesson. Check that each item adds a distinct idea. Use the number of items
the meaning has. Three real items stay three.

### W3. Metronomic rhythm

Watch: three or more consecutive sentences of matching length, stacked short punchy sentences,
every paragraph ending on a short line, several sentences in a row opening with the same
subject, paragraphs opening with `So`.

Merge, split, or change the subject where the repetition is a habit. Keep repetition the
writer chose for rhythm. Do not add wobble merely to look irregular.

### W4. Adverbs, intensifiers, and stacked hedges

Watch: `really`, `just`, `literally`, `genuinely`, `honestly`, `simply`, `actually`, `truly`,
`fundamentally`, `inherently`, `crucially`, `importantly`; `could potentially`, `might arguably`,
`it's worth noting`, `in some cases it may`.

Cut the ones that add no meaning. Keep an adverb that changes the claim (`rarely`, `partly`,
`temporarily`) and a hedge the source supports. Removing `most`, `some`, or `may` changes the
claim: that is drift, not tightening.

### W5. Passive voice and abstract actors

Watch: `mistakes were made`, `it is believed that`, and inanimate subjects with human verbs
(`the decision emerges`, `the data tells us`, `the culture shifts`, `the market rewards`).

Name the person, team, or system when that makes the action clearer. Passive voice stays when
the actor is unknown, irrelevant, deliberately protected, or less important than the object.
Technical and academic prose uses it correctly all the time.

### W6. Narrator from a distance

Watch: `Nobody designed this.` `This happens because...` `People tend to...`

The sentence floats above the scene. In authored prose, put a person or the reader in it when
the source supports that. Reference and academic prose is distant on purpose.

### W7. Sweeping extremes

Watch: `every`, `always`, `never`, `everyone`, `nobody` doing vague work.

Use the scope the source supports. Do not narrow a claim the author meant to make broadly.

### W8. Wh- openers and hyphen habits

A sentence that opens `What makes this hard is...` usually hides a plainer subject. Compound
modifiers keep a hyphen after the noun (`the report is high-quality`) where usage drops it.
Both are minor. Fix them only in passing.

## D. Formatting by rule (weak alone, strong when on every item)

### W9. Bold and labels

Words bolded without a reason. Lists where every item is a bold label and a colon followed by
a sentence that repeats the label. Remove the bold. Turn a labeled list into prose when the
labels carry no information. Keep bold for a literal UI element name in an instruction.

### W10. Decorative headings

Title Case Against House Style, emoji or arrows in headings, a horizontal rule between every
section, a heading written for effect instead of naming what the section holds. Use sentence
case and plain names. Keep whatever the project's own style requires.

### W11. Curly quotation marks

Curly quotes where the writer or the target format uses straight ones. Most editors auto-curl,
so this is rarely worth an edit on its own.

## E. Wrong reader (strong when the thread is visible)

### S12. Re-explaining what the reader knows

A reply restates the problem, walks the diagnosis, and proves the plan before it reaches the
decision. In a thread the reader already has the context. Lead with the decision and keep only
the reasoning that would change whether the reader agrees. Act on this only when you can see
the surrounding conversation or the text is clearly a reply.

## When not to act

- A watched phrase inside a quotation, title, proper name, code, or a passage discussing it.
- Text written before late 2022, and informal human text with no second tell.
- A device the surrounding prose earns: a real contrast, three real items, a short landing
  line that carries a new fact, a repetition chosen for rhythm.
- Anything the author's sample does on purpose.
- Any edit that would drop or change a fact, number, name, date, quotation, or condition.

Keep the details that carry the writer's voice: an unusual checkable detail, mixed feelings,
dated references, a real aside or self-correction. Do not add them where they are absent.

## Sources

Humanizer by Siqi Chen (MIT), which draws on Wikipedia's "Signs of AI writing" maintained by
WikiProject AI Cleanup. Stop Slop by Hardik Pandya (MIT). Clarity by Addy Osmani (MIT) for the
tiering principle and the tests in `edit.md`.
