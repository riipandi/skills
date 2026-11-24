#!/bin/sh
# Session hook for Claude Code and Codex. What it prints is added to the model's context.
#
#   hook.sh session-start          print the rules for every skill that is on
#   hook.sh prompt                 read the hook's JSON on stdin and handle a toggle command
#   hook.sh toggle on|off|status   change or report the prompt-optimizer state
set -eu

root=$(cd "$(dirname "$0")/.." && pwd)
state_dir="${XDG_CONFIG_HOME:-$HOME/.config}/riipandi-skills"
# The flag marks "off" so that a fresh install, with no file, starts on.
flag="$state_dir/prompt-optimizer-off"

toggle() {
  case "$1" in
  on)
    rm -f "$flag"
    echo "PROMPT OPTIMIZER ON. Saved for this session and new ones. Follow these rules from now on:"
    echo
    cat "$root/hooks/prompt-optimizer-rules.md"
    ;;
  off)
    mkdir -p "$state_dir"
    : >"$flag"
    echo "PROMPT OPTIMIZER OFF. Saved for this session and new ones. Stop applying the prompt optimizer rules to the user's messages. The prompt-optimizer skill still works when the user asks for a prompt."
    ;;
  status)
    if [ -f "$flag" ]; then
      echo "PROMPT OPTIMIZER STATUS: off."
    else
      echo "PROMPT OPTIMIZER STATUS: on."
    fi
    ;;
  *)
    echo "usage: hook.sh toggle on|off|status" >&2
    exit 2
    ;;
  esac
}

case "${1:-}" in
session-start)
  cat "$root/hooks/clarity-language-rules.md"
  if [ ! -f "$flag" ]; then
    echo
    cat "$root/hooks/prompt-optimizer-rules.md"
  fi
  ;;
prompt)
  # Match only a prompt that starts with the command, so ordinary prose never toggles it.
  arg=$(grep -oE '"prompt"[[:space:]]*:[[:space:]]*"[/$@]([a-z-]+:)?prompt-optimizer[[:space:]]+(on|off|status)([[:space:]]|\\n)*"' | grep -oE '(on|off|status)([[:space:]]|\\n)*"$' | grep -oE '^[a-z]+' || true)
  if [ -n "$arg" ]; then
    toggle "$arg"
  fi
  ;;
toggle)
  toggle "${2:-}"
  ;;
*)
  echo "usage: hook.sh session-start | prompt | toggle on|off|status" >&2
  exit 2
  ;;
esac
