#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证命令解析和执行功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from command_map import COMMAND_MAP
from main import parse_command

# 测试用例
test_cases = [
    "查看IP地址",
    "查看系统信息", 
    "列出当前目录",
    "ping 百度",
    "ping 谷歌 -次数 2",
    "扫描端口 80",
    "扫描端口 8080 -目标IP 127.0.0.1"
]

print("===== 测试命令解析功能 =====")
for test_cmd in test_cases:
    print(f"\n测试命令: {test_cmd}")
    cmd_type, cmd_info = parse_command(test_cmd)
    if cmd_type and cmd_info:
        print(f"  ✓ 解析成功")
        print(f"  - 命令类型: {cmd_type}")
        print(f"  - 命令名称: {cmd_info['name']}")
        print(f"  - 执行动作: {cmd_info['action']}")
        print(f"  - 参数: {cmd_info['params']}")
    else:
        print(f"  ✗ 解析失败")

print("\n===== 测试完成 =====")
