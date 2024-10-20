# @Version  : 1.0
# @Author   : LiHongFei
# @File     : temp.py
# @Time     : 2024/10/20 0:58
import time
import pyecharts
print(pyecharts.__version__)

# print(hex(ord("李")))  # => 编码


# 分析如何保存时间-格式要求

print(time.time())
print(time.localtime(time.time()))
print(time.strftime("%m-%d %H:%M:%S", time.localtime(time.time())))

