#!/bin/bash
# auto_push_content.sh
# 由 launchd 每天 00:05 自動執行，將 Cowork 排程生成的 content JSON push 到 GitHub

cd /Users/mick/Documents/Projects/Language || exit 1

TODAY=$(date +%Y-%m-%d)

# 如果 content/ 沒有任何變動，直接結束
if git diff --quiet HEAD -- content/ && git ls-files --others --exclude-standard content/ | grep -q '^'; then
  : # 有 untracked 新檔案，繼續
elif git diff --quiet HEAD -- content/; then
  echo "[$TODAY] 無新 content，跳過 push"
  exit 0
fi

git add content/
git commit -m "content: $TODAY auto-push" || { echo "[$TODAY] commit 失敗（可能沒有新檔案）"; exit 0; }
git push origin main && echo "[$TODAY] push 完成 ✅" || echo "[$TODAY] push 失敗 ❌"
