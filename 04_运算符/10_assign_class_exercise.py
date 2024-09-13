# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 10_assign_class_exercise.py
# @Time     : 2024/9/9 22:08

# 有两个变量，a 和 b，要求将其进行交换，动动脑筋，要求不使用前面老师讲过两种方式完成
"""
    老师分享
    1. a, b 记录值
    2. 需要各位小伙伴动动脑筋
    a = 1, b = 2
    a = a + b
    b = a - b
    a = a - b
"""
a = 1
b = 2
print(f"交换前 a = {a} b = {b}")
a = a + b
b = a - b
a = a - b
print(f"交换后 a = {a} b = {b}")
