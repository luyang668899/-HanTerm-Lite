import os

# 中文命令映射表（与main.py期望的结构匹配）
COMMAND_MAP = {
    "system": {
        "查看IP地址": {
            "action": "get_ip_address"
        },
        "查看系统信息": {
            "action": "get_system_info"
        },
        "列出当前目录": {
            "action": "list_directory"
        }
    },
    "network": {
        "ping": {
            "action": "ping_host"
        },
        "扫描端口": {
            "action": "scan_port"
        }
    },
    "file": {
        "列出当前目录": {
            "action": "list_files"
        }
    },
    "security": {
        "扫描漏洞": {
            "action": "scan_vulnerabilities"
        },
        "快速扫描局域网": {
            "action": "scan_lan"
        }
    }
}