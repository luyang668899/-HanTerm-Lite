import os
import platform

def list_directory(path='.'):
    """列出指定目录下的文件和文件夹"""
    try:
        items = os.listdir(path)
        result = []
        
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                result.append(f"[DIR]  {item}")
            else:
                size = os.path.getsize(item_path)
                result.append(f"[FILE] {item} ({size} bytes)")
        
        return "\n".join(result)
    
    except PermissionError:
        return "权限不足，无法访问此目录"
    except FileNotFoundError:
        return "目录不存在"
    except Exception as e:
        return f"列出目录失败: {str(e)}"


def search_file(filename, search_path='.'):
    """在指定路径中搜索文件"""
    results = []
    
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if filename.lower() in file.lower():
                results.append(os.path.join(root, file))
                
        # 限制搜索结果数量，避免过多结果占用内存
        if len(results) >= 50:
            results.append("... 更多结果（限制显示50个）")
            break
    
    if results:
        return "\n".join(results)
    else:
        return f"未找到包含 '{filename}' 的文件"


def file_info(filepath):
    """获取文件详细信息"""
    try:
        stat = os.stat(filepath)
        info = [
            f"文件名: {os.path.basename(filepath)}",
            f"路径: {os.path.abspath(filepath)}",
            f"大小: {stat.st_size} 字节",
            f"创建时间: {os.path.getctime(filepath)}",
            f"修改时间: {os.path.getmtime(filepath)}",
            f"访问权限: {oct(stat.st_mode)[-3:]}"
        ]
        
        return "\n".join(info)
    
    except FileNotFoundError:
        return "文件不存在"
    except Exception as e:
        return f"获取文件信息失败: {str(e)}"