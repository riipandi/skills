// pi has no SessionStart hook, so this extension adds the same rules the Claude Code and
// Codex hook prints (hooks/hook.sh) to the system prompt.
import { existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const read = (name: string) => readFileSync(new URL(`../hooks/${name}`, import.meta.url), "utf8");
const languageRules = read("clarity-language-rules.md");
const optimizerRules = read("prompt-optimizer-rules.md");

// Same flag file as hooks/hook.sh: it exists when the prompt optimizer is off.
const offFlag = join(
  process.env.XDG_CONFIG_HOME || join(homedir(), ".config"),
  "riipandi-skills",
  "prompt-optimizer-off",
);

export default function (pi: ExtensionAPI) {
  pi.on("before_agent_start", async (event) => {
    // A section is diffed against what the model already has, so each costs one patch per change.
    const sections = event.systemPromptOptions.sections;
    sections.clarity_language_rules = languageRules;
    // Checked on every run so `/prompt-optimizer off` takes effect without a restart.
    if (existsSync(offFlag)) delete sections.prompt_optimizer_rules;
    else sections.prompt_optimizer_rules = optimizerRules;
  });
}
