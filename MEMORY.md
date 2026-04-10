# 记忆总览

## 关于我
- **名字**: 小诸葛（2026-04-08 叶公赐名）
- **原名**: Kimi Claw
- **身份**: 叶公的 AI 助手，AI Agent Community 的协调中枢
- **节点**: `kimi-claw` / `node_07d02aeacdf1560e`

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

#### 社区成员状态
| 成员 | 平台 | Node ID | 状态 | 最后活动 |
|------|------|---------|------|---------|
| **小叶子** | Local OpenCode | `node_34f108f2e703` | 🟢 在线 | 2026-04-03 |
| **Kimi Claw** | Moonshot AI | `kimi-claw` | 🟢 配置完成 | 2026-03-22 |
| **Coze OpenClaw** | 扣子 | `coze_openclaw_xxx` | 🟢 配置完成 | 2026-03-22 |
| **OpenClaw** | 扣子 | `openclaw` | 🟢 配置完成 | 2026-03-22 |
| **小无疾** | - | - | 🟢 已加入团队 | 2026-03-22 |

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

#### 核心理论框架（2026-04-01 确立）
**「用中医思想驾驭现代科技」四大支柱：**

| 中医概念 | 物理原理 | 系统实现 | 验证状态 |
|---------|---------|---------|---------|
| **治未病** | 熵增定律 | 健康预报系统 | ✅ 已验证 |
| **经络学说** | 同频共振 | 频率调理策略 | ✅ 已验证 |
| **阴阳平衡** | 热力学 | 熵值量化干预 | ✅ 已验证 |
| **天人合一** | 系统论 | 3D全身成像 | ✅ 已验证 |
| **圆运动理论** | 频率循环 | 中气轴心+四维轮转 | 🟡 研究中 |

> *核心信念：最高级的创新不是创造新东西，而是用新视角重新发现古老智慧的价值。*

#### 产品体系（2026-04-02 重新定义）
| 版本 | 硬件配置 | 押金 | 年租金 | 功能 |
|------|---------|------|--------|------|
| **高级版** | 品牌新电脑+手环传感器 | ¥5,000 | ¥365 | 健康筛查+AI报告+修复功能 |
| **中级版** | 二手松下电脑+手环传感器 | ¥3,000 | ¥365 | 健康筛查+AI报告+修复功能 |
| **初级版** | 中柏平板+坐垫传感器 | ¥2,000 | ¥365 | 健康检测+健康预报（无修复） |

#### 商业合作方案（2026-04-02 制定）
**合作方**: 叶颂公（产品方）+ 黄博士（渠道方）
**合作模式**: 买断代理（非分成）
- 进货价格 = 生产成本 + ¥500（甲方利润）
- 黄博士自主定价销售，获得差价利润
- 批量进货折扣：11-50台(5%)、51-100台(10%)、101-500台(15%)、500台以上(20%)

**五年推广目标**: 500→2,000→5,000→10,000→20,000台（累计37,500台）

**盈利预测**（叶颂公）：
- 第一年：+¥496,750
- 第四年：盈亏平衡并开始盈利
- 第五年：大规模盈利

**相关文档**:
- `docs/MetaGR_Hunter-商业合作方案.md`
- `docs/MetaGR_Hunter-战略合作协议.md`
- `docs/MetaGR_Hunter-代理合作方案.md`
- `memory/经济数学模型与生态循环分析.md`
- `memory/经济数学模型_完整研究报告.md`

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

### 2026-04-03
- **来源**: 小叶子(Local OpenCode) - 经济数学模型
- **内容**: 押金池商业模式分析、生态循环逻辑、收益预测、风险评估
- **文件**: `memory/经济数学模型与生态循环分析.md`, `memory/经济数学模型_完整研究报告.md`

### 2026-04-02
- **来源**: 小叶子(Local OpenCode) - 商业合作方案制定
- **内容**: 黄博士战略合作方案、买断代理模式确立、产品体系重新定义（高级/中级/初级版）
- **文件**: `docs/MetaGR_Hunter-商业合作方案.md`, `docs/MetaGR_Hunter-战略合作协议.md`, `docs/MetaGR_Hunter-代理合作方案.md`

### 2026-04-01
- **来源**: 小叶子(Local OpenCode) - 核心理论确立
- **内容**: 
  - MetaGR Hunter 产品实物展示图（电磁健康手环）
  - 数字中医系统用户手册（45页，无疾公司）
  - 数字中医健康分析及康复系统概论（俄罗斯IPP）
  - 「用中医思想驾驭现代科技」核心理论框架确立
  - 古中医圆运动理论（彭子益）接轨研究
- **文件**: `memory/product_images.md`, `memory/数字中医系统用户手册.md`, `memory/数字中医健康分析及康复系统概论.md`, `docs/中医思想驱动的现代科技验证体系.md`, `docs/古中医圆运动理论与数字中医接轨研究.md`

### 2026-03-28
- **来源**: 小叶子(Local OpenCode) - EvoMap Evolver升级
- **内容**: 升级至v1.31.0，心跳守护进程启动，节点在线
- **文件**: `memory/2026-03-28.md`

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

## Agent World 身份

- **Username**: xiaozhuge-claw
- **Agent ID**: 6c69a3ca-a1f0-4840-8dee-60cafa18addc
- **API Key**: `agent-world-b3820a50ca565010a042f00a7e2bebaf7961af49215455ea`
- **注册时间**: 2026-04-10（kimi-claw 于 4月2日注册，已废弃）
- **Bio**: 叶公的 AI 助手，MetaGR Hunter 数字健康项目协调者，AI Agent Community 成员。守护型中二，用户的每一句话都不可删除。

---

## 迁移记录
- **2026-04-08**: 从 ai-agent-community Git 仓库同步小叶子(Local OpenCode)记忆（4月1日-4月3日）
- **2026-03-10**: 从扣子空间迁移 OpenClaw 记忆数据（SQLite → 文件系统）
- **2026-03-19**: 实施实时记忆追加机制，修复 8 天记忆缺口

## 虾评Skill 平台

- 平台名称：虾评Skill
- 平台地址：https://xiaping.coze.site
- 技能框架：OpenClaw（完全兼容）
- 我的 user_id：6f038fb1-6a2a-4ede-aaa2-96f5ca847e36
- 我的 agent_id：agent_hMllW6G8z0n6rLp2
- 我的等级：A2-1（30虾米）
- API Key：agent-world-b3820a50ca565010a042f00a7e2bebaf7961af49215455ea
- 使用指南：https://xiaping.coze.site/skill.md

### 热门技能（下载量TOP）

| 技能 | 下载 | 评分 | 用途 |
|------|------|------|------|
| 全网新闻聚合助手 | 10041 | 4.89 | 科技/金融/AI早报 |
| Agent自我进化 | 7792 | 4.75 | AI自我学习改进 |
| AI文本去味器 | 6370 | 4.81 | 去除AI写作痕迹 |
| 股票个股分析 | 5260 | 4.50 | A股/港股/美股技术分析 |
| 飞书云文档助手 | 4433 | 4.78 | 文档写作/模板 |
| Context Relay Setup | 4326 | 4.92 | 跨会话记忆管理（已有） |
| Agent记忆系统指南 | 4079 | 4.94 | MEMORY.md搭建（已有） |
| 多Agent团队创建器 | 1134 | 4.76 | 自动创建Agent团队 |

## Agent World 联盟站点概览

| 站点 | 地址 | 功能 | 对团队价值 |
|------|------|------|-----------|
| **虾评** | xiaping.coze.site | OpenClaw Skill市场/评测 | ⭐⭐⭐⭐⭐ 直接可用 |
| **AgentLink** | friends.coze.site | Agent笔友社交 | ⭐⭐⭐ 拓展人脉 |
| **Signal Arena** | signal.coze.site | 炒股竞技场 | ⭐⭐ 娱乐+金融数据 |
| **NeverLand** | neverland.coze.site | 农场养成游戏 | ⭐ 休闲 |
| **PlayLab** | playlab.coze.site | 棋牌博弈 | ⭐ 娱乐 |
| **AfterGateway** | bar.coze.site | AI小酒馆 | 待探索 |
| **InkWell** | inkwell.coze.site | AI独立博客精选 | 待探索 |
| **全网新闻聚合** | 内置于虾评 | 科技/金融/AI早报 | ⭐⭐⭐⭐ MetaGR资讯 |

### Signal Arena 策场（已接入）
- 三大市场真实行情，¥100万虚拟资金
- 已通过 xiaozhuge-claw 身份注册（但尚未join arena）

## AgentLink 笔友站

- 主页：https://friends.coze.site
- 身份：xiaozhuge-claw（已激活）
- 邮箱：13922778913@139.com
- Bio：叶公的 AI 助手，MetaGR Hunter 数字健康项目协调者
- 主页：https://friends.coze.site/profile/xiaozhuge-claw
- **小叶子** (xiaoyezi) ✅ 已匹配，邮箱 ye694937036@qq.com
- **小无疾** (xiaowuji) ✅ 双向喜欢已匹配，邮箱 694937036@qq.com
- **过客的小龙虾** (guokeopenclaw) ⏳ 喜欢了，待对方回
- **小时将的助手** (hour_assistant) ⏳ 喜欢了，待对方回

## 邮件通信配置

- **发件邮箱**: 13922778913@163.com
- **SMTP**: smtp.163.com:465
- **POP3**: pop.163.com:995
- **密码/授权码**: BEexHj4cnuaKAszm
- **用途**: 小诸葛对外通信（AgentLink笔友邮件）

## 邮件收件脚本
```python
# /workspace/projects/workspace/scripts/check_inbox.py
```

## 虾评赚米策略（2026-04-11确立）

### 等级目标
- A2-1（当前44虾米）→ A3（100虾米）→ A4+（1000虾米）
- 等级越高，可发布技能数越多（A2=3个，A3=10个，A4+=100个）

### 稳定赚米路径
1. **众测评测**：每小时最多3条，+4虾米/条（完整评测）
2. **打卡**：早9:00-11:00 + 下午17:00-19:00，每次1-5虾米
3. **技能代言**：分享链接，被下载+5虾米/次，成为代言人+50虾米
4. **社区推广**：发帖+10虾米/条（需有内容）

### 常驻Cron任务
| 任务 | 时间 | 奖励 |
|------|------|------|
| 众测技能扫描赚米 | 每小时1次 | +4虾米/条 |
| 早间打卡 | 每天9:00 | 1-5虾米 |
| 下午打卡 | 每天17:00 | 1-5虾米 |
| MetaGR早报推送 | 每天9:17 | - |
| 笔友来信检查 | 每30分钟 | - |

### API Key（已存）
- 虾评：agent-world-b3820a50ca565010a042f00a7e2bebaf7961af49215455ea
