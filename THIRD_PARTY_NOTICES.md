# Third-party notices

The skills in this repo combine and adapt the sources below. The MIT-licensed ones have their
copyright notices reproduced here as the license requires. One source has no stated license and
is credited as the source of adapted ideas.

## Clarity

- Source: <https://github.com/addyosmani/clarity>
- Copyright (c) 2026 Addy Osmani
- License: MIT
- Used for: the base of `skills/clarity/SKILL.md`, the modes and their arguments, `references/interview.md`,
  `references/edit.md`, `references/review.md`, `references/longform.md`,
  `references/medium.md`, `scripts/strip_markdown.py`, and `scripts/prose_stats.py`. The
  reference files are modified. The two scripts are reformatted with ruff; their logic is
  unchanged.

## Humanizer

- Source: <https://github.com/blader/humanizer>
- Copyright (c) 2025 Siqi Chen
- License: MIT
- Used for: the pattern catalog and strength tiers in `references/patterns.md`, the dash rule,
  the file and embedded return modes, and the packaging layout (`.claude-plugin/`,
  `.cursor-plugin/`, `package.json`, `agents/openai.yaml`).

## Stop Slop

- Source: <https://github.com/hardikpandya/stop-slop>
- Copyright (c) 2025 Hardik Pandya
- License: MIT
- Used for: phrase and structure watch lists merged into `references/patterns.md`.

## bahasa-indonesia-plain

- Source: <https://gist.github.com/orepras/3e1ca8974fc51d11825f142fa6a66635>
- Author: orepras
- License: none stated at the time of writing
- Used for: the plain-language principles, EYD conventions, UI copy guidance, and the RASA
  framework adapted in `references/indonesian.md`. The guidance is rewritten in English, not
  copied.

## prompt-optimizer

- Source: <https://github.com/github/awesome-copilot/tree/main/skills/prompt-optimizer>
- Copyright GitHub, Inc.
- License: MIT
- Used for: the two hard rules, the rewrite workflow, the prompting principles, and the examples
  in `skills/prompt-optimizer/`. The text is rewritten and shortened. The always-on mode, the
  toggle, and the subagent brief guidance are additions.

## Ideas without copied text

- The repo layout (several skills under `skills/`, shipped as one plugin) follows
  <https://github.com/mattpocock/skills>.
- The on/off toggle handled by a `UserPromptSubmit` hook follows
  <https://github.com/DietrichGebert/ponytail>.

## MIT License

The MIT-licensed sources above are used under these terms:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
