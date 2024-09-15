# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 20_while_exercise01.py
# @Time     : 2024/9/15 10:21

# 打印1-100之间所有能被3整除的数
"""
    思路分析：
    1. 定义变量 i = 1 max_num = 100, 表示我们要遍历的范围 while
    2. 如果 i % 3 == 0, 说明当前i是可以被3整除
    3. 满足条件输出即可， 注意遍历时 i += 1
"""
i = 1
max_num = 100
# 遍历 1-100
while i <= max_num:
    # 如果 i % 3 == 0 成立，说明 i 可以被3整除
    if i % 3 == 0:
        print(i)
    i += 1



# 自己写的
# num = 1
# while num <= 100:
#     if num % 3 == 0:
#         print(num)
#     num += 1
