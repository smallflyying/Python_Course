# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 12_type_force_change.py
# @Time     : 2024/9/6 22:35


# 显式类型转换案例

i = 10

j = float(i)
print("j的类型:", type(j), "j = ", j)

k = str(i)
print("k的类型:", type(k), "k = ", k) # str, "10"

print(k + 90)  # TypeError: can only concatenate str (not "int") to str