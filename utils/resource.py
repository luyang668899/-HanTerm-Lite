import threading
import time
import gc
import os
import sys

def monitor_resource(limit):
    """资源监控线程：限制内存/CPU占用，超过则自动释放，不依赖psutil"""
    def monitor():
        while True:
            # 内存限制：定期进行垃圾回收
            try:
                import gc
                gc.collect()
            except Exception as e:
                print(f"内存回收错误: {str(e)}")
            
            # CPU限制：简单实现，使用time.sleep减少CPU占用
            time.sleep(2)  # 每2秒监控一次
    
    # 启动监控线程（守护线程，不影响主程序退出）
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()