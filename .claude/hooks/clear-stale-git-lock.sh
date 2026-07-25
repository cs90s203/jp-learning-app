#!/bin/bash
# Remove stale git lock files left behind by a crashed git process.
#
# Why: the nightly content-push routine runs unattended. A leftover
# .git/HEAD.lock blocks every `git commit` forever, and the 15-minute
# retry loop can never recover from it on its own (2026-07-20 incident:
# a stale HEAD.lock silently blocked pushes for two days).
#
# Safety: only deletes a lock that is older than 60 minutes AND only when
# no git process is running anywhere on this machine. A real git operation
# never holds a lock that long in a repo this size.

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
[ -d "$REPO/.git" ] || exit 0

# Any live git process at all -> assume the lock is legitimate, do nothing.
pgrep -x git >/dev/null 2>&1 && exit 0

removed=""
for lock in HEAD.lock index.lock config.lock; do
  if [ -n "$(find "$REPO/.git/$lock" -mmin +60 2>/dev/null)" ]; then
    rm -f "$REPO/.git/$lock" && removed="$removed $lock"
  fi
done

[ -z "$removed" ] && exit 0

echo "$(date '+%Y-%m-%d %H:%M:%S') cleared stale lock:$removed" >> "$REPO/.claude/hooks/stale-lock.log"
printf '{"systemMessage":"🔓 已自動清除 stale git lock:%s（超過 60 分鐘且無 git 程序在跑）"}\n' "$removed"
exit 0
