# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_homework01.py
# @Time     : 2024/9/27 23:03


# 1、编程题
# 随机生成10个整数(1-100的范围)保存到列表，使用冒泡排序，对其进行从大到小排序


# 随机生成10个整数(1-100的范围)保存到列表
import random

list_num = []
for _ in range(10):
    list_num.append(random.randint(1, 100))

print("排序前 list_num:", list_num)


# 使用冒泡排序
# 使用冒泡排序，对其进行从大到小排序
def bubble_sort(my_list):
    """
    功能: 对传入的列表排序-顺序是从大到小
    @param my_list: 传入的列表
    @return: 无
    """
    """
        通过分析，我们发现每一轮的比较逻辑是一样的，
        我们只需要考虑变化的部分即可，使用外层的for循环来处理
    """
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


# 完成排序
bubble_sort(list_num)
print("排序后 list_num:", list_num)

# 自己写的
# import random
#
# query_list = []
# for i in range(10):
#     query_list.append(random.randint(1, 100))
# print("排序前:", query_list)
#
#
# def bubble_sort(my_list):
#     for j in range(len(my_list) - 1):
#         for k in range(len(my_list) - 1 - j):
#             if my_list[k] < my_list[k + 1]:
#                 my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
#
#
# bubble_sort(query_list)
# print(f"排序后: {query_list}")
