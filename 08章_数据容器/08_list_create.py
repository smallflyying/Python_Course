# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 08_list_create.py
# @Time     : 2024/9/21 23:48


list1 = [ele * 2 for ele in range(1, 5)]
print("list1: ", list1)  # [2, 4, 6, 8]

list2 = [ele + ele for ele in "你好呀"]
print("list2: ", list2)  # ['你你', '好好', '呀呀']

# 再举一个案例, 要求生成一个列表, 内容为 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1*1, 2*2, 3*3...]
list3 = [ele * ele for ele in range(1, 11)]
print("list3: ", list3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]