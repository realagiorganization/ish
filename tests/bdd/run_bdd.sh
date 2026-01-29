#!/usr/bin/env bash
set -euo pipefail

CODEX_KEY="${CODEX_API_KEY:-${OPENAI_API_KEY:-}}"
TAGS=()
if [[ -z "$CODEX_KEY" ]]; then
  TAGS+=("--tags" "~@codex")
fi

python3 -m behave tests/bdd/features "${TAGS[@]}"
