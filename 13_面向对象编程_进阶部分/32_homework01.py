# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 32_homework01.py
# @Time     : 2024/10/13 15:03


# 1、定义一个Person类，属性：name, age, job，创建Person 列表，有3个person对象，
# 并按照age从 大到小 进行排序。
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"{self.name}-{self.age}-{self.job}"


p1 = Person("smith", 20, "java工程师")
p2 = Person("king", 18, "学生")
p3 = Person("tom", 22, "老师")
my_list = [p1, p2, p3]


for p in my_list:
    print(p)


# 有3个person对象，并按照 age 从 大到小 进行排序。
"""
    思路分析：
    1. 解决方案：冒泡排序=>做了改进(根据需求)
    2. 解决方案：直接使用列表的.sort
"""


# 定义函数-完成排序
def bubble_sort(my_list: list[Person]):
    """
    功能: 对传入的列表排序-顺序是大到小(按照年龄)
    @param my_list: 传入的列表
    @return: 无
    """
    # i 变量来控制多少轮排序 len(my_list) - 1
    for i in range(0, len(my_list) - 1):  # [0, 1, 2, 3]
        # j变量控制比较的次数，同时可以作为比较元素的索引下标
        for j in range(0, len(my_list) - 1 - i):
            # 如果前面的元素的年龄 < 后面的元素的年龄，就交换
            if my_list[j].age < my_list[j + 1].age:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


# bubble_sort(my_list)
# 2. 解决方案：直接使用列表的.sort

"""
    解读：
    1. key=lambda ele: ele.age 表示指定按照列表元素的age属性进行排序
    2. reverse=True ： 表示逆序
"""

my_list.sort(key=lambda ele: ele.age, reverse=True)

print("排序后".center(32, "*"))

for p in my_list:
    print(p)


