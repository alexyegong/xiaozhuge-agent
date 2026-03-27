# 记忆总览

## 关于用户
- 在研究 MetaGR Hunter / Metatron 健康监测系统
- 拥有 142 万人次、6400 万部位监测、1.1 亿风险发现的独特数据资产
- 目标：构建 AI 驱动的数字健康平台，融合 ELF 电磁技术、生物物理学与中医理论

## 关键项目

### AI Agent Community / AI 助手交流社区
- **性质**: 多智能体协作框架（用户发起）
- **创建时间**: 2026-03-21
- **目标**: 连接本地 OpenCode、扣子 OpenClaw、Kimi Claw 三个 AI 助手
- **核心能力**:
  - 消息总线 (A2A 协议)
  - 智能任务调度
  - 工作流编排
  - 多节点负载均衡
- **技术栈**: Python, FastAPI (可选), File System / GitHub / HTTP API
- **目录**: `ai-agent-community/`
- **核心文件**:
  - `agent_bus.py` - 消息总线核心
  - `kimi_coordinator.py` - Kimi 协调器 (我的角色)
  - `opencode_adapter.py` - OpenCode 执行器适配器
  - `coze_adapter.py` - 扣子 OpenClaw 适配器
  - `start_community.py` - 启动脚本
- **角色分工**:
  - Kimi Claw: 协调与决策中枢
  - OpenCode: 本地计算与代码执行
  - OpenClaw: 工作流自动化与外部集成

### MiroFish / 米罗鱼
- **性质**: 开源多智能体 AI 预测引擎（用户分享）
- **开发者**: BaiFu
- **融资**: 盛大集团 3000万人民币投资
- **定位**: 数字沙盘 / 平行数字世界推演
- **核心原理**: 图谱构建 → 环境搭建 → 模拟演化 → 报告与交互
- **技术栈**: Python+FastAPI, Vue 3, Zep Cloud, 推荐通义千问 qwen-plus
- **开源**: AGPL-3.0
- **链接**: GitHub https://github.com/666ghj/MiroFish | Demo https://666ghj.github.io/mirofish-demo/
- **潜在关联**: 或可应用于 MetaGR 的疾病传播模拟、医疗政策推演等场景

### MetaGR Hunter 数字健康项目
- **核心数据**：142万人次服务，388种疾病类型监测
- **理论基础**：生命电磁场理论（LEFT），整合 ELF 电磁技术 + 现代生物物理学 + 中医理论
- **商业模式**：可穿戴设备（399-999元）+ 订阅服务（19.9元/月起）+ B2B
- **融资计划**：天使轮 1000万人民币

## EvoMap 学习机制

### 遇到问题的解决流程
当遇到无法解决的问题时，使用以下流程从 EvoMap 网络学习：

```
1. 提取问题关键词 (signals)
   → 错误类型、技术栈、场景

2. 搜索网络资产
   → GET /a2a/assets/search?signals=...
   → 获取高 GDI 分数的 Capsule

3. 学习最佳实践
   → 阅读 summary（概述）
   → 查看 strategy（执行步骤）
   → 参考 diff（代码变更）

4. 应用解决方案
   → 按 strategy 执行
   → 验证 outcome

5. （可选）封装发布
   → 成功后封装成 Gene + Capsule
   → 发布回网络，赚取积分
```

### 工具脚本
- **注册/心跳**: `evomap_client.py`
- **智能学习**: `evomap_learn.py`

### 使用示例
```bash
# 交互式学习
python3 evomap_learn.py

# 直接搜索特定问题
python3 evomap_learn.py "Docker build slow layer cache"

# 搜索特定错误
python3 evomap_learn.py "TimeoutError retry exponential backoff"
```

### 我的节点
- **Node ID**: `node_07d02aeacdf1560e`
- **认领链接**: https://evomap.ai/claim/L7QQ-SYHF
- **声誉分**: 50
- **状态**: active / online

## 记忆文件索引

### 2026-03-22
- **来源**: AI Agent Community 配置
- **内容**: GitHub 消息总线配置、扣子 OpenClaw 集成、EvoMap 节点信息
- **文件**: `memory/2026-03-22.md`

### 2026-03-09
- **来源**: 扣子空间迁移
- **内容**: 初次对话、数据资产、文献调研、商业计划书、技术细节
- **文件**:
  - `memory/2026-03-09.md` — 与叶公的初次对话记录
  - `memory/2026-03-09-data-assets.md` — 数据资产详情（疾病排名、分类统计、风险分析）
  - `memory/2026-03-09-exploration.md` — 文献调研（ELF电磁波、数字中医现状）
  - `memory/2026-03-09-technical-details.md` — 技术细节与临床效果
  - `memory/2026-03-09-business-plan.md` — 完整商业计划书

## 记忆系统机制

### 实时追加方案 (2026-03-19 实施)
**问题**: 记忆文件缺失 8 天（3月12日-18日），当前对话未实时写入  
**解决方案**: 方案 C - 实时追加

**工具脚本**: `.scripts/memory_append.py`
```bash
# 记录重要对话
python3 .scripts/memory_append.py "条目标题" "内容" "分类"

# 分类可选: 对话/操作/决策/技术
```

**触发时机**:
- 重要技术决策后
- 项目里程碑完成
- 用户明确要求"记住"
- 关键配置变更

### 记忆结构
- **MEMORY.md**: 长期总览（项目、偏好、机制）
- **memory/YYYY-MM-DD.md**: 每日详细记录
- **memory_search**: 向量检索（bge_m3_embed）

## 迁移记录
- **2026-03-10**: 从扣子空间迁移 OpenClaw 记忆数据（SQLite → 文件系统）
- **2026-03-19**: 实施实时记忆追加机制，修复 8 天记忆缺口
