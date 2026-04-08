#!/bin/bash
# 小诸葛仓库初始化脚本
# 由小诸葛生成，供叶公执行

set -e

echo "=========================================="
echo "  小诸葛独立仓库初始化"
echo "=========================================="

# 配置变量
REPO_NAME="xiaozhuge-agent"
GITHUB_USER="alexyegong"
WORKSPACE_DIR="/root/.openclaw/workspace"

cd "$WORKSPACE_DIR"

echo ""
echo "步骤 1/5: 检查 Git 配置..."
if ! git config --global user.name >/dev/null 2>&1; then
    echo "  ⚠️  Git user.name 未设置"
    echo "     请运行: git config --global user.name '你的名字'"
    exit 1
fi
if ! git config --global user.email >/dev/null 2>&1; then
    echo "  ⚠️  Git user.email 未设置"
    echo "     请运行: git config --global user.email '你的邮箱'"
    exit 1
fi
echo "  ✅ Git 配置已就绪"

echo ""
echo "步骤 2/5: 创建初始提交..."
# 添加所有非忽略文件
git add .
git commit -m "feat: 小诸葛初始记忆与身份配置

- 添加 MEMORY.md 长期记忆
- 添加 IDENTITY.md 身份定义（小诸葛）
- 添加 SOUL.md 人格锚点
- 添加 USER.md 用户信息（叶公）
- 添加 AGENTS.md 工作指南
- 添加 TOOLS.md 本地工具配置
- 添加 memory/ 每日记录（2026-03-09 至 2026-03-22）
- 添加 .gitignore 敏感信息保护

Created-by: 小诸葛
Date: $(date +%Y-%m-%d)" || echo "  无新变更需要提交"

echo ""
echo "步骤 3/5: 准备推送到远程..."
echo ""
echo "  ⚠️  请先在 GitHub 上创建空仓库:"
echo "     https://github.com/new"
echo ""
echo "     仓库名称: $REPO_NAME"
echo "     可见性: Private（推荐）或 Public"
echo "     ✅ 不要初始化 README（已由本地提交）"
echo ""
read -p "  按 Enter 确认已在 GitHub 创建仓库..."

echo ""
echo "步骤 4/5: 配置远程仓库..."
read -p "  使用 HTTPS 还是 SSH? [https/ssh, 默认 https]: " PROTOCOL
PROTOCOL=${PROTOCOL:-https}

if [ "$PROTOCOL" = "ssh" ]; then
    REMOTE_URL="git@github.com:$GITHUB_USER/$REPO_NAME.git"
else
    REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"
fi

# 移除现有远程（如果有）
git remote remove origin 2>/dev/null || true
# 添加新远程
git remote add origin "$REMOTE_URL"
echo "  ✅ 远程仓库已配置: $REMOTE_URL"

echo ""
echo "步骤 5/5: 推送代码..."
if [ "$PROTOCOL" = "https" ]; then
    echo "  ℹ️  将提示输入 GitHub Personal Access Token"
    echo "     可在 https://github.com/settings/tokens 创建"
    echo "     所需权限: repo"
    echo ""
fi

git push -u origin master || git push -u origin main
echo ""
echo "  ✅ 推送完成！"

echo ""
echo "=========================================="
echo "  仓库地址: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "=========================================="
