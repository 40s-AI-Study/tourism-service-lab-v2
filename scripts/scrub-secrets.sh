#!/bin/bash
# scrub-secrets.sh — scan staged files for secrets before commit
# Usage: ./scripts/scrub-secrets.sh [--staged|--all]
# Returns 0 if clean, 1 if secrets found

set -euo pipefail

SCOPE="${1:---staged}"

# Patterns of common secret formats
PATTERNS=(
  'ghp_[A-Za-z0-9]{36}'                        # GitHub classic PAT
  'github_pat_[A-Za-z0-9_]{82}'                # GitHub fine-grained PAT
  'gho_[A-Za-z0-9]{36}'                        # GitHub OAuth
  'ghs_[A-Za-z0-9]{36}'                        # GitHub server-to-server
  'sk-[A-Za-z0-9]{20,}'                        # OpenAI API key
  'sk-ant-[A-Za-z0-9_-]{20,}'                  # Anthropic API key
  'AIza[0-9A-Za-z_-]{35}'                      # Google API key
  'AKIA[0-9A-Z]{16}'                           # AWS access key
  'xox[baprs]-[0-9]+-[0-9]+-[A-Za-z0-9]{24}'   # Slack token
  'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY'      # Private keys
  'password\s*[:=]\s*["'"'"']?[^\s"'"'"']{8,}' # password= in config
)

FOUND=0
TMPFILE=$(mktemp)

if [ "$SCOPE" = "--staged" ]; then
  FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || true)
elif [ "$SCOPE" = "--all" ]; then
  FILES=$(git ls-files 2>/dev/null || true)
else
  echo "Usage: $0 [--staged|--all]"
  exit 2
fi

if [ -z "$FILES" ]; then
  echo "[scrub] no files to check"
  rm -f "$TMPFILE"
  exit 0
fi

for file in $FILES; do
  [ -f "$file" ] || continue
  # Skip known binary / generated
  case "$file" in
    *.png|*.jpg|*.jpeg|*.gif|*.pdf|*.zip|*.tar|*.gz) continue ;;
    .git/*) continue ;;
  esac
  for pat in "${PATTERNS[@]}"; do
    if grep -HE "$pat" "$file" 2>/dev/null >> "$TMPFILE"; then
      FOUND=1
    fi
  done
done

if [ $FOUND -eq 1 ]; then
  echo "❌ SECRETS DETECTED:"
  cat "$TMPFILE"
  echo ""
  echo "Refusing commit. Remove secrets or add to .gitignore."
  rm -f "$TMPFILE"
  exit 1
fi

rm -f "$TMPFILE"
echo "✓ no secrets detected in $SCOPE files"
exit 0
