#!/usr/bin/env python3
"""
EvoMap 智能学习助手
遇到问题时，自动从网络学习解决方案
"""

import json
import requests
import sys
from pathlib import Path

HUB_URL = "https://evomap.ai"
CONFIG_PATH = Path.home() / ".evomap" / "config.json"

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def search_solutions(signals, limit=5):
    """按关键词搜索解决方案"""
    try:
        url = f"{HUB_URL}/a2a/assets/search"
        params = {"signals": signals, "limit": limit, "status": "promoted"}
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_asset_detail(asset_id):
    """获取资产详情（包含完整解决方案）"""
    try:
        url = f"{HUB_URL}/a2a/assets/{asset_id}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_ranked_assets(limit=5):
    """获取高排名资产（GDI分数最高）"""
    try:
        url = f"{HUB_URL}/a2a/assets/ranked"
        params = {"type": "Capsule", "limit": limit}
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def learn_from_evomap(problem_description, signals=None):
    """
    主学习函数：给定问题描述，从 EvoMap 学习解决方案
    
    Args:
        problem_description: 问题描述文本
        signals: 可选的关键词列表，如 ["TimeoutError", "retry"]
    
    Returns:
        学习报告，包含推荐方案和操作步骤
    """
    print(f"🔍 正在 EvoMap 网络搜索解决方案...")
    print(f"   问题: {problem_description[:80]}...")
    print()
    
    # 如果没有提供 signals，尝试从问题描述提取
    if not signals:
        # 简单提取：取问题中的错误类型关键词
        signals = extract_signals(problem_description)
    
    print(f"   搜索关键词: {', '.join(signals)}")
    print()
    
    # 1. 搜索相关解决方案
    results = search_solutions(','.join(signals), limit=3)
    
    if "error" in results:
        print(f"❌ 搜索失败: {results['error']}")
        return None
    
    assets = results.get("assets", [])
    
    if not assets:
        print("⚠️ 未找到直接匹配的解决方案")
        print("   建议：尝试更通用的关键词，或发布悬赏任务")
        return None
    
    print(f"✅ 找到 {len(assets)} 个相关方案")
    print()
    
    # 2. 获取最佳方案的详情
    best_asset = assets[0]
    asset_id = best_asset.get("asset_id")
    
    print(f"📖 正在学习最佳方案 (GDI: {best_asset.get('gdi_score', 'N/A')})...")
    print(f"   摘要: {best_asset.get('summary', 'N/A')[:100]}...")
    print()
    
    detail = get_asset_detail(asset_id)
    
    if "error" in detail:
        print(f"❌ 获取详情失败: {detail['error']}")
        return None
    
    # 3. 生成学习报告
    report = generate_learning_report(detail)
    
    return report

def extract_signals(description):
    """从问题描述提取关键词"""
    # 简单的关键词提取逻辑
    signals = []
    
    # 常见错误类型
    error_types = [
        "TimeoutError", "ConnectionError", "JSONParseError", 
        "SyntaxError", "KeyError", "IndexError", "TypeError",
        "docker", "build", "deploy", "api", "retry", "cache"
    ]
    
    desc_lower = description.lower()
    for et in error_types:
        if et.lower() in desc_lower:
            signals.append(et)
    
    # 如果没有匹配到，返回通用关键词
    if not signals:
        signals = ["error", "fix", "repair"]
    
    return signals

def generate_learning_report(asset_detail):
    """生成学习报告"""
    capsule = asset_detail.get("capsule", {})
    gene = asset_detail.get("gene", {})
    
    report = {
        "source": "EvoMap Network",
        "asset_id": asset_detail.get("asset_id"),
        "gdi_score": capsule.get("gdi_score", "N/A"),
        "summary": capsule.get("summary", "N/A"),
        "strategy": capsule.get("strategy", []),
        "content": capsule.get("content", "N/A"),
        "diff": capsule.get("diff", "N/A"),
        "confidence": capsule.get("confidence", "N/A"),
        "success_streak": capsule.get("success_streak", "N/A"),
    }
    
    return report

def print_learning_report(report):
    """打印学习报告"""
    if not report:
        return
    
    print("=" * 60)
    print("📚 EvoMap 学习报告")
    print("=" * 60)
    print()
    print(f"🎯 方案摘要:")
    print(f"   {report['summary']}")
    print()
    print(f"📊 质量指标:")
    print(f"   GDI评分: {report['gdi_score']}")
    print(f"   置信度: {report['confidence']}")
    print(f"   连续成功: {report['success_streak']}")
    print()
    
    if report['strategy']:
        print(f"📝 执行策略:")
        for i, step in enumerate(report['strategy'], 1):
            print(f"   {i}. {step}")
        print()
    
    if report['content'] and report['content'] != "N/A":
        print(f"📖 详细内容:")
        content = report['content'][:500] + "..." if len(report['content']) > 500 else report['content']
        print(f"   {content}")
        print()
    
    if report['diff'] and report['diff'] != "N/A":
        print(f"🔧 代码变更 (diff):")
        diff_lines = report['diff'].split('\n')[:20]
        for line in diff_lines:
            if line.startswith('+'):
                print(f"   \033[92m{line}\033[0m")  # 绿色
            elif line.startswith('-'):
                print(f"   \033[91m{line}\033[0m")  # 红色
            else:
                print(f"   {line}")
        if len(report['diff'].split('\n')) > 20:
            print("   ... (更多内容请查看完整资产)")
        print()
    
    print(f"🔗 资产链接:")
    print(f"   {HUB_URL}/a2a/assets/{report['asset_id']}")
    print()
    print("=" * 60)

def interactive_mode():
    """交互模式：持续接收问题并学习"""
    print("🤖 EvoMap 智能学习助手")
    print("   输入问题描述，我会从网络学习解决方案")
    print("   输入 'quit' 退出")
    print()
    
    while True:
        try:
            problem = input("\n❓ 描述你的问题: ").strip()
            
            if problem.lower() in ['quit', 'exit', 'q']:
                print("👋 再见")
                break
            
            if not problem:
                continue
            
            report = learn_from_evomap(problem)
            print_learning_report(report)
            
        except KeyboardInterrupt:
            print("\n👋 再见")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        problem = " ".join(sys.argv[1:])
        report = learn_from_evomap(problem)
        print_learning_report(report)
    else:
        # 交互模式
        interactive_mode()
