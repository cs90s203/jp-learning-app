#!/bin/bash
# ============================================================
# deploy.sh — 日語學習 App 自動部署腳本
# 用法：./deploy.sh <版本號> "<變更摘要>"
# 例如：./deploy.sh v0.0.2 "實作內容包系統，文章可依日期切換"
# ============================================================

set -e

VERSION="$1"
SUMMARY="$2"
DATE=$(date +%Y-%m-%d)
CHANGELOG="Released/CHANGELOG.md"

# --- 驗證參數 ---
if [ -z "$VERSION" ] || [ -z "$SUMMARY" ]; then
  echo "❌ 用法：./deploy.sh <版本號> \"<變更摘要>\""
  echo "   例如：./deploy.sh v0.0.2 \"修正長按面板關閉問題\""
  exit 1
fi

echo "🚀 開始部署 $VERSION ..."

# --- 更新 CHANGELOG ---
echo "📝 更新 CHANGELOG..."
ENTRY="\n## $VERSION — $DATE\n\n$SUMMARY\n\n---"

# 在第一個 --- 後插入新版本
awk -v entry="$ENTRY" '
/^---$/ && !found {
  print
  print entry
  found=1
  next
}
{ print }
' "$CHANGELOG" > /tmp/changelog_tmp && mv /tmp/changelog_tmp "$CHANGELOG"

# --- Git commit & push ---
echo "📦 Commit 中..."
git add -A
git commit -m "$VERSION: $SUMMARY"

echo "⬆️  推送到 GitHub..."
git push origin main

echo ""
echo "✅ 部署完成！"
echo "   版本：$VERSION"
echo "   內容：$SUMMARY"
echo "   URL：https://cs90s203.github.io/jp-learning-app/Released/jp_learning_mvp.html"
echo ""
echo "📱 約 1-2 分鐘後可在手機開啟上方連結測試"
