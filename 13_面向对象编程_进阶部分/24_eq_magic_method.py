# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 24_eq_magic_method.py
# @Time     : 2024/10/13 10:44


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 判断两个Person 对象的内容是否相等，
    # 如果两个Person对象的各个属性值都一样，则返回True，反之False

    def __eq__(self, other):

        # 判断other是不是Person
        if isinstance(other, Person):
            return (self.name == other.name and
                    self.age == other.age and
                    self.gender == other.gender)
        return False

    # 重写 __lt__
    def __lt__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age < other.age
        return "类型不一致，不能比较"

    # 重写 __le__
    def __le__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age <= other.age
        return "类型不一致，不能比较"

    # 重写 __ne__
    def __ne__(self, other):
        return not self.__eq__(other)


class Dog:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 没有重写 __eq__ 前， == 比较的是内存地址

p1 = Person('john', 39, '男')
p2 = Person('john', 20, '男')
dog = Dog('john', 28, '男')
# print(f"p1==p2: {p1 == p2}")  # False
print(f"p1==p2: {p1 == p2}")  # True
# print(f"p1==dog: {p1 == dog}")  # False

# 重写 __eq__ 后， == 比较的是属性/内容

print(f"p1 < p2: {p1 < p2}")  # False
# print(f"p1 < p2: {p1 < p2}")  # True
print(f"p1 <= p2: {p1 <= p2}")  # True
print(f"p1 != p2: {p1 != p2}")  # True



