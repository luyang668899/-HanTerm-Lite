# 中易终端（Zhongyi Terminal）

中易终端（Zhongyi Terminal）是一个轻量级的中文终端工具，支持使用中文命令操作，降低命令行使用门槛，特别适配低配置设备（2GB内存+双核CPU），资源占用少，兼容Windows/Linux（Kali）/macOS系统。

## 功能特性

- 支持中文自然语言命令输入，降低命令行使用门槛
- 适配老旧电脑，资源占用≤30MB，CPU占用≤10%
- 集成网络安全、系统管理、文件操作等常用功能
- 全免费技术栈，代码开源可二次开发
- 兼容Windows/Linux（Kali）/macOS系统

## 支持的命令

### 基础操作
- 查看IP地址 → 显示本机IP信息
- 查看系统信息 → 显示CPU、内存、系统版本
- 列出当前目录 → 显示当前文件夹下的文件
- 清空屏幕 → 清空当前屏幕内容

### 网络工具
- ping 域名（如：ping 百度）→ 测试网络连通性
- ping 域名 -次数 N（如：ping 谷歌 -次数 3）→ 自定义ping次数
- 扫描端口 端口号（如：扫描端口 8080）→ 扫描本机指定端口
- 扫描端口 端口号 -目标IP IP（如：扫描端口 80 -目标IP 192.168.1.1）

### 安全工具（Kali Linux专用）
- 扫描漏洞 目标IP（如：扫描漏洞 192.168.1.1）→ 调用nmap扫描
- 快速扫描局域网 → 扫描局域网内的设备

## 安装和运行

### 环境要求
- Python 3.8+

### 安装依赖
```bash
pip install chardet psutil
```

### 运行程序
```bash
cd zhongyi_terminal
python main.py
```

## 系统架构

```
zhongyi_terminal/
├── main.py          # 主程序入口（窗口渲染、命令分发）
├── command_map.py   # 中文命令-系统命令映射表
├── config.py        # 配置文件（资源限制、默认参数）
├── tools/           # 功能模块目录
│   ├── network.py   # 网络工具（ping、端口扫描、局域网扫描）
│   ├── system.py    # 系统工具（系统信息、进程管理）
│   ├── file.py      # 文件工具（文件查看、搜索、复制）
│   └── security.py  # 安全工具（Kali工具集成：nmap、sqlmap）
├── utils/           # 工具函数目录
│   ├── encoding.py  # 中文编码处理（防乱码）
│   └── resource.py  # 资源优化（内存/CPU控制）
└── README.md        # 项目说明文档
```

## 优化特性

### 内存优化
- 限制命令输出长度：每次输出最多1000字符，显示最多15行
- 自动垃圾回收：内存占用超过30MB时，触发gc.collect()释放内存
- 避免缓存冗余数据：不存储历史命令输出，仅显示当前结果

### CPU优化
- 限制扫描线程数：端口扫描、nmap调用时，最多使用1个线程
- 命令执行超时控制：所有外部命令超时10秒，避免无限占用CPU
- 减少窗口刷新频率：仅在输入命令后刷新界面，不实时刷新

### 兼容性优化
- 跨平台命令适配：通过os.name判断系统，自动切换ping/ipconfig等命令
- 低版本Python支持：仅使用Python 3.8+兼容语法，避免新特性
- 中文显示适配：用curses.setlocale和chardet双重保障，解决不同系统中文乱码

## 打包发布

使用PyInstaller打包成单文件：

```bash
pip install pyinstaller
# Windows:
pyinstaller -F -w -n 中易终端 -i icon.ico main.py
# Linux/macOS:
pyinstaller -F -n zhongyi-terminal main.py
```

## 扩展开发

### 插件系统
- 设计插件目录规范：plugins/目录下放置.py插件文件，支持中文命名
- 实现插件加载功能：主程序启动时自动扫描插件，添加到命令列表

### 云同步功能
- 用GitHub Gist API（免费）同步自定义命令和脚本
- 支持"上传脚本""下载脚本"命令，无需额外付费

## 常见问题

1. 中文显示乱码：检查curses.setlocale(curses.LC_ALL, '')是否添加，确保系统编码为UTF-8
2. 命令执行失败：检查命令参数是否正确，跨平台命令是否适配
3. 内存占用过高：确认resource.py的监控线程已启动，限制参数是否正确
4. Kali工具调用失败：检查是否已安装对应工具（如apt install nmap），确保命令路径正确

## 许可证

MIT License