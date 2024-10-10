# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 10_访问父类成员细节.py
# @Time     : 2024/10/10 22:42


# 1、子类不能直接访问父类的私有成员

# 访问父类成员细节

# class A:
#     n1 = 100
#     # 私有属性
#     __n2 = 600
#
#     def run(self):
#         print("A-run()......")
#
#     # 私有方法
#     def __jump(self):
#         print("A-jump()......")
#
#
# class B(A):
#
#     def say(self):
#         # 子类不能直接访问父类的私有成员
#         # AttributeError: type object 'A' has no attribute '_B__n2'.
#         # Did you mean: '_A__n2'?
#         # print(A.__n2)
#         # AttributeError
#         # print(super().__n2)
#         # A.__jump(self)
#         # super().__jump()
#         print("say()......")
#
#
# b = B()
# b.say()


# 访问父类成员细节

class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()...")


class A(Base):
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()......")

    def __jump(self):
        print("A-jump()......")


# B->A->Base
class B(A):

    # def fly(self):
    #     print("B-fly()...")

    def say(self):
        print("say()....")
        # 访问不限于直接父类，而是建立从子类向上级类的查找关系 A->B->Base
        # Base.n3: 表示直接访问Base类的n3属性-》800
        # A.n3: 表示直接访问A类中的n3属性-》800
        # super().n3: 表示从B类的直接父类A类去访问n3-》800
        print(Base.n3, A.n3, super().n3)  # 800 800 800
        # Base.fly(self)：表示直接访问Base类中的fly方法-》Base-fly()...
        # A.fly(self)：表示直接访问A类中的fly方法-》Base-fly()...
        # super().fly()：表示访问直接父类A的fly方法-》Base-fly()...
        # self.fly()：表示访问本类B的fly方法-》Base-fly()...
        Base.fly(self)
        A.fly(self)
        super().fly()
        self.fly()


b = B()
b.say()
