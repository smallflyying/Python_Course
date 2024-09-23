# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 24_slice_use.py
# @Time     : 2024/9/23 21:35


# 对字符串进行切片
str = "hello,world"
# 需求：截取 "hello"
str_slice = str[0:5:1]
print("str_slice:", str_slice)  # "hello"


# 对列表进行切片
list_a = ["jack", "tom", "yoyo", "nono", "lhs"]
# 需求：截取 ["tom", "nono"]
list_slice = list_a[1:4:2]
print("list_slice:", list_slice)  # ['tom', 'nono']


# 对元组进行切片
tuple_a = (100, 200, 300, 400, 500, 600)
# 需求：截取 (200, 300, 400, 500)
tuple_slice = tuple_a[1:5:1]
print("tuple_slice:", tuple_slice)  # (200, 300, 400, 500)