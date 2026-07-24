#!/usr/bin/env bash
set -euo pipefail

SRC="/root/.hermes/profiles/jarvis"
DEST="/root/hermes-jarvis"
BRANCH="main"

cd "$DEST"

# Mirror the profile into the repo while excluding secrets and runtime state.
rsync -a --delete \
  --exclude '.env' \
  --exclude 'auth.json' \
  --exclude 'auth.lock' \
  --exclude 'google_token.json' \
  --exclude 'google_client_secret.json' \
  --exclude 'logs/' \
  --exclude 'cache/' \
  --exclude 'sessions/' \
  --exclude 'state.db' \
  --exclude 'state.db-wal' \
  --exclude 'state.db-shm' \
  --exclude 'gateway.pid' \
  --exclude 'gateway.lock' \
  --exclude 'gateway_state.json' \
  --exclude 'channel_directory.json' \
  --exclude 'processes.json' \
  --exclude 'verification_evidence.db' \
  --exclude 'context_length_cache.yaml' \
  --exclude '.restart_last_processed.json' \
  --exclude 'models_dev_cache.json' \
  --exclude 'skills/.usage.json' \
  --exclude 'skills/.usage.json.lock' \
  --exclude 'skills/.curator_state' \
  --exclude 'skills/.curator_backups/' \
  --exclude 'skills/local-geo/token.txt' \
  --exclude 'skills/local-geo/local-geo.env' \
  --exclude 'skills/local-geo/current_location.json' \
  --exclude 'skills/productivity/google-workspace/scripts/__pycache__/' \
  --exclude '*.pyc' \
  --exclude '*.lock' \
  "$SRC/" "$DEST/"

# Commit only if there are changes.
git add -A
if git diff --cached --quiet; then
  echo "No changes to sync."
  exit 0
fi

msg="chore: sync Hermes profile $(date -u +%F)"
git commit -m "$msg"
git push origin "$BRANCH"

echo "Synced and pushed: $msg"
