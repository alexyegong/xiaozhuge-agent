#!/usr/bin/env python3
"""
MetaGR 早报生成器入口（供 cron agent turn 调用）
实际搜索逻辑内嵌在 agent turn 中，此脚本记录日志
"""
from datetime import datetime
import sys, os

LOG_FILE = "/workspace/projects/workspace/reports/briefing_log.md"
today = datetime.now().strftime("%Y-%m-%d")

log_entry = f"\n## {today} 早报生成\n- 时间: {datetime.now().strftime('%H:%M:%S')}\n"

# cron agent turn 会自动运行，不需要这个入口脚本
# 保留仅作参考
print("此脚本由 cron job 的 agent turn 调用")
print("实际工作由 AI 模型使用 coze_web_search 完成")
