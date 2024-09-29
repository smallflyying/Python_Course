# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 05_method_example.py
# @Time     : 2024/9/29 22:25


"""
定义一个Person 类(name,age), 完成如下要求：
1）添加 hi 成员方法，输出 "hi,python"
2）添加 cal01 成员方法，可以计算从 1+...+1000 的结果
3）添加 cal02 成员方法，该方法可以接收一个数 n，计算从 1+...+n 的结果
4）添加get_sum 成员方法，可以计算两个数的和，并返回
"""


class Person:
    # 属性(成员变量)
    name = None
    age = None

    # 成员方法
    # 1）添加 hi 成员方法，输出 "hi,python"
    def hi(self):
        print("hi,python")

    # 2）添加 cal01 成员方法，可以计算从 1+...+1000 的结果
    def cal01(self):
        result = 0
        for i in range(1, 1001):
            result += i
        print("result=", result)

    # 3）添加 cal02 成员方法，该方法可以接收一个数 n，计算从 1+...+n 的结果
    def cal02(self, n):
        result = 0
        for i in range(1, n + 1):
            result += i
        print("result=", result)

    # 4）添加 get_sum 成员方法，可以计算两个数的和，并返回
    def get_sum(self, n1, n2):
        return n1 + n2


# 完成测试
p = Person()
# 通过对象名.方法名() 调用方法
p.hi()
p.cal01()
p.cal02(10)  # 55
print(p.get_sum(10, 20))  # 30
