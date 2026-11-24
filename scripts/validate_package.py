#!/usr/bin/env python3
"""Check that every skill and manifest in the repo is consistent and follows the house rules."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json")
# The .skill format rejects any other top-level frontmatter key.
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
failures = []


def check(ok, message):
    print(("PASS  " if ok else "FAIL  ") + message)
    if not ok:
        failures.append(message)


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


skill_dirs = sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))
names = [d.name for d in skill_dirs]
check(len(skill_dirs) >= 2, f"found skills: {', '.join(names)}")

for skill_dir in skill_dirs:
    rel = skill_dir.relative_to(ROOT)
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    front = text.split("---", 2)[1]
    name = re.search(r"^name:\s*(\S+)", front, re.M).group(1)
    description = re.search(r'^description:\s*"(.*)"$', front, re.M)
    check(name == skill_dir.name, f"{rel}/SKILL.md name matches its folder")
    check(bool(description) and len(description.group(1)) <= 1024, f"{rel}/SKILL.md description fits 1024 characters")
    check(bool(re.search(r'^\s+version:\s*"[^"]+"', front, re.M)), f"{rel}/SKILL.md has metadata.version")
    extra = set(re.findall(r"^([\w-]+):", front, re.M)) - ALLOWED_KEYS
    check(not extra, f"{rel}/SKILL.md frontmatter has only allowed keys {sorted(extra) or ''}")
    # Every reference or script the prompt routes to must exist, and every reference must be routed to.
    for target in sorted(set(re.findall(r"`((?:references|scripts)/[\w.-]+)`", text))):
        check((skill_dir / target).is_file(), f"{rel}/{target} exists")
    for path in sorted((skill_dir / "references").glob("*.md")):
        check(f"references/{path.name}" in text, f"{rel}/SKILL.md routes to references/{path.name}")
    check((skill_dir / "agents" / "openai.yaml").is_file(), f"{rel}/agents/openai.yaml exists")

versions = set()
for rel in MANIFESTS:
    data = load(rel)
    check(data["name"] == "riipandi", f"{rel} name is riipandi")
    versions.add(data["version"])
check(len(versions) == 1, f"plugin manifests agree on the version {sorted(versions)}")
for rel in load(".claude-plugin/plugin.json")["skills"]:
    check((ROOT / rel / "SKILL.md").is_file(), f"Claude plugin skill {rel} exists")
check(
    sorted(Path(s).name for s in load(".claude-plugin/plugin.json")["skills"]) == names,
    "Claude plugin lists every skill",
)
package = load("package.json")
check(sorted(Path(s).name for s in package["pi"]["skills"]) == names, "pi package lists every skill")
for rel in package["pi"]["extensions"]:
    check((ROOT / rel).is_file(), f"pi extension {rel} exists")
listed = sorted(s for group in load("skills.sh.json")["groupings"] for s in group["skills"])
check(listed == names, "skills.sh.json lists every skill")
load(".claude-plugin/marketplace.json")
hooks = json.dumps(load("hooks/hooks.json"))
check("hook.sh" in hooks and (ROOT / "hooks" / "hook.sh").is_file(), "hooks/hooks.json points at hooks/hook.sh")
for rule_file in re.findall(r"hooks/([\w-]+\.md)", (ROOT / "hooks" / "hook.sh").read_text(encoding="utf-8")):
    check((ROOT / "hooks" / rule_file).is_file(), f"hooks/{rule_file} exists")

# Each command must show a description and an argument hint in the slash menu.
for path in sorted((ROOT / "commands").glob("*.md")):
    head = path.read_text(encoding="utf-8").split("---", 2)[1]
    check("description:" in head and "argument-hint:" in head, f"commands/{path.name} has a description and a hint")
    check(path.stem.split("-")[0] in names or path.stem in names, f"commands/{path.name} is named after a skill")

changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
headings = re.findall(r"^## (.+)$", changelog, re.M)
check(
    bool(headings) and all(re.fullmatch(r"\d{8}-\d{4}", h) for h in headings),
    "CHANGELOG.md headings are YYYYMMDD-HHMM timestamps",
)
check(headings == sorted(headings, reverse=True), "CHANGELOG.md entries are newest first")

# The prompt files follow Clarity's hard rule: no em or en dash.
prompt_files = [ROOT / "README.md", *sorted((ROOT / "hooks").glob("*.md"))]
for skill_dir in skill_dirs:
    prompt_files += [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]
for path in prompt_files:
    check(not re.search("[–—]", path.read_text(encoding="utf-8")), f"{path.relative_to(ROOT)} has no dashes")

sys.exit(1 if failures else 0)
