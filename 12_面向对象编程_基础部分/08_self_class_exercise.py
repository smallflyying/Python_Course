# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 08_self_class_exercise.py
# @Time     : 2024/9/30 22:24

# 定义Person类
# 1）里面有name、age属性
# 2）并提供compare_to比较方法，用于判断是否和另一个人相等
# 3）名字和年龄都一样，就返回True，否则返回False

"""
    思路分析
    1. 类名：Person
    2. 属性：name、age
    3. 方法：compare_to(self, other):
    4. 功能：名字和年龄都一样，就返回True，否则返回False

"""


class Person:
    name = None
    age = None

    def compare_to(self, other):
        # 名字和年龄都一样，就返回True，否则返回False
        return self.name == other.name and self.age == other.age


# 测试
p1 = Person()
p1.name = "tom"
# p1.age = 3
p1.age = 2

p2 = Person()
p2.name = "tom"
p2.age = 3

# print(p1.compare_to(p2))  # True
print(p1.compare_to(p2))  # False
