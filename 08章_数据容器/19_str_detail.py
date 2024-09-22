# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 19_str_detail.py
# @Time     : 2024/9/22 17:58



str = "hi-你好呀哈喽"
print(id(str))

# 通过索引可以访问指定元素
print(str[3])  # 你
# 不能修改元素
# str[3] = "李"  # TypeError: 'str' object does not support item assignment
str = "abc"
print(id(str))