# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 21_while_exercise02.py.py
# @Time     : 2024/9/15 10:29

# 打印40-200之间所有的偶数
"""
    思路分析：
    1. 定义变量 i = 40 max_num = 200, 表示我们要遍历的范围 while
    2. 如果 i % 2 == 0, 说明当前i是可以被2整除
    3. 满足条件输出即可， 注意遍历时 i += 1
"""

i = 40
max_num = 200
# 遍历40-200
while i <= max_num:
    # 如果 i 是偶数
    if i % 2 == 0:
        print(i)
    i += 1


# 自己写的
# i = 40
# while i <= 200:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# 或者
# i = 40
# while i <= 200:
#     if i % 2 == 0:
#         print(i)
#     i += 2
