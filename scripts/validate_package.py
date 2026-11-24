#!/usr/bin/env python3
"""Check that the package files exist, agree on the version, and follow the dash rule."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = []


def check(ok, message):
    print(("PASS  " if ok else "FAIL  ") + message)
    if not ok:
        failures.append(message)


skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
front = skill.split("---", 2)[1]
name = re.search(r"^name:\s*(\S+)", front, re.M).group(1)
version = re.search(r'^\s+version:\s*"([^"]+)"', front, re.M).group(1)
check(name == "clarity", "SKILL.md name is clarity")
# The .skill format rejects any other top-level frontmatter key.
allowed = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
extra = set(re.findall(r"^([\w-]+):", front, re.M)) - allowed
check(not extra, f"SKILL.md frontmatter has only allowed keys {sorted(extra) or ''}")

# Every reference or script the prompt routes to must exist.
for rel in sorted(set(re.findall(r"`((?:references|scripts)/[\w.-]+)`", skill))):
    check((ROOT / rel).is_file(), f"{rel} exists")
for path in (ROOT / "references").glob("*.md"):
    check(f"references/{path.name}" in skill, f"SKILL.md routes to references/{path.name}")

for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json"):
    data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    check(data["name"] == name, f"{rel} name matches SKILL.md")
    check(data["version"] == version, f"{rel} version is {version}")
for rel in (".claude-plugin/marketplace.json", "package.json", "skills.sh.json", "hooks/hooks.json"):
    json.loads((ROOT / rel).read_text(encoding="utf-8"))
    check(True, f"{rel} is valid JSON")
package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
for rel in package["pi"]["extensions"]:
    check((ROOT / rel).is_file(), f"pi extension {rel} exists")
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
headings = re.findall(r"^## (.+)$", changelog, re.M)
check(
    bool(headings) and all(re.fullmatch(r"\d{8}-\d{4}", h) for h in headings),
    "CHANGELOG.md headings are YYYYMMDD-HHMM timestamps",
)
check(headings == sorted(headings, reverse=True), "CHANGELOG.md entries are newest first")

# The skill must follow its own hard rule: no em or en dash in the prompt files.
for path in [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "hooks" / "session-start.md",
    *sorted((ROOT / "references").glob("*.md")),
]:
    text = path.read_text(encoding="utf-8")
    check(not re.search("[–—]", text), f"{path.relative_to(ROOT)} has no dashes")

sys.exit(1 if failures else 0)
