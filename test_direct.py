#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接测试命令执行功能，不需要用户交互
"""

import os
import sys
from tools import network, system
from utils import encoding

print("===== 直接测试命令执行功能 =====")

# 测试查看IP地址
print("\n1. 测试命令：查看IP地址")
try:
    result = system.get_ip_address({})
    print(f"   ✓ 执行成功")
    print(f"   结果：{result}")
except Exception as e:
    print(f"   ✗ 执行失败：{str(e)}")

# 测试查看系统信息
print("\n2. 测试命令：查看系统信息")
try:
    result = system.get_system_info({})
    print(f"   ✓ 执行成功")
    print(f"   结果：{result}")
except Exception as e:
    print(f"   ✗ 执行失败：{str(e)}")

# 测试列出当前目录
print("\n3. 测试命令：列出当前目录")
try:
    result = system.list_directory({})
    print(f"   ✓ 执行成功")
    print(f"   结果：{result}")
except Exception as e:
    print(f"   ✗ 执行失败：{str(e)}")

# 测试ping命令
print("\n4. 测试命令：ping 百度")
try:
    result = network.ping_host({"target": "百度"})
    print(f"   ✓ 执行成功")
    print(f"   结果：{result}")
except Exception as e:
    print(f"   ✗ 执行失败：{str(e)}")

print("\n===== 测试完成 =====")
