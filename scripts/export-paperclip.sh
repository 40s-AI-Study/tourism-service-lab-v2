#!/bin/bash
# export-paperclip.sh — export Paperclip company state to repo
# Usage: ./scripts/export-paperclip.sh [company_id]

set -euo pipefail

API="http://127.0.0.1:3100/api"
COMPANY_ID="${1:-}"
REPO_DIR="/Users/sklee01/tourism-service-lab-v2"
OUT_DIR="${REPO_DIR}/company-config/exports"
TIMESTAMP=$(date '+%Y%m%d-%H%M%S')

_log() { echo "[export-paperclip] $(date '+%H:%M:%S') $*"; }

if [ -z "$COMPANY_ID" ]; then
  _log "ERROR: company_id required"
  echo "Usage: $0 <company-id>"
  exit 1
fi

mkdir -p "$OUT_DIR"

_log "exporting company $COMPANY_ID..."

# 1. Company info
/usr/bin/curl -s "${API}/companies/${COMPANY_ID}" -o "${OUT_DIR}/company-${TIMESTAMP}.json"

# 2. Agents
/usr/bin/curl -s "${API}/companies/${COMPANY_ID}/agents" -o "${OUT_DIR}/agents-${TIMESTAMP}.json"

# 3. Issues
/usr/bin/curl -s "${API}/companies/${COMPANY_ID}/issues?limit=200" -o "${OUT_DIR}/issues-${TIMESTAMP}.json"

# 4. Projects
/usr/bin/curl -s "${API}/companies/${COMPANY_ID}/projects" -o "${OUT_DIR}/projects-${TIMESTAMP}.json"

# 5. Recent heartbeat runs
/usr/bin/curl -s "${API}/companies/${COMPANY_ID}/heartbeat-runs?limit=50" -o "${OUT_DIR}/runs-${TIMESTAMP}.json"

# 6. Create symlink "latest" for convenience
cd "$OUT_DIR"
for kind in company agents issues projects runs; do
  ln -sf "${kind}-${TIMESTAMP}.json" "${kind}-latest.json"
done

_log "exported to $OUT_DIR/*-${TIMESTAMP}.json"
ls -la "$OUT_DIR" | head -15
