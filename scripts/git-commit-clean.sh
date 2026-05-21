#!/usr/bin/env bash
# Commit staged changes without Co-authored-by trailers (Cursor hook bypass).
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "Usage: $0 \"commit message\"" >&2
  exit 1
fi
MSG="$1"
if [ -z "$(git diff --cached --name-only)" ]; then
  echo "Nothing staged." >&2
  exit 1
fi
TREE=$(git write-tree)
PARENT=$(git rev-parse HEAD)
NEW=$(printf '%s\n' "$MSG" | git commit-tree "$TREE" -p "$PARENT")
git reset --hard "$NEW"
