import os
import subprocess
from utils.encoding import execute_cmd

def nmap_scan(target_ip):
    """使用nmap进行网络扫描"""
    try:
        # 简单的nmap扫描命令
        cmd = f"nmap -sn {target_ip}/24"
        result = execute_cmd(cmd)
        return result
    except Exception as e:
        return f"nmap扫描失败: {str(e)}"


def port_scan(target_ip, port):
    """端口扫描功能（使用nmap）"""
    try:
        cmd = f"nmap -p {port} {target_ip}"
        result = execute_cmd(cmd)
        return result
    except Exception as e:
        return f"端口扫描失败: {str(e)}"


def vulnerability_scan(target_ip):
    """漏洞扫描（使用nmap的漏洞扫描脚本）"""
    try:
        # 使用nmap的基本漏洞扫描脚本
        cmd = f"nmap --script vuln {target_ip}"
        result = execute_cmd(cmd)
        return result
    except Exception as e:
        return f"漏洞扫描失败: {str(e)}"