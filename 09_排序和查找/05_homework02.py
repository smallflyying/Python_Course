# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 05_homework02.py
# @Time     : 2024/9/27 23:03


# 2、编程题
# 在第1题的基础上，使用二分查找，查找是否有8这个数，如果有，则返回对应的下标，如果没有，返回-1
# 提示：注意这里要查找的列表是从大到小

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


# 编写二分查找函数
def binary_search(my_list, find_val):
    """
    功能：完成二分查找
    @param my_list: 要查找的列表（该列表是有大小顺序）
    @param find_val: 要查找的元素/值
    @return: 如果找到返回对应的下标，如果没有找到，返回 -1
    """

    left_index, right_index = 0, len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] < find_val:
            # 到列表的左边查找
            right_index = mid_index - 1
        elif my_list[mid_index] > find_val:
            # 到列表的右边查找
            left_index = mid_index + 1
        else:  # 相等
            find_index = mid_index
            break  # 找到一个就退出while
    return find_index


# 完成排序
bubble_sort(list_num)
print("排序后 list_num:", list_num)

# 使用二分查找，来查找是否有8这个元素，并返回下标，没有找到，返回-1
res_index = binary_search(list_num, 8)
if res_index == -1:
    print("没有在列表中找到8这个元素")
else:
    print("在列表中找到8这个元素，对应的下标/索引为：", res_index)


# 使用二分查找，来查找是否有8这个元素，把满足查询条件的元素的下标，都返回
# def binary_search2(my_list, find_val):
#     """
#     功能：完成二分查找
#     @param my_list: 要查找的列表（该列表是有大小顺序）
#     @param find_val: 要查找的元素/值
#     @return: 如果找到返回对应的下标，如果没有找到，返回 -1
#     """
#
#     left_index, right_index = 0, len(my_list) - 1
#     list_index = []
#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         if my_list[mid_index] < find_val:
#             # 到列表的左边查找
#             right_index = mid_index - 1
#         elif my_list[mid_index] > find_val:
#             # 到列表的右边查找
#             left_index = mid_index + 1
#         else:  # 相等
#             list_index.append(mid_index)
#
#             # 向左扩展查找相同的元素
#             i = mid_index - 1
#             while i >= 0 and my_list[i] == find_val:
#                 list_index.append(i)
#                 i -= 1
#
#             # 向右扩展查找相同的元素
#             i = mid_index + 1
#             while i < len(my_list) and my_list[i] == find_val:
#                 list_index.append(i)
#                 i += 1
#
#             # 结束查找
#             break
#     return list_index


# 使用二分查找，来查找是否有8这个元素，把满足查询条件的元素的下标，都返回
# res_index = binary_search2(list_num, 8)
# print("在列表中找到8这个元素，对应的下标/索引为：", res_index)

# 自己写的
# def binary_search(my_list, find_val):
#
#     left, right = 0, len(list_num) - 1
#
#     find_index = -1
#
#     while left <= right:
#         mid_index = (left + right) // 2
#         if my_list[mid_index] < find_val:
#             right = mid_index - 1
#         elif my_list[mid_index] > find_val:
#             left = mid_index + 1
#         else:
#             find_index = mid_index
#             break
#     return find_index
#
#
# res_index = binary_search(list_num, 8)
# print("res_index:", res_index)
