# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 18_poly_example.py
# @Time     : 2024/10/12 22:03


# class Animal:
#     def cry(self):
#         pass
#
#
# class Cat(Animal):
#     def cry(self):
#         print("小猫 喵喵叫...")
#     # pass
#
#
# class Dog(Animal):
#     def cry(self):
#         print("小狗 汪汪叫...")
#
#
# class Bird(Animal):
#     def cry(self):
#         print("小鸟 喳喳叫...")
#
#
# class Pig(Animal):
#     def cry(self):
#         print("小猪 噜噜叫...")
#
#
# # class AA:
# #     def cry(self):
# #         pass
#
#
# # 注意：在Python 面向对象编程中，子类对象可以传递给父类类型
# # def func(animal: AA):
# def func(animal: Animal):
#     print(f"animal 类型是{type(animal)}")
#     animal.cry()
#
#
# # 创建三个对象
# cat = Cat()
# dog = Dog()
# pig = Pig()
# bird = Bird()
#
#
# # 调用函数
# func(cat)
# func(dog)
# func(pig)
# func(bird)


# 1）Python 中函数/方法的参数是没有类型限制的，所以多态在 Python 中的体现并不是很严谨
# （比如和 Java 等强类型语言比）
# 2）Python 并不要求严格的继承体系，关注的不是对象的类型本身，而是它是否具有要调用的方法（行为）
class AA:
    def hi(self):
        print("AA-hi()...")


class BB:
    def hi(self):
        print("BB-hi()...")


def test(obj):
    obj.hi()


aa = AA()
bb = BB()
test(aa)
test(bb)











