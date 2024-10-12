# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 20_isinstance_example.py
# @Time     : 2024/10/12 22:43


# isinstance 使用案例

class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


# 创建两个对象
obj = BB()
obj2 = AA()

# 分析输出的结果
print(f"obj 是不是BB的对象 {isinstance(obj, BB)}")  # True
print(f"obj 是不是AA的对象 {isinstance(obj, AA)}")  # True
print(f"obj 是不是CC的对象 {isinstance(obj, CC)}")  # False

num = 9
print(f"num 是不是int: {isinstance(num, int)}")  # True
print(f"num 是不是str: {isinstance(num, str)}")  # False
# # 是元组中的一个返回 True
print(f"num 是不是str/int/list: {isinstance(num, (str, int, list))}")  # True


