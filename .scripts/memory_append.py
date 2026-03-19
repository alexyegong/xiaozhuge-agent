#!/usr/bin/env python3
"""
自动记忆写入系统 - 实时追加方案
每次重要交互后自动记录到 memory/YYYY-MM-DD.md
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

def get_memory_path():
    """获取今日记忆文件路径"""
    workspace = os.environ.get('OPENCLAW_WORKSPACE', '/root/.openclaw/workspace')
    today = datetime.now().strftime('%Y-%m-%d')
    return Path(workspace) / 'memory' / f'{today}.md'

def ensure_memory_dir():
    """确保记忆目录存在"""
    workspace = os.environ.get('OPENCLAW_WORKSPACE', '/root/.openclaw/workspace')
    memory_dir = Path(workspace) / 'memory'
    memory_dir.mkdir(parents=True, exist_ok=True)
    return memory_dir

def append_memory_entry(title, content, category="对话"):
    """
    追加记忆条目到今日记忆文件
    
    Args:
        title: 条目标题
        content: 内容（支持多行）
        category: 分类（对话/操作/决策/技术）
    """
    ensure_memory_dir()
    memory_path = get_memory_path()
    
    now = datetime.now()
    time_str = now.strftime('%H:%M')
    
    # 如果文件不存在，创建文件头
    if not memory_path.exists():
        header = f"""# {now.strftime('%Y-%m-%d')} 记忆记录

> 自动生成于 {now.strftime('%Y-%m-%d %H:%M:%S')}

---

"""
        memory_path.write_text(header, encoding='utf-8')
    
    # 追加新条目
    entry = f"""## {title}

**时间**: {time_str}  
**分类**: {category}

{content}

---

"""
    
    with open(memory_path, 'a', encoding='utf-8') as f:
        f.write(entry)
    
    print(f"[记忆] 已记录到 {memory_path}")
    return memory_path

def main():
    """命令行入口"""
    if len(sys.argv) < 3:
        print("Usage: memory_append.py <title> <content> [category]")
        sys.exit(1)
    
    title = sys.argv[1]
    content = sys.argv[2]
    category = sys.argv[3] if len(sys.argv) > 3 else "对话"
    
    append_memory_entry(title, content, category)

if __name__ == '__main__':
    main()
