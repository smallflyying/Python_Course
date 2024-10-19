# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 07_ raise_example.py
# @Time     : 2024/10/20 0:01


try:
    # num1 = 10
    # num2 = 0
    # res = num1 / num2
    """
        解读：
        1. raise: 用于主动的触发异常
        2. ZeroDivisionError: 程序员指定的异常，可以根据需要指定
        3. "主动触发ZeroDivisionError异常" 是指定的异常信息
    """
    raise ZeroDivisionError("主动触发ZeroDivisionError异常")
except ZeroDivisionError as e:
    print(f"捕获到异常 信息->{e} 类型->{type(e)}")



