import os
import subprocess
from utils.encoding import execute_cmd

def ping_host(params):
    """中文ping工具：支持域名/IP，自定义次数，跨平台适配"""
    # 从params字典中获取参数
    domain = params.get("target", "baidu.com")  # 默认ping百度
    count = params.get("次数", "4")  # 默认4次
    
    # 处理域名映射（中文域名转英文）
    domain_map = {
        "百度": "baidu.com",
        "谷歌": "google.com",
        "腾讯": "tencent.com",
        "阿里": "alibaba.com"
    }
    if domain in domain_map:
        domain = domain_map[domain]
    
    # 跨平台命令适配
    if os.name == "nt":  # Windows
        cmd = f"ping {domain} -n {count}"
    else:  # Linux/macOS
        cmd = f"ping {domain} -c {count}"
    
    # 执行命令并返回结果（处理编码）
    return execute_cmd(cmd)

def scan_port(params):
    """端口扫描工具：基于telnet/ss命令，轻量无依赖（无需nmap）"""
    # 从params字典中获取参数
    target_ip = params.get("目标IP", "127.0.0.1")  # 默认扫描本地
    port = params.get("target", params.get("端口", "80"))  # 默认扫描80端口
    
    try:
        port = int(port)
        if port < 1 or port > 65535:
            return "端口号无效（需在1-65535之间）"
    except ValueError:
        return "端口号必须是数字"
    
    # 跨平台端口扫描命令（轻量，适合低配置）
    if os.name == "nt":  # Windows
        cmd = f"telnet {target_ip} {port} 2>NUL && echo 开放 || echo 关闭"
    else:  # Linux/macOS
        cmd = f"ss -tuln | grep ': {port}' && echo 开放 || echo 关闭"
    
    result = execute_cmd(cmd)
    if "开放" in result:
        return f"端口 {port} 状态：开放"
    elif "关闭" in result:
        return f"端口 {port} 状态：关闭"
    else:
        return f"端口 {port} 状态：无法检测（可能被防火墙拦截）"