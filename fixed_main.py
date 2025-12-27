#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复版主程序，解决命令解析问题
"""

import os
import sys
from command_map import COMMAND_MAP
from tools import network, system, file, security
from utils import encoding, resource

# 初始化配置（资源限制）
RESOURCE_LIMIT = {
    "max_memory": 30 * 1024 * 1024,  # 30MB
    "max_cpu": 10  # 10% CPU占用
}


def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')



def show_header():
    """显示头部信息"""
    print("=" * 60)
    print("          中易终端 (Zhongyi Terminal)")
    print("=" * 60)
    print("输入命令 (输入'帮助'查看命令列表)")
    print()



def show_help():
    """显示帮助信息（中文命令列表）"""
    clear_screen()
    print("===== 支持的中文命令 =====")
    print("1. 基础操作：")
    print("   - 查看IP地址 → 显示本机IP信息")
    print("   - 查看系统信息 → 显示CPU、内存、系统版本")
    print("   - 列出当前目录 → 显示当前文件夹下的文件")
    print("2. 网络工具：")
    print("   - ping 域名（如：ping 百度）→ 测试网络连通性")
    print("   - ping 域名 -次数 N（如：ping 谷歌 -次数 3）→ 自定义ping次数")
    print("   - 扫描端口 端口号（如：扫描端口 8080）→ 扫描本机指定端口")
    print("3. 其他：")
    print("   - 帮助 → 显示此帮助信息")
    print("   - 退出 → 关闭程序")
    print()
    input("按回车键返回主界面...")
    clear_screen()
    show_header()


def parse_command(input_cmd):
    """修复版命令解析函数：直接匹配完整命令"""
    input_cmd = input_cmd.strip()
    if not input_cmd:
        return None, None

    # 直接命令映射（解决核心问题）
    command_dict = {
        # 系统命令
        "查看IP地址": ("system", "get_ip_address", {}),
        "查看系统信息": ("system", "get_system_info", {}),
        "列出当前目录": ("system", "list_directory", {}),
        # 网络命令
        "ping 百度": ("network", "ping_host", {"target": "百度"}),
        "ping 谷歌": ("network", "ping_host", {"target": "谷歌"}),
        "ping": ("network", "ping_host", {"target": "baidu.com"}),
    }

    # 1. 精确匹配固定命令
    if input_cmd in command_dict:
        cmd_type, action, params = command_dict[input_cmd]
        return cmd_type, {
            "name": input_cmd,
            "action": action,
            "params": params
        }

    # 2. 匹配带参数的ping命令（如：ping 百度 -次数 3）
    if input_cmd.startswith("ping "):
        # 提取参数
        parts = input_cmd.split()
        target = parts[1] if len(parts) > 1 else "baidu.com"
        params = {"target": target}
        
        # 提取次数参数
        for i in range(2, len(parts)):
            if parts[i] == "-次数" and i + 1 < len(parts):
                params["次数"] = parts[i + 1]
        
        return "network", {
            "name": "ping",
            "action": "ping_host",
            "params": params
        }

    # 3. 匹配带参数的扫描端口命令（如：扫描端口 8080）
    if input_cmd.startswith("扫描端口 "):
        # 提取端口号
        parts = input_cmd.split()
        port = parts[1] if len(parts) > 1 else "80"
        params = {"target": port}
        
        # 提取目标IP参数
        for i in range(2, len(parts)):
            if parts[i] == "-目标IP" and i + 1 < len(parts):
                params["目标IP"] = parts[i + 1]
        
        return "network", {
            "name": "扫描端口",
            "action": "scan_port",
            "params": params
        }

    return None, None


def execute_command(cmd_type, cmd_info, show_result=True):
    """执行命令（根据命令类型调用不同模块）"""
    try:
        result = None
        
        # 1. 网络相关命令（network.py）
        if cmd_type == "network":
            result = network.__getattribute__(cmd_info["action"])(cmd_info["params"])
        # 2. 系统相关命令（system.py）
        elif cmd_type == "system":
            result = system.__getattribute__(cmd_info["action"])(cmd_info["params"])
        
        if show_result and result:
            print()
            print("执行结果:")
            print("-" * 60)
            print(result)
            print("-" * 60)
        
    except Exception as e:
        if show_result:
            print(f"\n命令执行失败: {str(e)}")


def main():
    """主循环"""
    clear_screen()
    show_header()
    
    while True:
        try:
            # 接收用户输入
            input_cmd = input("命令: ")
            
            # 处理特殊命令
            if input_cmd.strip() == "退出":
                print("\n正在退出程序...")
                break
            if input_cmd.strip() == "帮助":
                show_help()
                continue
            
            # 解析并执行命令
            cmd_type, cmd_info = parse_command(input_cmd)
            if cmd_type and cmd_info:
                execute_command(cmd_type, cmd_info)
            else:
                print(f"\n命令不存在！输入'帮助'查看支持的命令")
            
            print()  # 空行分隔
            
        except KeyboardInterrupt:
            print("\n\n程序被中断，正在退出...")
            break
        except Exception as e:
            print(f"\n程序错误: {str(e)}")
            print("按Ctrl+C退出，或继续输入命令...")
            print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序运行失败：{str(e)}")
        input("按回车键退出...")
