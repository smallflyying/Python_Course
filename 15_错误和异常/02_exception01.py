# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 02_exception01.py
# @Time     : 2024/10/18 22:27


# 捕获异常，进行处理，这样程序可以再出现异常的情况下，继续执行
# 看看如何异常进行处理，保证程序可以继续执行
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except Exception as e:
    # 当我们得到异常后(捕获异常)，程序员自己处理。
    # 这里简单地输出异常信息
    print(f"捕获到异常，异常是: {e}")
print("程序继续执行......")



