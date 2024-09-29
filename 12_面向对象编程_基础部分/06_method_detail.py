# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 06_method_detail.py
# @Time     : 2024/9/29 22:37


def hi():
    print("hi,python")


class Person:
    name = None
    age = None

    def ok(self):
        pass


# 创建了对象 p 和 p2
p = Person()
p2 = Person()

"""
    解读
    1. 动态的给p对象添加方法m1，注意只是针对p对象添加方法
    2. m1是你新增加的方法的名称，由程序员指定名字
    3. 即m1方法和函数hi关联起来，当调用m1方法时，会执行hi函数
"""
p.m1 = hi
# 调用m2(即hi)
p.m1()

print(type(p.m1), type(hi))  # function
print(type(p.ok))  # method

# 因为没有动态的给p2添加方法，会报错
# p2.m1()  # AttributeError: 'Person' object has no attribute 'm1'