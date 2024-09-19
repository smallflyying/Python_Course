# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 07_recursion_exercise01.py
# @Time     : 2024/9/19 21:27


# 1、请使用递归的方式求出斐波那契数列1，1，2，3，5，8，13...给你一个整数n，求出它的值是多少？

def fbn(n):
    """
    功能: 返回n对应的斐波那契数
    :parm n: 接收一个整数n>=1
    :return: 返回斐波那契数
    """
    if n == 1 or n == 2:
        return 1
    # 如果n > 2 则对应的斐波那契数为 n-1 和 n-2 对应的斐波那契数的和
    else:
        return fbn(n - 1) + fbn(n - 2)


# 完成测试
print(fbn(7))


# 自己独立写的
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# result = fibonacci(7)
# print("result = ", result)
