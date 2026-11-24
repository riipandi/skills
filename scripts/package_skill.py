#!/usr/bin/env python3
"""Pack the skill into dist/clarity.skill (a zip with one top-level `clarity/` folder).

Usage:
    python3 scripts/package_skill.py [output-directory]
"""

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "clarity"
# Only what the agent needs at runtime, plus the license files.
INCLUDE = [
    "SKILL.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "references/*.md",
    "scripts/strip_markdown.py",
    "scripts/prose_stats.py",
]

if subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_package.py")]).returncode:
    sys.exit("Validation failed; not packaging.")

out_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "dist"
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / f"{NAME}.skill"

files = sorted(p for pattern in INCLUDE for p in ROOT.glob(pattern))
with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in files:
        archive.write(path, Path(NAME) / path.relative_to(ROOT))

assert f"{NAME}/SKILL.md" in zipfile.ZipFile(target).namelist()
print(f"\nPacked {len(files)} files into {target}")
