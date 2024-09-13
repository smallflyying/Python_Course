# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_bool_operator.py
# @Time     : 2024/9/8 22:58


# and   x and y 布尔"与" : 如果 x 为 False, x and y 返回 x 的值, 则返回 y 的计算值. (a and b) 返回 20
# or    x  or y 布尔"或" : 如果 x 为 True, 它返回 x 的值, 否则它返回 y 的计算值. (a or b) 返回 10
# not   x not y 布尔"非" : 如果 x 为 True, 返回 False . 如果 x 为 False, 它返回 True. not(a and b) 返回 False

a = 10
b = 20
print(a and b) # 20
print(a or b) # 10
print(not (a and b)) # False