# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_object_bool.py
# @Time     : 2024/9/28 15:59

print("---下面对象的布尔值为False---")
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))  # 空列表
print(bool(()))  # 空元组
print(bool({}))  # 空字典
print(bool(set()))  # 空集合

# 因为所有对象都有一个布尔值，所以有些代码直接使用对象的布尔值做判断
# content = "hello"
content = ""
if content:
    print(f"hi {content}")
else:
    print("空字符串")

# print(bool(content))  # True

# lst = [1, 2]
lst = []
if lst:
    print(f"lst: {lst}")
else:
    print("空列表")

# print(bool(lst))  # False
