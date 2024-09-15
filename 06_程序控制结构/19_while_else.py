# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 19_while_else.py
# @Time     : 2024/9/15 10:16


# while-else 使用案例
i = 0
while i < 3:
    print("你好，韩顺平教育 ", i)
    i += 1
    # 演示break 中断
    if i == 1:
        break
else:
    print("i < 3 不成立 i = ", i)
