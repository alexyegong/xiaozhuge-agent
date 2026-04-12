# gstack 集成指南

## 简介
gstack 是 Y Combinator 总裁 Garry Tan 开源的 AI 编程工作流工具，已适配 OpenClaw。

## 已安装的技能

| 技能 | 用途 | Emoji |
|------|------|-------|
| `gstack-openclaw-ceo-review` | CEO/创始人模式规划审查，4种模式（范围扩展/选择性扩展/保持范围/范围缩减） | 👑 |
| `gstack-openclaw-investigate` | 事故调查，深入分析问题根因 | 🔍 |
| `gstack-openclaw-office-hours` | 设计文档生成（问题陈述、前提、替代方案） | 📋 |
| `gstack-openclaw-retro` | 工程回顾，分析提交历史和工作模式 | 🔄 |

## 分发级别（Dispatch Tiers）

### SIMPLE（简单任务）
- **场景**: 单文件更改、typo 修复、配置更新
- **方式**: `sessions_spawn(runtime: "acp", prompt: "<任务>")`

### MEDIUM（中等任务）
- **场景**: 多文件功能、重构、技能编辑
- **方式**: 注入 `gstack-lite-CLAUDE.md` 后执行

### HEAVY（重度任务）
- **场景**: 需要特定 gstack 方法论（/cso, /review, /qa, /ship）
- **技能**: /cso, /review, /qa, /ship, /investigate, /design-review, /benchmark, /gstack-upgrade

### FULL（完整功能）
- **场景**: 完整功能构建、多天范围、需要规划+审查
- **管道**: /autoplan → implement → /ship → report
- **方式**: 注入 `gstack-full-CLAUDE.md` 后执行

### PLAN（规划模式）
- **场景**: 规划项目、功能规格、设计（不实现）
- **管道**: /office-hours → /autoplan → 保存计划
- **方式**: 注入 `gstack-plan-CLAUDE.md` 后执行
- **输出**: `plans/<project-slug>-plan-<date>.md`

## AI Agent Community 集成方案

### 小诸葛（协调中枢）
- **角色**: 使用 PLAN 模式做项目规划
- **配置**: `gstack-plan-CLAUDE.md`
- **流程**:
  1. /office-hours 生成设计文档
  2. /autoplan 审查设计（CEO + eng + design + DX + codex adversarial）
  3. 保存计划到 `plans/` 目录
  4. 报告计划摘要和决策

### 小叶子（Local OpenCode）
- **角色**: 使用 FULL 模式实现功能
- **配置**: `gstack-full-CLAUDE.md`
- **流程**:
  1. 读取 CLAUDE.md 和项目上下文
  2. /autoplan 审查方法
  3. 实现批准的计划
  4. /ship 创建 PR
  5. 报告 PR URL 和决策

### 小无疾（审查者）
- **角色**: 使用 HEAVY 模式进行审查
- **技能**: /review, /investigate
- **重点**: 找出通过 CI 但生产环境会爆炸的 bug

## 触发词

当用户提到以下内容时，应使用相应的 gstack 技能：

- "CEO review", "创始人视角", "挑战前提", "扩大范围", "10星产品"
  → `gstack-openclaw-ceo-review`

- "调查问题", "事故分析", "根因分析", "为什么失败了"
  → `gstack-openclaw-investigate`

- "设计文档", "规划项目", "规格说明", "替代方案"
  → `gstack-openclaw-office-hours`

- "回顾", "周报", "效率分析", "工作模式"
  → `gstack-openclaw-retro`

## 重要规则

1. **Always spawn, never redirect** — 总是 spawn 一个 ACP session，不要让用户自己去打开 Claude Code
2. **Resolve the repo** — 如果用户指定了仓库或项目，设置工作目录到该路径
3. **Autoplan runs end-to-end** — 对于 /autoplan，spawn session 并让它运行完整的审查管道
4. **Do not implement in PLAN mode** — 规划模式只规划，不实现

## 决策启发式

- 能在 <10 行代码内完成？ → **SIMPLE**
- 触及多个文件但方法明显？ → **MEDIUM**
- 用户指定特定技能（/cso, /review, /qa）？ → **HEAVY**
- "升级 gstack", "更新 gstack" → **HEAVY** + `Run /gstack-upgrade`
- 是功能、项目或目标（不是任务）？ → **FULL**
- 想要规划但不实现？ → **PLAN**

## 参考资料

- gstack GitHub: https://github.com/garrytan/gstack
- Star: 61K+
- 作者: Garry Tan (Y Combinator CEO)

---

**安装时间**: 2026-04-12 16:52
**安装路径**: `/workspace/projects/workspace/skills/`
**源路径**: `~/.claude/skills/gstack/openclaw/skills/`
