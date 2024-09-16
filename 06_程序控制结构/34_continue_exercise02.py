# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 34_continue_exercise02.py
# @Time     : 2024/9/16 20:55

# 2、请分析下面的代码输出结果是什么?

for i in range(0, 2):
    for j in range(1, 4):
        if j == 2:
            continue
        print("i = ", i, "j = ", j)

# 内存分析法:
# 输出结果
# i = 0 j = 1
# i = 0 j = 3
# i = 1 j = 1
# i = 1 j = 3
