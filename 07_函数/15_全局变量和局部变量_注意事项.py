# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 15_全局变量和局部变量_注意事项.py
# @Time     : 2024/9/19 23:30


# 1、未在函数内部重新定义 n1，那么默认使用全局变量 n1

# n1 = 100
#
#
# def f1():
#     print(n1)
#
#
# f1()


# 2、在函数内部重新定义了n1，那么根据就近原则，使用的就是函数内部重新定义的n1

# n1 = 100
#
#
# def f1():
#     # n1 重新定义了
#     n1 = 200
#     print(n1)
#
#
# f1()
# print(n1)


# 3、在函数内部使用global 关键字，可以标明指定使用全局变量

n1 = 100


def f1():
    # global 关键字标明使用全局变量n1
    global n1
    n1 = 200
    print(n1)  # 200


f1()
print(n1)  # 200

