# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 08_recursion_exercise02.py
# @Time     : 2024/9/19 21:37


# 猴子吃桃子问题：有一堆桃子，猴子第一天吃了其中的一半，并再多吃了一个！
# 以后每天猴子都吃其中的一般，然后再多吃一个。当到第10天时，想再吃时（即还没吃），
# 发现只有1个桃子了。问题：最初共多少个桃子？
"""
    思路分析:
    1. day == 10 时，有桃子数: 1
    2. day == 9 时，有桃子数: (day10 的桃子数 + 1)*2
    3. day == 8 时，有桃子数: (day9 的桃子数 + 1)*2
    4. day == 7 时，有桃子数: (day8 的桃子数 + 1)*2
    5. 看到这个关系。
"""

# 定义函数，返回对应天数的桃子数
def peach(day):
    if day == 10:
        return 1
    # 如果是1<=day<10的范围就是从最后一天开始推导
    else:
        return (peach(day + 1) + 1) * 2


# 完成测试
print("最初桃子数为: ", peach(1))



# 自己写的
# def get_Peaches(day):
#     if day == 10:
#         return 1
#     else:
#         return (get_Peaches(day + 1) + 1)*2
#
#
# print(get_Peaches(1))
