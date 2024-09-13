# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 03_bit_exercise.py
# @Time     : 2024/9/13 21:18

# -- 请小伙伴完成前面提出的思考题
# 代码
a = 1>>2  # 1 向右移2位
b = -1>>2
c = 1<<2
d = -1<<2

# a,b,c,d结果是多少
print("a = ", a) # a=0
print("b = ", b) # b=-1
print("c = ", c) # c=4
print("d = ", d) # d=-4

print(~2)  # -3 # 按位取反
print(2&3) # 2
print(2|3) # 3
print(~-5) # 4
print(13&7) # 5
print(5|4) # 5
print(-3^3) # -2
