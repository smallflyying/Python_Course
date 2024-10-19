# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 06_exception_exercise_01.py
# @Time     : 2024/10/19 23:42


# 如果用户输入的不是一个整数，就提示他反复输入，直到输入一个整数为止


age = 0
while True:  # 无限循环
    try:
        age = int(input("请输入年龄(要求时整数): "))
        break
    except Exception as e:
        print("你输入的年龄不是整数，请重新输入")

print(f"你输入的age={age}")
