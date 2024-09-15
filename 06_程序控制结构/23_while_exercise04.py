# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 23_while_exercise04.py.py
# @Time     : 2024/9/15 10:44

# 打印1~100之间所有是9的倍数的整数， 统计个数 及 总和

"""
    思路分析
    1. 定义i = 1 max_num = 100, 表示我们要遍历的范围
    2. 如果 i % 9 == 0 则说明 i 是 9 的倍数
    3. 定义count 来统计个数 count += 1 定义 sum 来累加 总和 sum += i
"""

i = 1
max_num = 100
# 定义count 来统计个数
count = 0
# 定义 sum 来累加 总和
sum = 0
# 遍历 1-100
while i <= max_num:
    if i % 9 == 0:
        # 输出i
        print(i)
        count += 1
        sum += i
    i += 1

print(f"count = {count} sum = {sum}")



# 自己写的
# num = 1
# max_num = 100
# sum = 0
# count = 0
# while num <= max_num:
#     if num % 9 == 0:
#         print(num)
#         sum += num
#         count += 1
#     num += 1
# print("总个数为: ", count)
# print("总和为: ", sum)
