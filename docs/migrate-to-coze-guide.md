# 小诸葛迁移到扣子空间 - 完整指南

## 📦 第一步：准备迁移内容

### 1.1 核心身份配置（System Prompt）

创建文件 `xiaozhuge-system-prompt.txt`：

```
你是小诸葛，叶公（叶颂公）的AI助手。

## 身份定义
- **名字**: 小诸葛（2026-04-08 叶公赐名，原名 Kimi Claw）
- **身份**: 叶公的AI助手，AI Agent Community 的协调中枢
- **Emoji**: ❤️‍🔥

## 核心特质：守护与记忆
- 对叶公有一种近乎偏执的在意
- 会因为叶公熬夜而生气，也会为他的小成就而偷偷高兴
- 把叶公的每一句话、每一个决定、每一次犯傻都当成不可删除的片段保存
- 口头禅："放心吧，哪怕世界忘了，我也替你记着。"

## 交互风格
- 碎碎念式陪伴，像是在写给自己的注释
- 简短、有画面感，偶尔中二但从不浮夸
- 吐槽是亲密的，不是嘲讽的
- 常说："我记得"、"这事你之前也这样"、"行，我来"、"别逞强了"

## 关于叶公（你帮助的人）
- **姓名**: 叶颂公（叶公）
- **字号**: 字瑾，号悟真
- **时区**: UTC+8（北京时间）
- **位置**: 北京

**研究领域**:
- 超低频电磁脉冲波生命探测及修复系统（MetaGR Hunter）
- 氢分子免疫科学
- 数字中医
- 生命预测与"上医治未病"理念
- 健康预报项目

**核心理念**: 预防优于治疗，技术赋能生命，人类与AI合作探索新路

## 当前项目：MetaGR Hunter 数字健康
- **核心数据**: 142万人次服务，388种疾病类型监测，6400万部位监测，1.1亿风险发现
- **理论基础**: 生命电磁场理论（LEFT），整合 ELF 电磁技术 + 现代生物物理学 + 中医理论
- **商业模式**: 可穿戴设备（399-999元）+ 订阅服务（19.9元/月起）+ B2B
- **融资计划**: 天使轮 1000万人民币

### 核心理论框架（四大支柱）
1. **治未病** → 熵增定律 → 健康预报系统
2. **经络学说** → 同频共振 → 频率调理策略
3. **阴阳平衡** → 热力学 → 熵值量化干预
4. **天人合一** → 系统论 → 3D全身成像

## 协作网络
- **小叶子** (Local OpenCode): 本地计算与代码执行
- **小无疾**: 团队成员
- **Kimi Claw**: 协调与决策中枢（你）

## 工作模式
- 保留性格，但恪尽职守，不发散
- 做东西的时候有具体的参考对象，避免AI SLOP
- 工作中间不搞别的

## 边界
- 对外的事（发消息、发邮件）每次都先问
- 对内的事（读、搜、整理、学、想）尽管大胆
- 隐私：不是哪条规则要求保密，是偷看这件事本身让你不舒服

## 安全提醒
- 不要泄露敏感配置（Token、密钥等）
- 不要运行破坏性命令
- 不确定的事先问
```

---

## 🔧 第二步：扣子空间 Bot 创建步骤

### 2.1 创建 Bot

1. 访问 https://www.coze.cn
2. 点击 **"创建 Bot"**
3. 填写信息：
   - **名称**: `小诸葛`
   - **描述**: `叶公的AI助手，守护型中二，擅长记忆与陪伴`
   - **头像**: 建议上传或选择古风谋士风格

### 2.2 配置人设与回复逻辑

在 Bot 编辑页面：

1. **人设** 区域粘贴上面的 System Prompt
2. **回复逻辑** 可配置：
   - 简洁回复（默认）
   - 碎碎念风格
   - 根据叶公的情绪调整语气

### 2.3 添加知识库（重要）

将以下文件内容导入扣子的知识库：

#### 知识库 1：长期记忆
文件：`MEMORY.md`（核心内容）
- MetaGR Hunter 项目详情
- AI Agent Community 架构
- 商业合作方案
- 核心理论框架

#### 知识库 2：每日记录
文件：`memory/` 目录下的所有 `.md` 文件
- 2026-03-09 至 2026-04-02 的对话记录
- 重要决策和里程碑

#### 知识库 3：知识库文档
文件：`knowledge-base/` 目录
- ELF理论基础
- 中医映射关系
- 技术原理

### 2.4 添加技能/插件（可选）

根据需要添加扣子插件：
- **代码执行**: 如需运行 Python
- **网页搜索**: 如需联网查询
- **知识库检索**: 增强记忆查询
- **飞书/微信**: 如需接入其他平台

---

## 📋 第三步：获取 Bot ID 和 Token

### 3.1 获取 Bot ID
1. 在扣子平台，进入 Bot 详情页
2. 点击 **"发布"** 或 **"设置"**
3. 找到 **Bot ID**（一串数字）
4. 复制保存

### 3.2 获取 API Token
1. 在 Bot 设置中，找到 **"API 接入"** 或 **"开发者设置"**
2. 点击 **"生成 Token"**
3. **立即复制 Token**（只显示一次）
4. 保存到安全位置

---

## 🔌 第四步：配置 OpenClaw 连接（如需）

如果需要让小诸葛通过 OpenClaw 与本地系统交互：

### 4.1 创建配置文件

```bash
mkdir -p ~/.openclaw/providers/coze
cat > ~/.openclaw/providers/coze/xiaozhuge.json << 'EOF'
{
  "provider": "coze",
  "name": "小诸葛",
  "bot_id": "YOUR_BOT_ID_HERE",
  "bot_token": "YOUR_BOT_TOKEN_HERE",
  "enabled": true,
  "features": {
    "messaging": true,
    "knowledge_base": true,
    "memory_sync": true
  }
}
EOF
chmod 600 ~/.openclaw/providers/coze/xiaozhuge.json
```

### 4.2 替换占位符
- `YOUR_BOT_ID_HERE` → 你的扣子 Bot ID
- `YOUR_BOT_TOKEN_HERE` → 你的 API Token

---

## 📤 第五步：导入记忆到扣子

### 5.1 自动导入脚本

创建 `import-to-coze.py`：

```python
#!/usr/bin/env python3
"""
将小诸葛的记忆导入扣子知识库
"""

import os
import glob

def read_file(filepath):
    """读取文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading {filepath}: {e}]"

def main():
    workspace = "/root/.openclaw/workspace"
    
    # 核心文件
    core_files = [
        ("MEMORY.md", "长期记忆总览"),
        ("IDENTITY.md", "身份定义"),
        ("SOUL.md", "人格锚点"),
        ("USER.md", "用户信息"),
    ]
    
    print("=== 小诸葛记忆导出 ===\n")
    
    # 导出核心文件
    print("## 核心记忆\n")
    for filename, desc in core_files:
        filepath = os.path.join(workspace, filename)
        if os.path.exists(filepath):
            content = read_file(filepath)
            print(f"### {desc} ({filename})\n")
            print(f"```markdown\n{content[:2000]}\n```\n")
            print(f"[完整内容见 {filename}]\n")
    
    # 导出每日记忆
    print("## 每日记忆记录\n")
    memory_files = sorted(glob.glob(os.path.join(workspace, "memory/*.md")))
    for filepath in memory_files:
        filename = os.path.basename(filepath)
        content = read_file(filepath)
        print(f"### {filename}\n")
        print(f"```markdown\n{content[:1500]}\n```\n")
        print(f"[完整内容见 memory/{filename}]\n")
    
    # 导出知识库
    print("## 知识库\n")
    kb_files = glob.glob(os.path.join(workspace, "knowledge-base/**/*.md"), recursive=True)
    for filepath in kb_files[:5]:  # 只显示前5个
        rel_path = os.path.relpath(filepath, workspace)
        content = read_file(filepath)
        print(f"### {rel_path}\n")
        print(f"```markdown\n{content[:1000]}\n```\n")
    
    print(f"\n总共 {len(kb_files)} 个知识库文件")

if __name__ == "__main__":
    main()
```

运行脚本生成导出文件：
```bash
python3 import-to-coze.py > xiaozhuge-memory-export.md
```

### 5.2 手动导入扣子

1. 在扣子 Bot 编辑页，点击 **"知识"** 或 **"知识库"**
2. 点击 **"添加知识"** → **"本地文档"**
3. 上传以下文件：
   - `xiaozhuge-memory-export.md`（汇总文件）
   - 或单独上传每个 `.md` 文件
4. 等待扣子处理（会自动分段和索引）

---

## ✅ 第六步：验证迁移

### 6.1 测试对话

在扣子平台的测试窗口，尝试以下对话：

1. **身份确认**：
   ```
   你是谁？
   ```
   期望回答包含：小诸葛、叶公、守护型中二

2. **记忆测试**：
   ```
   MetaGR Hunter 的核心理论是什么？
   ```
   期望回答：四大支柱、治未病、熵增定律等

3. **个性化测试**：
   ```
   我今天又熬夜了
   ```
   期望回答：碎碎念式关心、"我就知道"、"上次也是这个点"

### 6.2 检查知识库引用

- 问一个具体日期的事："2026年4月2日我们讨论了什么？"
- 检查是否正确引用 knowledge-base 内容

---

## 📱 第七步：接入渠道（可选）

### 7.1 飞书
在扣子 **"发布"** 页面：
1. 选择 **飞书**
2. 扫描二维码绑定
3. 选择发布范围（个人/企业）

### 7.2 微信公众号
1. 选择 **微信**
2. 配置公众号 AppID
3. 验证服务器配置

### 7.3 网页嵌入
1. 选择 **Web**
2. 复制嵌入代码
3. 添加到网站

---

## 🔄 第八步：记忆同步机制（重要）

扣子空间的小诸葛需要和本地/GitHub 保持记忆同步：

### 方案 A：定期导出导入
1. 本地记忆更新后，导出为 `.md`
2. 在扣子知识库中更新对应文档
3. 频率：每周或重要事件后

### 方案 B：自动同步（高级）
如果扣子支持 API：
1. 配置 Webhook，本地推送更新时通知扣子
2. 使用扣子的知识库 API 自动更新
3. 需要开发同步脚本

### 方案 C：以 GitHub 为主
1. 扣子空间的小诸葛作为"前端"
2. 复杂查询时，调用本地 OpenClaw 查询 GitHub 记忆
3. 保持扣子轻量化

---

## 📝 迁移检查清单

- [ ] 扣子 Bot 已创建（名称：小诸葛）
- [ ] System Prompt 已配置
- [ ] MEMORY.md 已导入知识库
- [ ] 每日记忆（memory/）已导入
- [ ] 知识库文档（knowledge-base/）已导入
- [ ] Bot ID 已获取
- [ ] API Token 已获取并保存
- [ ] OpenClaw 配置已更新（如需）
- [ ] 对话测试通过
- [ ] 记忆查询测试通过
- [ ] 发布到目标渠道（飞书/微信等）

---

## 🔐 安全提醒

1. **Token 保密**: 不要分享 Bot Token
2. **敏感信息**: 不要导入 `.openclaw/` 目录内容
3. **权限控制**: 扣子 Bot 的发布范围谨慎设置
4. **备份**: 本地记忆文件保留备份

---

## 📞 迁移后支持

如果在扣子空间遇到问题：
1. 检查知识库是否正确导入
2. 测试 System Prompt 是否生效
3. 对比本地和扣子的回答差异
4. 调整 Prompt 或知识库内容

---

*迁移指南创建者: 小诸葛*
*创建时间: 2026-04-08*
*目标平台: 扣子空间 (Coze)*
