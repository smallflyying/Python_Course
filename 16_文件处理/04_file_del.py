# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_file_del.py
# @Time     : 2024/10/20 12:57


# - 需求：
# 1）判断在d盘的a目录下是否有 abc.txt 文件，如果有则删除
# 2）如果没有，则提示 "文件不存在, 无法删除"


# 引入os模块，该模块提供更多的操作
import os

if os.path.exists("d://a//abc.txt"):
    os.remove("d://a//abc.txt")
else:
    print("文件不存在, 无法删除")