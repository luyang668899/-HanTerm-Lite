import subprocess
import sys

def execute_cmd(cmd):
    """执行系统命令，自动识别输出编码，防止中文乱码"""
    try:
        # 执行命令，捕获输出（stderr重定向到stdout）
        output = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, timeout=10  # 超时10秒，避免卡死
        )
        # 使用系统默认编码或尝试常见编码，不依赖chardet
        encodings = ['utf-8', 'gbk', 'latin-1']
        result = None
        for encoding in encodings:
            try:
                result = output.decode(encoding).strip()
                break
            except UnicodeDecodeError:
                continue
        if result is None:
            result = output.decode('utf-8', errors='ignore').strip()
        return result
    except subprocess.TimeoutExpired:
        return "命令执行超时（超过10秒）"
    except subprocess.CalledProcessError as e:
        # 命令执行失败仍返回输出（如nmap扫描无结果）
        encodings = ['utf-8', 'gbk', 'latin-1']
        result = None
        for encoding in encodings:
            try:
                result = e.output.decode(encoding).strip()
                break
            except UnicodeDecodeError:
                continue
        if result is None:
            result = e.output.decode('utf-8', errors='ignore').strip()
        return result
    except Exception as e:
        return f"命令执行错误：{str(e)}"