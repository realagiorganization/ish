#!/usr/bin/env bash
set -euo pipefail

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is required to run the Codex CLI test." >&2
  exit 1
fi

PROMPT="${1:-Say hello from the iSH BDD suite.}"
OUT_DIR="prompt_artifacts"
OUT_JSON="$OUT_DIR/codex_cli_output.json"
OUT_TEXT="$OUT_DIR/codex_cli_output.txt"
PROMPT_FILE="$OUT_DIR/codex_prompt.txt"
TMUX_LOG="$OUT_DIR/codex_tmux.log"
SESSION="codex_cli_$$"

mkdir -p "$OUT_DIR"
printf "%s" "$PROMPT" > "$PROMPT_FILE"

CMD="python3 tools/codex_cli.py --prompt-file \"$PROMPT_FILE\" --out-json \"$OUT_JSON\" --out-text \"$OUT_TEXT\"; tmux wait-for -S codex_cli_done"

tmux new-session -d -s "$SESSION" "$CMD"
tmux wait-for codex_cli_done

tmux capture-pane -p -t "$SESSION" > "$TMUX_LOG"
tmux kill-session -t "$SESSION"
