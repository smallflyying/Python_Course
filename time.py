# @Version  : 1.0
# @Author   : LiHongFei
# @File     : time.py
# @Time     : 2024/10/13 14:40
import time

start = time.time()
print("开始时间: 秒", start)
for i in range(1, 900000):
    print(i)
end = time.time()
print("结束时间: 秒", end)
print("执行时间: 秒", (end - start))


