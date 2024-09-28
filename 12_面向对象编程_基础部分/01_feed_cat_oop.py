# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 01_feed_cat_oop.py
# @Time     : 2024/9/28 15:23

# 定义一个猫类. age, name, color 是属性，或者称为成员变量
# Cat类 就是你自己定义的一个新类型

# 定义Cat 类
class Cat:
    # age, name, color 是属性
    age = None  # 年龄属性
    name = None  # 名字属性
    color = None  # 颜色属性
    weight = None  # 体重属性


# 通过Cat类，创建 实例（实例对象/对象）
cat1 = Cat()

# 通过对象名.属性名 可以给各个属性赋值
cat1.name = "小白"
cat1.age = 2
cat1.color = "白色"
# cat1.weight = 3

# 通过对象名.属性名，可以访问到属性
print(f"cat1的信息为: name: {cat1.name} age: {cat1.age} color: {cat1.color}")

# 小结：通过上面的OOP方式解决问题，可以更好的管理小猫的属性