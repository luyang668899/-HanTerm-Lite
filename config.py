# 配置文件（资源限制、默认参数）

# 资源限制配置
RESOURCE_LIMIT = {
    "max_memory": 30 * 1024 * 1024,  # 30MB
    "max_cpu": 10  # 10% CPU占用
}

# 默认参数配置
DEFAULT_PARAMS = {
    "ping_count": 4,  # 默认ping次数
    "scan_timeout": 10,  # 扫描超时时间（秒）
    "max_display_lines": 15,  # 最大显示行数
    "max_output_length": 1000,  # 最大输出长度
}

# 系统命令配置
SYSTEM_COMMANDS = {
    "clear_screen": "clear" if not __import__('os').name == "nt" else "cls",
    "list_dir": "ls -l" if not __import__('os').name == "nt" else "dir",
    "ip_config": "ifconfig" if not __import__('os').name == "nt" else "ipconfig",
}