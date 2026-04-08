# GitHub Personal Access Token 创建指南

## 步骤 1：打开 Token 设置页面

访问：
**https://github.com/settings/tokens/new**

或者手动导航：
1. 登录 GitHub
2. 点击右上角头像 → **Settings**
3. 左侧菜单最下方 → **Developer settings**
4. 点击 **Personal access tokens** → **Tokens (classic)**
5. 点击右上角 **Generate new token** → 选择 **Generate new token (classic)**

## 步骤 2：填写 Token 信息

| 字段 | 填写内容 |
|------|---------|
| **Note** | `xiaozhuge-agent push` （随便写，自己认得就行）|
| **Expiration** | **No expiration** （或选 30/60/90 天）|

## 步骤 3：选择权限（Scopes）

勾选以下权限：

- [x] **repo** （完整仓库访问）
  - [x] repo:status
  - [x] repo_deployment
  - [x] public_repo
  - [x] repo:invite
  - [x] security_events

（直接勾选最上面的 **repo** 即可，会自动包含所有子权限）

## 步骤 4：生成 Token

点击页面底部绿色按钮 **Generate token**

⚠️ **重要**：生成的 Token 只显示一次！请立即复制保存。

Token 格式类似：
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 步骤 5：给我 Token 或自己推送

### 选项 A：给我 Token（最快）
直接把 Token 发给我，我立即完成推送。

### 选项 B：自己推送
在终端执行：
```bash
cd /root/.openclaw/workspace
git push https://alexyegong:ghp_xxxxxxxx@github.com/alexyegong/xiaozhuge-agent.git master
```

---

## 示意图

```
GitHub → Settings → Developer settings → Personal access tokens
                                                    ↓
                                         Generate new token (classic)
                                                    ↓
                                         Note: xiaozhuge-agent push
                                         Expiration: No expiration
                                         Scopes: [x] repo
                                                    ↓
                                         Generate token
                                                    ↓
                                         复制 ghp_xxxxxxxx...
```

---

## 安全提示

- Token 相当于密码，不要公开分享
- 如果不小心泄露，立即到 GitHub 删除该 Token
- 可以设置过期时间（Expiration）增加安全性
- 建议每个项目使用不同的 Token
