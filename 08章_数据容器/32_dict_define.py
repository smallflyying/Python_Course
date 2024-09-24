# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 32_dict_define.py
# @Time     : 2024/9/24 23:21


# 字典的基本使用案例
# 定义字典
tel = {'jack': 4098, 'tom': 4139}
print(f"dict_tel: {tel} 类型: {type(tel)}")  # {'jack': 4098, 'tom': 4139}  dict
# 查询jack 的 tel
print(f"jack 的 tel: {tel['jack']}")  # 4098
# print(f"jack 的 tel: {tel['jack~']}")  # KeyError: 'jack~'
