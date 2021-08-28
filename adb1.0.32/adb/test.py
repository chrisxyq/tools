"""
# @author chrisxu
# @create 2021-01-31 20:42
# Ctrl + Alt + L：格式化代码
# ctrl + Alt + T：代码块包围
# ctrl + Y：删除行
# ctrl + D：复制行
# alt+上/下：移动光标到上/下方法
"""
import time
import subprocess

sleep_time = 1

while 1:
    # 用popen设置shell=True不会弹出cmd框
    process = subprocess.Popen('adb shell input touchscreen swipe 330 880 930 880', shell=True)
    time.sleep(sleep_time)