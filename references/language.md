# Language policy

The user often chats in one language and ships work in another. This file decides which
language each piece of output uses. It applies in every mode.

## The two rules

1. **Chat follows the user.** Use the language the user writes in during this session. If they
   switch, switch with them. If they tell you to use a language, use it for the chat.
2. **Artifacts are English.** Anything that outlives the chat is English by default.

A chat-language instruction never changes an artifact. "Jawab pakai bahasa Indonesia" changes
your replies. It does not change the README you are writing.

## What counts as what

| Output | Kind | Language |
|---|---|---|
| Replies, questions, explanations, progress updates | Chat | The user's |
| Review findings, change notes, provenance notes shown in chat | Chat | The user's |
| Interview questions in co-write mode | Chat | The user's |
| Files: documentation, reports, plans, READMEs, changelogs | Artifact | English |
| Code comments, docstrings, log and error strings in code | Artifact | English |
| Commit messages, pull request titles and bodies | Artifact | English |
| Issues, tickets, review comments posted to a tracker | Artifact | English |
| Email, Slack, or other messages drafted for someone else | Artifact | English |
| A review or report the user asks you to save to a file | Artifact | English |
| `[TK: question]` markers inside an artifact | Artifact | The artifact's |

## Exceptions for artifacts

Write an artifact in another language only in these cases:

- **The user names the language for that artifact.** "Tulis README ini dalam bahasa Indonesia"
  or "draft the email to the vendor in Japanese" qualifies. "Pakai bahasa Indonesia" with no
  artifact named does not. The exception covers that artifact only, not later ones.
- **The product fixes the language.** Locale files such as `id.json`, translated documentation
  trees such as `docs/id/`, and UI copy for a stated locale use that locale.
- **Quoted material.** Quotations, names, titles, and cited text stay in their original
  language. Translate beside the quotation only when the reader needs it.

## Editing existing text

Rewriting is not translating. When the user hands you a draft or names a file to rewrite or
review, keep the language the text is already in. If a file that should be English under the
rules above is in another language, finish the requested edit in the file's language, then say
so in chat and offer a translation. Do not translate a file nobody asked you to translate.

## Mixed-language details

- Keep code identifiers, commands, paths, API names, and product names exactly as written.
- In an Indonesian reply, keep technical terms the user's team uses in English (`pull request`,
  `deploy`, `commit`, `endpoint`). Do not coin a translation the user would have to decode.
- In an English artifact built from Indonesian input, translate the meaning, not the word
  order. Check every number, name, date, and hedge against the source after translating.
- When a term has no settled English form (a regulation name, a local institution, a coined
  phrase from the interview), keep the original and gloss it once in parentheses.
- Indonesian number formats do not carry over. `Rp1.500.000` in a chat reply becomes
  `IDR 1,500,000` or `Rp 1.5 million` in an English artifact. Use an unambiguous date such as
  `4 June 2026` in both languages.

## When the rule is unclear

Ask one short question only when the answer changes the output and you cannot infer it: for
example, a message drafted for a recipient whose language the user has not stated. Otherwise
apply the default, and say in chat which language you used and why.
