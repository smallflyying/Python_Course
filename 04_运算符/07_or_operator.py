# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 07_or_operator.py
# @Time     : 2024/9/9 21:23


# or 运算符的使用
# 定义一个成绩变量
score = 70
# 判断成绩是否<=60 或者 >= 80

# print(score <= 60 or score >= 80)  # False
if score <= 60 or score >= 80:
    print("hi~~")


# 细节的案例
# 示例：
a = 1
b = 99

print(a or b)  # 1
print((a > b) or b)  # 99
print((a < b) or b)  # True