# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 06_recursion01.py
# @Time     : 2024/9/18 23:03


# 当执行test(4), 输出什么?
def test(n):
    if n > 2:
        test(n - 1)
        # test(n)  # RecursionError: maximum recursion depth exceeded
    # else:
    #     print("n = ", n)   # 输出 n = 2
    print("n = ", n)



# 调用test(4)
test(4)


# 阶乘， 当执行factorial(4), 返回值是多少?
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n - 1) * n
#
#
# # 执行
# print(factorial(4))   # 24
