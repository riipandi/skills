#!/usr/bin/env bash
# Lint and format check for every file type in the repo. Needs uv and Node.
#
#   scripts/check.sh         report problems, change nothing
#   scripts/check.sh --fix   rewrite what can be fixed, then report the rest
set -euo pipefail
cd "$(dirname "$0")/.."

# Pinned so a new tool release cannot fail the check on unchanged files.
rumdl=(uvx rumdl@0.3.6)
ruff=(uvx ruff@0.17.6)
shellcheck=(uvx --from shellcheck-py==0.11.0.1 shellcheck)
shfmt=(uvx --from shfmt-py==4.2.0 shfmt -i 2)
oxlint=(npx --yes oxlint@1.95.0 --deny-warnings)
oxfmt=(npx --yes oxfmt@0.80.0)
shell_files=(scripts/*.sh hooks/*.sh)

if [[ "${1:-}" == "--fix" ]]; then
  "${rumdl[@]}" fmt .
  "${ruff[@]}" format .
  # Unfixable findings are reported by the check below.
  "${ruff[@]}" check --fix . || true
  "${ruff[@]}" format .
  "${oxlint[@]}" --fix || true
  "${oxfmt[@]}"
  "${shfmt[@]}" -w "${shell_files[@]}"
fi

echo "== Markdown (rumdl)"
"${rumdl[@]}" check .
echo "== Python (ruff)"
"${ruff[@]}" check .
"${ruff[@]}" format --check .
echo "== TypeScript (oxlint)"
"${oxlint[@]}"
echo "== TypeScript, JSON, YAML, TOML (oxfmt)"
"${oxfmt[@]}" --check
echo "== Shell (shellcheck, shfmt)"
"${shellcheck[@]}" "${shell_files[@]}"
"${shfmt[@]}" -d "${shell_files[@]}"
echo "== Package (validate_package.py)"
python3 scripts/validate_package.py >/dev/null || python3 scripts/validate_package.py | grep FAIL
echo "All checks passed."
