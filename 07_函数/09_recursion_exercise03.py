# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 09_recursion_exercise03.py
# @Time     : 2024/9/19 22:01



# 3、求函数值，已知 f(1) = 3, f(n) = 2 * f(n-1)+1；请使用递归的思想编程，
# 求出 f(n) 的值？
"""
    思路分析
    1. 这个题，已经给出了推导公式
    2. 我们将其翻译成的对应的代码即可
"""
def f(n):
    if n == 1:
        return 3
    else:
        return 2 * f(n - 1) + 1


print(f(10))


# 自己写的
def get_sum(n):
    if n == 1:
        return 3
    else:
        return 2 * get_sum(n - 1) + 1

print(get_sum(5))

