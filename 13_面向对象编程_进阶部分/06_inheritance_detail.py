# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 06_inheritance_detail.py
# @Time     : 2024/10/9 22:20


# 1、子类继承了是所有的属性和方法，非私有的属性和方法可以在子类直接访问，
# 但是私有属性和方法不能在子类直接访问，
# 要通过父类提供公共的方法去访问
# class Base:
#     # 公共属性
#     n1 = 100
#     # 私有属性
#     __n2 = 200
#
#     def __init__(self):
#         print("Base 构造方法......")
#
#     def hi(self):
#         print("hi() 公共方法");
#
#     def __hello(self):
#         print("__hello() 私有方法")
#
#     # 提供公共方法，访问私有的属性和方法
#     def test(self):
#         print("属性: ", self.n1, self.__n2)
#         self.__hello()
#
#
# class Sub(Base):
#
#     def __init__(self):
#         print("Sub 构造方法......")
#
#     def say_ok(self):
#         # 我们发现父类的非私有属性和方法可以访问
#         print("say_ok() ", self.n1)  # 100
#         self.hi()  # hi() 公共方法
#         # 我们发现弗雷德私有属性和方法不可以访问
#         # AttributeError: 'Sub' object has no attribute '_Sub__n2'
#         # print(self.__n2)
#         # AttributeError: 'Sub' object has no attribute '_Sub__hello'.
#         # Did you mean: '_Base__hello'?
#         # self.__hello()
#
#
# # 创建子类对象
# sub = Sub()
# sub.say_ok()
#
# # 调用子类继承父类的公共方法，去实现访问父类的私有成员的效果
# sub.test()


# debug 示意图：


# Python 支持多重继承
class A:
    n1 = 100

    def sing(self):
        print("A sing()...", self.n1)


class B:
    n2 = 200
    n1 = 300

    def dance(self):
        print("B dance()...", self.n2)

    def sing(self):
        print("B sing()...", self.n1)


# C类继承了 A, 和 B 类（多重继承）
# class C(A, B):
class C(B, A):
    # Python pass 是空语句，是为了保持程序结构的完整性。
    # pass 不做任何事情，一般用作占位语句
    pass


c = C()
print("-------------------------------")
# 继承的属性信息
print(f"属性信息 {c.n1} {c.n2}")  # 300 200
# 调用集成的方法
c.dance()  # B dance()... 200
c.sing()  # B sing()... 300
