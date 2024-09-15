# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 24_while_exercise05.py.py
# @Time     : 2024/9/15 10:58

"""
    思路分析：
    1. 定义一个遍历num，接收用户的输入整数
    2. 遍历 0-num，第一个加数是 0-num 第二个加数是 num-0
    3. 使用while循环完成即可
"""
num = int(input("请输入一个整数："))
i = 0
# 遍历 0-num
while i <= num:
    print(f"{i} + {num - i} = {num}")
    i += 1


# # 自己写的
# num = int(input("请输入一个整数："))
# i = 0
# while num >= 0:
#     print(f"{i} + {num} = {i + num}")
#     i += 1
#     num -= 1

