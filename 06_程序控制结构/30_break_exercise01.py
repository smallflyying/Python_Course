# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 30_break_exercise01.py
# @Time     : 2024/9/16 14:52

# 1、1-100以内的数求和，求出 当和 第一次大于20的当前控制循环的变量值是多少? [for带做]
"""
    思路分析
    1. 定义变量sum累加和
    2. for遍历1-100，当sum > 20时，就退出for -break
    3. 输出当前的控制循环的变量即可
"""

# 定义变量sum累加和
sum = 0

# 遍历1-100
for i in range(1, 101):
    # 累加
    sum += i
    # 判断
    if sum > 20:
        break

# 补充：
#   在 Python 中，for 循环结束后，
#   循环变量（这里是 i）仍然会在循环体外保留其最后的值。
#   这意味着，即使循环结束，i 仍然存在于当前作用域中。
print("i = ", i)
