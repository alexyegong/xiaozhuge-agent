# 记忆写入快捷命令

## 使用方式

### 方法 1: Python 脚本
```bash
python3 .scripts/memory_append.py "标题" "内容" "分类"
```

### 方法 2: 设置别名（推荐）
添加到 `.bashrc`:
```bash
alias mem='python3 /root/.openclaw/workspace/.scripts/memory_append.py'
```

然后使用:
```bash
mem "SSH配置完成" "已配置GitHub SSH key并推送代码" "操作"
```

## 分类建议
- **对话**: 日常交流、讨论
- **操作**: 命令执行、配置变更
- **决策**: 方案选择、重要决定
- **技术**: 技术细节、解决方案

## 触发规则
以下情况应自动/手动记录：
1. ✅ 重要技术决策后
2. ✅ 项目里程碑完成
3. ✅ 用户说"记住"或"记下来"
4. ✅ 关键配置变更
5. ✅ 解决了复杂问题
6. ✅ 新知识/信息加入
