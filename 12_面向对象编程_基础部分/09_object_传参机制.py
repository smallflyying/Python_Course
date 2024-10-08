# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 09_object_传参机制.py
# @Time     : 2024/9/30 22:47


class Person:
    name = None
    age = None


# 分析对象作为参数传递到函数/方法的机制
def f1(person):
    print(f"②person的地址:{id(person)}")
    person.name = "james"
    person.age += 1


# 创建对象p1
p1 = Person()

p1.name = "jordan"
p1.age = 21

print(f"①p1的地址: {id(p1)} p1.name: {p1.name} p1.age: {p1.age}")  # jordan 21
f1(p1)
print(f"③p1的地址: {id(p1)} p1.name: {p1.name} p1.age: {p1.age}")  # james 22
