# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 12_ternary_operator_exercise.py
# @Time     : 2024/9/9 22:44

# 请使用前面讲的 if-else 方式，得到3个数的最大值 [代码：12_ternary_operator_exercise.py]
# 老韩提醒：看课程小伙伴，暂停，先自己做，再听老师评讲

"""
    思路分析
    1. a, b, c三个数
    2. 先求出a , b 的最大值 max1
    3. 再求出 max1 和 c 的最大值
"""
from operator import ifloordiv

# 1. a, b, c三个数
a = 30
b = 50
c = 53
# 2. 先求出a , b 的最大值 max1
max1 = a if a > b else b
# 3. 再求出 max1 和 c 的最大值
max2 = max1 if max1 > c else c
print(f"max2 = {max2}")

# 我们还可以使用一条语句完成，即可以支持嵌套使用，可读性差，知道可以这样使用即可
# 不推荐...
# 方式一：韩老师代码
# max = (a if a > b else b) if (a if a > b else b) > c else c
# 方式二：自己写的代码
max = a if a > b and a > c else (b if b > c else c)
print(f"max = {max}")