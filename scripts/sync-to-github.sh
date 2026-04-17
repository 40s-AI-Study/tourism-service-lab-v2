#!/bin/bash
# sync-to-github.sh — commit repo changes + push
# Called after each significant change (agent output, wiki update, etc.)
# Usage: ./scripts/sync-to-github.sh "commit message"

set -euo pipefail

REPO_DIR="/Users/sklee01/tourism-service-lab-v2"
MSG="${1:-auto: sync changes}"

_log() { echo "[sync-to-github] $(date '+%H:%M:%S') $*"; }

cd "$REPO_DIR"

# Scrub secrets first
if [ -x "./scripts/scrub-secrets.sh" ]; then
  ./scripts/scrub-secrets.sh --staged || {
    _log "aborting: secrets detected"
    exit 1
  }
fi

if [ -z "$(git status --porcelain)" ]; then
  _log "no changes to commit"
  exit 0
fi

git add .
git commit -m "$MSG"
git push 2>&1 | tail -3
_log "pushed: $MSG"
