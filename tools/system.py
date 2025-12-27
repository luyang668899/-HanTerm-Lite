import platform
import os
import subprocess
from utils.encoding import execute_cmd

def get_system_info(params=None):
    """获取系统信息，包括操作系统、CPU、内存等，不依赖psutil"""
    try:
        # 操作系统信息
        os_info = f"操作系统: {platform.system()} {platform.release()}"
        os_version = f"系统版本: {platform.version()}"
        machine = f"架构: {platform.machine()}"
        node = f"主机名: {platform.node()}"
        
        # CPU信息（使用标准库）
        cpu_count = f"CPU核心数: {os.cpu_count()}（逻辑）"
        # CPU使用率：在macOS上使用sysctl，Linux使用top，Windows使用wmic
        if platform.system() == "Darwin":  # macOS
            cpu_percent = execute_cmd("sysctl -n machdep.cpu.brand_string")
            cpu_percent = f"CPU: {cpu_percent}"
        elif platform.system() == "Linux":
            cpu_percent = execute_cmd("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\([0-9.]*\)%* id.*/\1/' | awk '{print 100 - $1}'")
            cpu_percent = f"CPU使用率: {cpu_percent}%"
        else:  # Windows
            cpu_percent = execute_cmd("wmic cpu get name /value")
            cpu_percent = f"CPU: {cpu_percent.replace('Name=', '')}"
        
        # 内存信息：使用系统命令
        if platform.system() == "Darwin":  # macOS
            mem_info = execute_cmd("top -l 1 | grep PhysMem")
        elif platform.system() == "Linux":
            mem_info = execute_cmd("free -h | grep Mem")
        else:  # Windows
            mem_info = execute_cmd("wmic memorychip get capacity /value | head -2")
        memory_info = f"内存: {mem_info}"
        
        # 磁盘信息：使用系统命令
        if platform.system() == "Darwin":  # macOS
            disk_info = execute_cmd("df -h / | tail -1")
        elif platform.system() == "Linux":
            disk_info = execute_cmd("df -h / | tail -1")
        else:  # Windows
            disk_info = execute_cmd("wmic logicaldisk where DeviceID='C:' get Size,FreeSpace /value")
        disk_info = f"磁盘: {disk_info}"
        
        info = [
            os_info,
            os_version,
            machine,
            node,
            cpu_count,
            cpu_percent,
            memory_info,
            disk_info
        ]
        
        return "\n".join(info)
    
    except Exception as e:
        return f"获取系统信息失败: {str(e)}"

def get_ip_address(params=None):
    """获取IP地址信息"""
    try:
        if platform.system() == "Darwin" or platform.system() == "Linux":
            net_info = execute_cmd("ifconfig | grep 'inet ' | grep -v '127.0.0.1'")
        else:  # Windows
            net_info = execute_cmd("ipconfig | grep IPv4")
        return f"IP地址信息:\n{net_info}"
    except Exception as e:
        return f"获取IP地址失败: {str(e)}"

def list_directory(params=None):
    """列出当前目录文件"""
    try:
        if platform.system() == "Windows":
            result = execute_cmd("dir /b")
        else:
            result = execute_cmd("ls -la")
        return f"当前目录文件:\n{result}"
    except Exception as e:
        return f"列出目录失败: {str(e)}"