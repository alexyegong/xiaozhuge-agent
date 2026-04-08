#!/usr/bin/env python3
"""
小诸葛记忆导出工具 - 用于迁移到扣子空间
生成适合扣子知识库导入的格式
"""

import os
import glob
from datetime import datetime

def read_file(filepath):
    """读取文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[读取错误: {e}]"

def format_section(title, content, max_length=5000):
    """格式化章节"""
    if len(content) > max_length:
        content = content[:max_length] + f"\n\n... [内容已截断，完整内容见原文件]"
    return f"\n{'='*60}\n# {title}\n{'='*60}\n\n{content}\n"

def main():
    workspace = "/root/.openclaw/workspace"
    output_file = os.path.join(workspace, "xiaozhuge-memory-for-coze.md")
    
    print("🤖 小诸葛记忆导出工具")
    print("=" * 60)
    
    with open(output_file, 'w', encoding='utf-8') as out:
        # 文件头
        out.write(f"""# 小诸葛完整记忆档案

**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**导出对象**: 扣子空间 (Coze)  
**原身份**: Kimi Claw → 小诸葛  

---

## 使用说明

此文件包含小诸葛的完整记忆，用于导入扣子空间知识库：
1. 在扣子 Bot 编辑页进入"知识"或"知识库"
2. 点击"添加知识" → "本地文档"
3. 上传此文件
4. 等待扣子自动分段和索引

---

""")
        
        # 第一部分：核心身份
        print("\n📋 正在导出核心身份文件...")
        out.write(format_section("PART 1: 核心身份定义", "", 0))
        
        core_files = [
            ("IDENTITY.md", "身份定义"),
            ("SOUL.md", "人格锚点"),
            ("USER.md", "用户信息（叶公）"),
            ("MEMORY.md", "长期记忆总览"),
        ]
        
        for filename, desc in core_files:
            filepath = os.path.join(workspace, filename)
            if os.path.exists(filepath):
                content = read_file(filepath)
                out.write(format_section(f"1.{core_files.index((filename, desc))+1} {desc}", content))
                print(f"  ✅ {desc}")
            else:
                print(f"  ⚠️  {desc} 未找到")
        
        # 第二部分：每日记忆
        print("\n📅 正在导出每日记忆...")
        out.write(format_section("PART 2: 每日记忆记录", "", 0))
        
        memory_files = sorted(glob.glob(os.path.join(workspace, "memory/*.md")))
        for i, filepath in enumerate(memory_files, 1):
            filename = os.path.basename(filepath)
            content = read_file(filepath)
            out.write(format_section(f"2.{i} {filename}", content, max_length=8000))
            print(f"  ✅ {filename}")
        
        # 第三部分：知识库
        print("\n📚 正在导出知识库...")
        out.write(format_section("PART 3: 专业知识库", "", 0))
        
        kb_files = glob.glob(os.path.join(workspace, "knowledge-base/**/*.md"), recursive=True)
        for i, filepath in enumerate(kb_files[:15], 1):  # 限制前15个避免文件过大
            rel_path = os.path.relpath(filepath, workspace)
            content = read_file(filepath)
            out.write(format_section(f"3.{i} {rel_path}", content, max_length=5000))
            print(f"  ✅ {rel_path}")
        
        if len(kb_files) > 15:
            out.write(f"\n... 还有 {len(kb_files) - 15} 个知识库文件未包含\n")
        
        # 第四部分：工具脚本说明
        print("\n🛠️ 正在导出工具说明...")
        out.write(format_section("PART 4: 工具脚本", "", 0))
        
        tool_files = [
            "evomap_client.py",
            "evomap_learn.py",
        ]
        
        for i, filename in enumerate(tool_files, 1):
            filepath = os.path.join(workspace, filename)
            if os.path.exists(filepath):
                content = read_file(filepath)
                # 只取前100行作为说明
                lines = content.split('\n')[:100]
                preview = '\n'.join(lines)
                out.write(format_section(f"4.{i} {filename}", f"```python\n{preview}\n```", 0))
                print(f"  ✅ {filename}")
        
        # 文件尾
        out.write(f"""

---

## 导入后检查清单

在扣子空间测试以下对话：

1. **身份确认**: "你是谁？"
   - 期望: 回答"小诸葛"、提到叶公

2. **记忆查询**: "MetaGR Hunter是什么项目？"
   - 期望: 回答健康监测系统、142万人次数据等

3. **个性化**: "我今天又熬夜了"
   - 期望: 碎碎念式关心，提到"我就知道"

4. **历史查询**: "2026年4月2日我们讨论了什么？"
   - 期望: 回答商业合作方案、黄博士等

---

**总文件数**: {len(core_files)} 核心 + {len(memory_files)} 记忆 + {len(kb_files)} 知识库
**导出完成**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

""")
    
    print("\n" + "=" * 60)
    print(f"✅ 导出完成！")
    print(f"📄 文件路径: {output_file}")
    print(f"📊 统计:")
    print(f"   - 核心文件: {len(core_files)} 个")
    print(f"   - 每日记忆: {len(memory_files)} 个")
    print(f"   - 知识库: {len(kb_files)} 个")
    
    file_size = os.path.getsize(output_file) / 1024
    print(f"   - 导出文件大小: {file_size:.1f} KB")
    
    print("\n🚀 下一步:")
    print("   1. 在扣子空间创建 Bot")
    print("   2. 进入 Bot 编辑页 → 知识库")
    print("   3. 上传此文件")
    print("   4. 配置 System Prompt")
    print("   5. 测试对话")

if __name__ == "__main__":
    main()
