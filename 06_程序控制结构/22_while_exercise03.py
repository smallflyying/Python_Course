# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 22_while_exercise03.py.py
# @Time     : 2024/9/15 10:34

# 不断输入姓名，直到输入 "exit" 为止

"""
    思路分析:
    1. 定义变量 name 接收用户输入
    2. 使用while判断，如果 name != "exit" 就循环的输入即可
"""
name = input("请输入姓名: ")
while name != "exit":
    name = input("请输入姓名: ")
    print("输入的内容是: ", name)

# 自己写的
# name = str(input("请输入姓名: "))
# while name:
#     if name != "exit":
#         name = str(input("请输入姓名: "))
#     else:
#         print("退出")
#         break

