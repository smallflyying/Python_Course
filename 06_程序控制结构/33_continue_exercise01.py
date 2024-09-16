# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 33_continue_exercise01.py
# @Time     : 2024/9/16 20:53

# 1、请分析下面的代码输出结果是什么?

for i in range(0, 13):
    if i == 10:
        continue
    print("i = ", i)

# 内存分析法:
# 0 1 2 3 4 5 6 7 8 9 11 12
