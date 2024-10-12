# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 17_master_feed_animal.py
# @Time     : 2024/10/12 21:48


# 示例

# 说明：显示有传统的方式完成
class Food:
    name = None

    def __init__(self, name):
        self.name = name


class Fish(Food):
    # 特有的属性和方法
    pass


class Bone(Food):
    # 特有的属性和方法
    pass


class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    # 给猫猫喂鱼
    def feed_cat(self, cat: Cat, fish: Fish):
        print(f"主人{self.name} 给动物: {cat.name} 喂的食物是: {fish.name}")

    # 给小狗喂骨头
    def feed_dog(self, dog: Dog, bone: Bone):
        print(f"主人{self.name} 给动物: {dog.name} 喂的食物是: {bone.name}")


# 测试
master = Master("老李")
cat = Cat("小花猫")
fish = Fish("草鱼")
dog = Dog("旺财")
bone = Bone("大棒骨")

master.feed_cat(cat, fish)
master.feed_dog(dog, bone)

# 问题分析：如果动物/食物的种类很多，怎么办
