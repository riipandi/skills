#!/bin/sh
# Session hook for Claude Code and Codex. What it prints is added to the model's context.
#
#   hook.sh session-start          print the rules for every skill that is on
#   hook.sh prompt                 read the hook's JSON on stdin: handle a toggle command, or
#                                  rewrite the message when rewriting is on
#   hook.sh toggle on|off|status   change or report the prompt-optimizer state
#   hook.sh toggle "rewrite on"    turn message rewriting on ("rewrite off" turns it off)
set -eu

root=$(cd "$(dirname "$0")/.." && pwd)
state_dir="${XDG_CONFIG_HOME:-$HOME/.config}/riipandi-skills"
# The flag marks "off" so that a fresh install, with no file, starts on.
flag="$state_dir/prompt-optimizer-off"
# Rewriting costs a model call per message, so it is opt-in: this flag marks "on".
rewrite_flag="$state_dir/prompt-optimizer-rewrite-on"

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
  "rewrite on")
    mkdir -p "$state_dir"
    : >"$rewrite_flag"
    echo "PROMPT OPTIMIZER REWRITE ON. Saved for this session and new ones. From the next message on, a small model rewrites each message into a brief that arrives in a PROMPT OPTIMIZER REWRITE block. It has no effect while the prompt optimizer itself is off."
    ;;
  "rewrite off")
    rm -f "$rewrite_flag"
    echo "PROMPT OPTIMIZER REWRITE OFF. Saved for this session and new ones. Messages arrive without a rewrite block; the prompt optimizer rules are unchanged."
    ;;
  status | "rewrite status")
    state=on rewriting=off
    [ ! -f "$flag" ] || state=off
    [ ! -f "$rewrite_flag" ] || rewriting=on
    echo "PROMPT OPTIMIZER STATUS: $state. Message rewriting: $rewriting."
    ;;
  *)
    echo "usage: hook.sh toggle on|off|status|'rewrite on'|'rewrite off'" >&2
    exit 2
    ;;
  esac
}

# Writes a sharper version of the user's message to stdout, or nothing. The rewrite comes from a
# small model that sees only the message, so every failure path stays silent: the agent then
# works from the original message and the session rules.
rewrite() {
  payload=$1
  [ ! -f "$flag" ] || return 0
  [ -f "$rewrite_flag" ] || return 0
  command -v claude >/dev/null 2>&1 || return 0
  # Slash commands and very short messages are confirmations or commands, not rough prompts.
  if printf '%s' "$payload" | grep -qE '"prompt"[[:space:]]*:[[:space:]]*"([/$@!#]|[^"]{0,24}")'; then
    return 0
  fi
  # The nested session must not run this hook again, and needs none of the user's settings.
  out=$(printf '%s' "$payload" | RIIPANDI_SKILLS_NESTED=1 claude -p \
    --model "${RIIPANDI_REWRITE_MODEL:-haiku}" --setting-sources "" --strict-mcp-config \
    --disable-slash-commands --no-session-persistence --tools "" \
    --system-prompt "$(cat "$root/hooks/prompt-optimizer-rewriter.md")" 2>/dev/null) || return 0
  case "$out" in
  "" | SKIP* | *"API key"* | *"rror:"*) return 0 ;;
  esac
  echo "PROMPT OPTIMIZER REWRITE. A small model rewrote the user's latest message without seeing the conversation or the project. Use it as a sharper reading of the request, and settle its open points from the project before asking the user. The user's own words and the conversation win wherever they differ. Do not print this rewrite."
  echo
  echo "<optimized_prompt>"
  printf '%s\n' "$out"
  echo "</optimized_prompt>"
}

# A session started by rewrite() gets no rules and no rewriting.
[ -z "${RIIPANDI_SKILLS_NESTED:-}" ] || exit 0

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
  payload=$(cat)
  arg=$(printf '%s' "$payload" | grep -oE '"prompt"[[:space:]]*:[[:space:]]*"[/$@]([a-z-]+:)?prompt-optimizer[[:space:]]+(rewrite[[:space:]]+)?(on|off|status)([[:space:]]|\\n)*"' | grep -oE '(rewrite[[:space:]]+)?(on|off|status)([[:space:]]|\\n)*"$' | grep -oE '^[a-z]+([[:space:]]+[a-z]+)?' | sed -E 's/[[:space:]]+/ /g' || true)
  if [ -n "$arg" ]; then
    toggle "$arg"
  else
    rewrite "$payload"
  fi
  ;;
toggle)
  toggle "${2:-}"
  ;;
*)
  echo "usage: hook.sh session-start | prompt | toggle on|off|status|'rewrite on'|'rewrite off'" >&2
  exit 2
  ;;
esac
