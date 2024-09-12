# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 02_bit_operator.py
# @Time     : 2024/9/12 22:31

# 位运算的案例

print(~-2)  # 1
print(~2)   # -3
print(2 & 3)  # 2
print(2 ^ -3)  # -1
print(2 | 3)  # 3

print(5 << 1)  # 10
print(-5 << 1) # -10
print(7 << 2)  # 28
print(-7 << 2)  # -28
print(5 >> 1)  # 2
print(-5 >> 1)  # -3

print(8 >> 2)  # 2
print(-13 >> 2) # -4

print(1 >> 2)  # 0
print(-1 >> 2)  # -1