# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 11_function_arg.py
# @Time     : 2024/9/19 22:55


# 定义一个函数，可以返回两个数的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f1(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值
    @param fun: 表示接收一个函数
    @param num1: 传入的数
    @param num2: 传入数
    @return: 最大值
    """
    return fun(num1, num2)

def f2(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值，同时返回两个数的和
    @param fun:
    @param num1:
    @param num2:
    @return:
    """
    return num1 + num2, fun(num1, num2)


# 测试
print(f1(get_max_val, 50, 20))
x, y = f2(get_max_val, 10, -20)
print(f"x = {x} y = {y}")