# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_add_oper.py
# @Time     : 2024/9/3 22:58
from tkinter.font import names

# +号的使用案例

name = "king"
score = 50.8

print(score + 90) # 140.8
print(name + " hi") # king hi
print("100" + "98") # 10098
print(34.5 + 100) # 134.5

print(100 + 100) # 200
print("100" + "100") # 100100
print("100" + 3) # 报错 TypeError: can only concatenate str (not "int") to str