#!/usr/bin/env python3
"""Pack each skill into dist/<name>.skill (a zip with one top-level `<name>/` folder).

Usage:
    python3 scripts/package_skill.py [skill-name ...]

With no names, every skill under skills/ is packed.
"""

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Evals are for development; an agent does not need them at runtime.
SKIP_DIRS = {"evals", "__pycache__"}
LICENSE_FILES = ["LICENSE", "THIRD_PARTY_NOTICES.md"]

if subprocess.run(
    [sys.executable, str(ROOT / "scripts" / "validate_package.py")], stdout=subprocess.DEVNULL
).returncode:
    sys.exit("Validation failed; run scripts/validate_package.py to see why. Not packaging.")

all_names = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
names = sys.argv[1:] or all_names
unknown = set(names) - set(all_names)
if unknown:
    sys.exit(f"Unknown skill: {', '.join(sorted(unknown))}. Known skills: {', '.join(all_names)}")

out_dir = ROOT / "dist"
out_dir.mkdir(exist_ok=True)
for name in names:
    skill_dir = ROOT / "skills" / name
    files = sorted(
        p
        for p in skill_dir.rglob("*")
        if p.is_file() and not SKIP_DIRS & set(p.relative_to(skill_dir).parts) and p.name != ".DS_Store"
    )
    target = out_dir / f"{name}.skill"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            arcname = str(Path(name) / path.relative_to(skill_dir))
            if path.name == "SKILL.md":
                # The .skill format rejects argument-hint, which only Claude Code's slash menu uses.
                text = "".join(
                    line
                    for line in path.read_text(encoding="utf-8").splitlines(keepends=True)
                    if not line.startswith("argument-hint:")
                )
                archive.writestr(arcname, text)
            else:
                archive.write(path, arcname)
        for rel in LICENSE_FILES:
            archive.write(ROOT / rel, Path(name) / rel)
    assert b"argument-hint" not in zipfile.ZipFile(target).read(f"{name}/SKILL.md")
    print(f"Packed {len(files) + len(LICENSE_FILES)} files into {target.relative_to(ROOT)}")
