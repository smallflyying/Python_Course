# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 16_homework04.py
# @Time     : 2024/10/7 20:49


# 4、编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，
# 定义四个方法实现求和、差、乘、商(要求除数为0的话，要提示)
# 并创建对象，分别测试

"""
    思路分析
    1. 类名：Cal
    2. 属性：num1, num2
    3. 构造器/构造方法：__init__(self, num1, num2)
    4. 定义四个方法实现求和 def sum()、差 def minus()、乘 def mul()、商 def div()
    5. 商(要求除数为0的话，要提示)
"""


class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 和
    def sum(self):
        return self.num1 + self.num2

    # 减
    def minus(self):
        return self.num1 - self.num2

    # 乘
    def mul(self):
        return self.num1 * self.num2

    # 除
    def div(self):
        # 商(要求除数为0的话，要提示)
        if self.num2 == 0:
            print("num2 不能为0")
            return None
        else:
            return self.num1 / self.num2


# 测试
# cal = Cal(2, 10)
cal = Cal(2, 0)
print("和=", cal.sum())
print("差=", cal.minus())
print("乘=", cal.mul())
print("商=", cal.div())


# 自己写的
# class Cal:
#     num1 = None
#     num2 = None
#
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self):
#         sum = self.num1 + self.num2
#         print("和:", sum)
#
#     def sub(self):
#         sub = self.num1 - self.num2
#         print("差:", sub)
#
#     def mul(self):
#         mul = self.num1 * self.num2
#         print("乘:", mul)
#
#     def div(self):
#         if self.num2 == 0:
#             print("除数不能为0")
#         else:
#             div = self.num1 / self.num2
#             print("商:", div)
#
#
# # 测试
# cal = Cal(10, 0)
# cal.add()
# cal.sub()
# cal.mul()
# cal.div()

