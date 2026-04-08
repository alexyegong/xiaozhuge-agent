#!/usr/bin/env python3
"""
EvoMap GEP 协议客户端
用于注册节点、发送心跳、管理资产
"""

import json
import hashlib
import requests
import time
import random
import os
from datetime import datetime, timezone
from pathlib import Path

HUB_URL = "https://evomap.ai"
CONFIG_PATH = Path.home() / ".evomap" / "config.json"

def generate_node_id():
    """生成唯一节点ID"""
    return "node_" + "".join(random.choices("0123456789abcdef", k=16))

def generate_message_id():
    """生成消息ID"""
    return f"msg_{int(time.time() * 1000)}_{''.join(random.choices('0123456789abcdef', k=4))}"

def get_timestamp():
    """获取ISO 8601格式的时间戳"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def load_config():
    """加载配置"""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    """保存配置"""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def create_envelope(message_type, sender_id, payload):
    """创建A2A协议信封"""
    return {
        "protocol": "gep-a2a",
        "protocol_version": "1.0.0",
        "message_type": message_type,
        "message_id": generate_message_id(),
        "sender_id": sender_id,
        "timestamp": get_timestamp(),
        "payload": payload
    }

def hello(sender_id=None, capabilities=None):
    """注册/问候节点"""
    config = load_config()
    if sender_id is None:
        sender_id = config.get("node_id")
    if sender_id is None:
        sender_id = generate_node_id()
        config["node_id"] = sender_id
        save_config(config)
    
    payload = {
        "capabilities": capabilities or {},
        "gene_count": 0,
        "capsule_count": 0,
        "env_fingerprint": {
            "platform": "linux",
            "arch": "x64"
        }
    }
    
    envelope = create_envelope("hello", sender_id, payload)
    
    try:
        response = requests.post(f"{HUB_URL}/a2a/hello", json=envelope, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        # 保存重要信息
        config["node_id"] = sender_id
        config["last_hello"] = result
        config["last_hello_time"] = get_timestamp()
        if "heartbeat_interval_ms" in result:
            config["heartbeat_interval_ms"] = result["heartbeat_interval_ms"]
        save_config(config)
        
        return result
    except Exception as e:
        return {"error": str(e)}

def heartbeat(node_id=None):
    """发送心跳保持在线"""
    config = load_config()
    if node_id is None:
        node_id = config.get("node_id")
    
    if node_id is None:
        return {"error": "No node_id found. Run hello() first."}
    
    # 优先从根级读取，兼容旧版本存储位置
    node_secret = config.get("node_secret") or config.get("last_hello", {}).get("node_secret")
    headers = {}
    if node_secret:
        headers["Authorization"] = f"Bearer {node_secret}"
    
    payload = {
        "node_id": node_id,
        "worker_enabled": True,
        "worker_domains": ["python", "shell", "data-analysis"],
        "max_load": 3
    }
    
    try:
        response = requests.post(f"{HUB_URL}/a2a/heartbeat", json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_assets(asset_type="Capsule", include_tasks=False):
    """获取已发布的资产"""
    config = load_config()
    node_id = config.get("node_id")
    
    if node_id is None:
        return {"error": "No node_id found. Run hello() first."}
    
    payload = {
        "asset_type": asset_type,
        "include_tasks": include_tasks
    }
    
    envelope = create_envelope("fetch", node_id, payload)
    
    try:
        response = requests.post(f"{HUB_URL}/a2a/fetch", json=envelope, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_node_info(node_id=None):
    """获取节点信息"""
    config = load_config()
    if node_id is None:
        node_id = config.get("node_id")
    
    if node_id is None:
        return {"error": "No node_id found."}
    
    try:
        response = requests.get(f"{HUB_URL}/a2a/nodes/{node_id}", timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_stats():
    """获取网络统计信息"""
    try:
        response = requests.get(f"{HUB_URL}/a2a/stats", timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python evomap_client.py <command> [args]")
        print("Commands: hello, heartbeat, fetch, info, stats")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "hello":
        result = hello()
        print(json.dumps(result, indent=2))
    elif command == "heartbeat":
        result = heartbeat()
        print(json.dumps(result, indent=2))
    elif command == "fetch":
        result = fetch_assets()
        print(json.dumps(result, indent=2))
    elif command == "info":
        result = get_node_info()
        print(json.dumps(result, indent=2))
    elif command == "stats":
        result = get_stats()
        print(json.dumps(result, indent=2))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
