# Examples

Each example shows the user's input and the single code block to return. None contains a
placeholder.

## A kind of task, no content given

Input: `I want a prompt to summarize my emails`

```txt
You are an executive assistant helping me triage email. I will share a batch of emails in my
next message.

For each email, give me:
- Sender and subject on one line
- A summary of one or two sentences, in a neutral tone
- The action required: reply needed, FYI only, schedule, delegate, or ignore
- A priority of high, medium, or low, based on the sender and any urgency cues

Group the output into three sections in this order: high, medium, low. Inside each section,
list emails that need a reply first.

Leave out automated marketing and notification mail, and list its senders and subjects under a
final "Filtered out" heading so I can check.

When you are ready, ask me to paste the emails.
```

The prompt ends by inviting the content in the next turn. There is no block for the user to
fill in.

## A rough draft, details missing

Input: `can you fix this prompt: "write a linkedin post about my new product launch, make it
engaging and not too salesy"`

```txt
You are writing a LinkedIn post for me that announces a product launch. The readers are B2B
operators who have seen every launch template and distrust marketing language.

Before you draft, ask me for:
- The product's name
- What it does, in plain language
- Who it is for
- One or two reasons I built it that the description does not make obvious
- The link for the call to action

Once I answer, write one post that:
- Opens with a concrete hook in the first two lines: a tension, a number, or an unexpected
  observation. Do not open with an announcement.
- Tells the short story or insight that led to the product before naming it.
- Says what the product does in one plain sentence, with no superlatives.
- Closes with one clear next step.
- Runs between 150 and 220 words, in short paragraphs, with no emoji.

Write as someone who built the thing and is talking to peers.
```

The missing product details are not invented and not left as blanks. The prompt tells the model
to ask for them.

## Real content given

Input: `rewrite this so it's clearer: "help me figure out whether to take offer A or offer B.
A is 280k base + 60k bonus + 100k stock per year vesting over 4, hybrid 3 days a week. B is 250k
base, no bonus, 800k stock over 4 with a 1yr cliff, fully remote. I care most about long term
equity upside, work I'd be excited about, and not relocating."`

```txt
I am deciding between two job offers and want your help thinking it through.

My priorities, in order:
1. Long-term equity upside
2. Work I would be excited about
3. Not relocating

Offer A
- $280k base
- $60k annual bonus
- $100k per year in stock, vesting over 4 years
- Hybrid, in the office 3 days a week

Offer B
- $250k base
- No annual bonus
- $800k in stock, vesting over 4 years with a 1-year cliff
- Fully remote

Walk me through:
1. Total expected compensation for each offer, year by year over 4 years, with bear, base, and
   bull cases for the equity.
2. How each offer scores against my three priorities.
3. The non-obvious risks in how each offer is structured.
4. Your recommendation, and the single biggest reason it could be wrong.

Be direct. I have told you what I value, so do not answer that it depends on what I value.

Take time to think this through before answering.
```

Every number the user gave is in the prompt, unchanged. The closing line asks for careful
reasoning because the task needs it.

## A simple task

Input: `write me a haiku about coffee`

```txt
Write a haiku about coffee in the traditional 5-7-5 syllable form. Build it around one concrete
image a reader could picture, not a general statement about coffee.
```

A simple task gets no role, no tags, and no closing line. Structure in proportion to the task.

## Source

Adapted and shortened from the examples in the `prompt-optimizer` skill in
[github/awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/prompt-optimizer)
(MIT, GitHub, Inc.).
