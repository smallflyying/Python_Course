# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 11_super_exercise.py
# @Time     : 2024/10/10 23:04


# 1、分析下面的代码，看看输出什么内容？

class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A-fly()...")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B-fly()...")


# C->B->A
class C(B):
    n1 = 100

    def fly(self):
        print("C-fly()...")

    def say(self):
        print(self.n1)  # 100
        print(self.n2)  # 400
        print(self.n3)  # 600
        print(super().n1)  # 200
        print(B.n1)  # 200
        print(C.n1)  # 100

        # 针对上面的程序，想在C的say()中，调用C的fly() 和 A的fly()，应该如何调用？
        self.fly()  # C-fly()...
        # super().fly()  # 不行
        A.fly(self)  # A-fly()...
        super().fly()  # B-fly()...


c = C()
c.say()