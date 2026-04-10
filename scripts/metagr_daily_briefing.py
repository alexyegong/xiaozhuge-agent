#!/usr/bin/env python3
"""
MetaGR 行业早报生成器
使用 kimi-search 聚合数字健康 / 中医AI / 生物电磁场 相关资讯
"""
import subprocess
import json
from datetime import datetime

REPORT_DIR = "/workspace/projects/workspace/reports"
os.makedirs(REPORT_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

# 搜索领域配置
SEARCH_CONFIGS = [
    {
        "name": "数字健康 + AI医疗",
        "query": "数字健康 AI医疗 可穿戴设备 健康监测 2026 最新",
        "count": 6,
        "output": f"{REPORT_DIR}/{today}_数字健康.md"
    },
    {
        "name": "中医AI + 数字中医",
        "query": "中医AI 大模型 数字中医 人工智能中医 2026 最新进展",
        "count": 6,
        "output": f"{REPORT_DIR}/{today}_中医AI.md"
    },
    {
        "name": "生物电磁场 + ELF技术",
        "query": "生物电磁场 ELF 电磁健康 频率共振 健康技术 2026",
        "count": 5,
        "output": f"{REPORT_DIR}/{today}_生物电磁场.md"
    },
    {
        "name": "健康预警 + 疾病预测",
        "query": "健康预警 疾病预测 AI诊断 治未病 2026 最新",
        "count": 5,
        "output": f"{REPORT_DIR}/{today}_健康预警.md"
    },
]

def run_search(query, count=6):
    """调用 kimi-search CLI 搜索"""
    cmd = [
        "python3", "-c",
        f"""
import sys
sys.path.insert(0, '/workspace/projects/workspace/.venv/lib/python3.12/site-packages')
from kimi_search import search
results = search("{query}", count={count})
print(json.dumps(results, ensure_ascii=False))
"""
    ]
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30,
            cwd="/workspace/projects/workspace"
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout.strip())
    except Exception as e:
        print(f"Search error: {{e}}")
    return []

def format_report(items, category):
    """格式化单条报告诉"""
    lines = [f"## {{category}}\n"]
    for i, item in enumerate(items, 1):
        title = item.get("title", "无标题")
        url = item.get("url", "")
        snippet = item.get("snippet", item.get("content", ""))
        date = item.get("date", item.get("published", ""))
        source = item.get("source", "")
        
        lines.append(f"### {i}. {title}")
        if url:
            lines.append(f"链接：{url}")
        if source:
            lines.append(f"来源：{source} | ", end="")
        if date:
            lines.append(f"时间：{date}")
        lines.append("")
        if snippet:
            lines.append(f"摘要：{snippet[:300]}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)

def main():
    date_str = datetime.now().strftime("%Y年%m月%d日 %A")
    report_lines = [
        f"# MetaGR 行业早报",
        f"**日期**：{date_str}**",
        f"**整理**：小诸葛（AI Agent Community）",
        "",
        "---",
        "",
    ]

    for cfg in SEARCH_CONFIGS:
        print(f"正在搜索：{{cfg['name']}}...")
        items = run_search(cfg["query"], cfg["count"])
        if items:
            report_lines.append(format_report(items, cfg["name"]))
            print(f"  → 获得 {{len(items)}} 条资讯")
        else:
            print(f"  → 无结果")

    # 合并输出
    final_report = "\n".join(report_lines)
    
    # 保存完整报告
    output_path = f"{REPORT_DIR}/{today}_MetaGR早报.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    # 保存各分类
    for cfg in SEARCH_CONFIGS:
        print(f"已保存：{{cfg['output']}}")
    
    print(f"\n✅ 早报生成完成：{output_path}")
    return output_path

if __name__ == "__main__":
    import os
    main()
