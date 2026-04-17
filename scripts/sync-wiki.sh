#!/bin/bash
# sync-wiki.sh — local llm-wiki (.omc/wiki/) → GitHub Wiki push
# Usage: ./scripts/sync-wiki.sh [--dry-run]

set -euo pipefail

REPO_DIR="/Users/sklee01/tourism-service-lab-v2"
WIKI_DIR="/Users/sklee01/tourism-service-lab-v2.wiki"
LOCAL_WIKI_SRC="${REPO_DIR}/.omc/wiki"  # llm-wiki content to sync
DRY_RUN="${1:-}"

_log() { echo "[sync-wiki] $(date '+%H:%M:%S') $*"; }

if [ ! -d "$WIKI_DIR" ]; then
  _log "ERROR: wiki repo not cloned at $WIKI_DIR"
  _log "Run: git clone https://github.com/sinrim11/tourism-service-lab-v2.wiki.git $WIKI_DIR"
  exit 1
fi

if [ ! -d "$LOCAL_WIKI_SRC" ]; then
  _log "WARN: no local llm-wiki at $LOCAL_WIKI_SRC — nothing to sync"
  exit 0
fi

cd "$WIKI_DIR"
git pull --rebase 2>&1 | tail -3

# Copy llm-wiki pages to wiki repo (rename to GitHub Wiki conventions)
# .omc/wiki/competition/overview.md → Competition-Overview.md
for f in "$LOCAL_WIKI_SRC"/**/*.md; do
  [ -e "$f" ] || continue
  rel="${f#$LOCAL_WIKI_SRC/}"
  # Skip internal index/log
  [[ "$rel" == "index.md" || "$rel" == "log.md" ]] && continue
  # Flatten path: competition/overview.md → Competition-Overview.md
  flat=$(echo "$rel" | sed 's|/|-|g; s|\.md$||' | awk '{for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1' OFS="-")
  dest="$WIKI_DIR/${flat}.md"
  if [ "$DRY_RUN" = "--dry-run" ]; then
    _log "[DRY] would copy: $f → $dest"
  else
    cp "$f" "$dest"
    _log "copied: $rel → ${flat}.md"
  fi
done

if [ "$DRY_RUN" = "--dry-run" ]; then
  _log "dry-run complete"
  exit 0
fi

# Commit + push if changes
cd "$WIKI_DIR"
if [ -n "$(git status --porcelain)" ]; then
  git add .
  git commit -m "sync: llm-wiki → GitHub Wiki $(date '+%Y-%m-%d %H:%M')"
  git push 2>&1 | tail -2
  _log "pushed to GitHub Wiki"
else
  _log "no changes"
fi
