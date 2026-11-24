// pi has no SessionStart hook, so this extension adds the same language rules the
// Claude Code and Codex hook prints (hooks/session-start.md) to the system prompt.
import { readFileSync } from "node:fs";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const rules = readFileSync(new URL("../hooks/session-start.md", import.meta.url), "utf8");

export default function (pi: ExtensionAPI) {
  pi.on("before_agent_start", async (event) => {
    // A section is diffed against what the model already has, so this costs one patch per session.
    event.systemPromptOptions.sections.clarity_language_rules = rules;
  });
}
