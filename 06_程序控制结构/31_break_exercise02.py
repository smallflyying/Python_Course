# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 31_break_exercise02.py
# @Time     : 2024/9/16 15:04


# 实现登录验证，有三次机会，如果用户名为 "张无忌" , 密码 "888"
# 提示登录成功，否则提示还有几次机会， 请使用for+break完成

"""
    思路分析:
    1. 实现登录验证，有3次机会，使用for循环3次
    2. 接收用户的输入 (名字name + 密码password, 如果满足条件，就break)
    3. 根据登录的情况，提示成功/ 还有几次登录机会
"""

# 定义一个变量-表示还有几次登录机会
chance = 3

# 登录3次
for i in range(1, 4):
    username = input("请输入登录名：")
    password = input("请输入密码：")
    chance -= 1
    # 判断是否成功
    if username == "张无忌" and password == "888":
        print("登录成功, 恭喜小伙伴")
        break
    else:
        print(f"登录失败，还有 {chance}次机会")
