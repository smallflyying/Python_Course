# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 07_self.py
# @Time     : 2024/9/29 22:58


# class Dog:
#     name = "波斯猫"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息: {name}")  # ? 加菲猫
#         # 通过self.属性名 可以访问 对象的属性/成员变量
#         print(f"name信息: {self.name}")  # 波斯猫
#
#
# dog = Dog()
# dog.info("加菲猫")


# class Dog:
#     name = "波斯猫"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息: {name}")
#
#     # 静态方法
#     # 不添加将报错：Method must have a first parameter, usually called 'self'
#     # 解读：
#     # 1.通过@staticmethod 可以将方法转为静态方法
#     # 2.如果是一个静态方法，可以不带self
#     # 3. 静态的方法的调用形式有变化
#     @staticmethod
#     def ok():
#         print("ok()...")
#
#
# dog = Dog()
# dog.info("德牧")
# # 不能直接调用普通方法
# # Dog.info("哈哈")  # TypeError: Dog.info() missing 1 required positional argument: 'name'
# # 调用静态方法
# # 方式1：通过对象调用
# dog.ok()
# # 方式2：通过类名调用
# Dog.ok()


# self 表示当前对象本身，简单地说，哪个对象调用，self就代表哪个对象
class Dog:
    name = "藏獒"
    age = 2

    def hi(self):
        print(f"hi self: {id(self)}")  # 自身


# self表示当前对象本身
# 创建对象dog2
dog2 = Dog()
print(f"dog2: {id(dog2)}")
dog2.hi()
# 创建对象dog3
print("-------------------------")
dog3 = Dog()
print(f"dog3: {id(dog3)}")
dog3.hi()
