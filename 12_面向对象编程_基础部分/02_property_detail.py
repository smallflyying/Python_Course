# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 02_property_detail.py
# @Time     : 2024/9/28 15:39


# 定义Cat类
class Cat:
    age = 2  # 年龄属性
    name = "小白"  # 名字属性
    color = "白色"  # 颜色属性


# 创建对象
cat1 = Cat()
# cat1.age = 100

print(f"age: {cat1.age} name: {cat1.name} color: {cat1.color}")
