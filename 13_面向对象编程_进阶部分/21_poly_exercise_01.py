# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 21_poly_exercise_01.py
# @Time     : 2024/10/12 22:53


# 1、代码阅读题，看下面的代码，分析输出内容是什么？

class A:
    i = 10

    # self到底是A还是B [B]
    # 当调用对象成员的时候，会和对象本身动态关联
    def sum(self):
        return self.getI() + 10

    def sum1(self):
        return self.i + 10

    def getI(self):
        return self.i


class B(A):
    i = 20

    # def sum(self):
    #     return self.i + 20

    def getI(self):
        return self.i

    # def sum1(self):
    #     return self.i + 10


# 创建B的对象b
b = B()
print(b.sum())  # 输出什么？ 40 -> 30
print(b.sum1())  # 输出什么？ 30 -> 30
