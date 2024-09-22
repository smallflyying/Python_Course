# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 14_tuple_detail.py
# @Time     : 2024/9/22 10:57


"""
元组使用注意事项和细节
"""
# 1、如果我们需要一个空元组，可以通过 ()，或者 tuple() 方式来定义
# tuple_a = ()
# tuple_b = tuple()
# print(f"tuple_a 内容是{tuple_a} 类型是{type(tuple_a)}")
# print(f"tuple_b 内容是{tuple_b} 类型是{type(tuple_b)}")


# 2、元组的数据项可以有多个，而且数据类型没有限制

# tuple_c = (100, "jack", 4.5, True, "jack")
# print(tuple_c)  # (100, 'jack', 4.5, True, 'jack')
#
#  嵌套元组
# tuple_d = (100, "tom", ("天龙八部", "笑傲江湖", 300))
# print("tuple_d = ", tuple_d)  # (100, "tom", ("天龙八部", "笑傲江湖", 300))


# 3、元组的索引/下表示从0开始的

# 4、元组索引必须在指定范围内使用，否则报：IndexError: tuple index out of range
# 比如 tuple_d = (1, 2.1, '你好呀')  有效下标为 0-2

# tuple_d = (1, 2.1, '你好呀')
# 索引越界
# print(tuple_d[0])
# print(tuple_d[3])  # IndexError: tuple index out of range


# 5、元组是不可变序列(要注意其使用特点).
# 元组的元素是不能修改的，
# 会报错 TypeError: 'tuple' object does not support item assignment
# tuple_e = (1, 2.1, '你好呀')
# tuple_e[2] = 'Python'  # 不能修改


# 6、可以修改元组内 list的内容(包括 修改、增加、删除等)
# tuple_f = (1, 2.1, '你好呀', ["jack", "tom", "mary"])
# 访问元组中list及其元素
# print(tuple_f[3])  # ['jack', 'tom', 'mary']
# print(tuple_f[3][0])  # jack
# 修改
# tuple_f[3][0] = "lucy"
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '你好呀', ["luck", "tom", "mary"])
# TypeError: 'tuple' object does not support item assignment
# tuple_f[3] = [10, 20]  # 不能替换整个列表元素


# 删除
# del tuple_f[3][0]
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '你好呀', ['tom', 'mary'])

# del tuple_f[3]

# 增加
# tuple_f[3].append("smith")
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '你好呀', ['tom', 'mary', 'smith'])

# tuple_f.append("abc")  # AttributeError: 'tuple' object has no attribute 'append'


# 7、索引也可以从尾部开始，最后一个元素的索引是-1，往前一位为 -2，依此类推

# tuple_g = (1, 2.1, '你好呀', ["jack", "tom", "mary"])
# print(tuple_g[-2])  # 你好呀
# print(tuple_g[-5])  # IndexError: tuple index out of range


# 8、定义一个元素的元组，需要带上逗号
# tuple_h = (100)  # <class 'int'>
tuple_h = (100,)  # <class 'tuple'>
print(f"tuple_h的类型是{type(tuple_h)}")

