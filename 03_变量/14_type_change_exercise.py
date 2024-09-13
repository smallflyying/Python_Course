# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 14_type_change_exercise.py
# @Time     : 2024/9/6 23:06
from idlelib.configdialog import is_int

# 课堂练习题 5min思考
i = 10
j = float(i)
print(type(i))  # int类型
print(type(j))  # float类型

i = j + 1  # 10.0 + 1 = 11.0
print(type(i))  # float类型
print(type(j))  # float类型

print(i)  # 11.0
print(int(i))  # 11
print(type(i))  # float类型