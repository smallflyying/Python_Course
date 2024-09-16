# @Version  : 1.0
# @Author   : LiHongFei
# @File     : print_99.py
# @Time     : 2024/9/16 11:42


# 打印出九九乘法表[课后题,自己完成]

# i 控制行数
for i in range(1, 10):
    # j 控制列数
    for j in range(1, i + 1):
        # 输出公式 i * j = i * j
        # end="" 表示输出该行，但是不换行
        print(f"{i} * {j} = {i * j} \t", end="")
    # 表示每一次循环结束换行
    print("")
