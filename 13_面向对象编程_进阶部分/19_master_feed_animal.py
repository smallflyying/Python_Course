# @Version  : 2.0
# @Author   : LiHongFei
# @File     : 19_master_feed_animal.py
# @Time     : 2024/10/12 21:48


# 示例

# 说明：使用多态特性来优化程序

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


# 可以扩展一下 Horse, Grass, 体会多态的机制 带来的好处
class Horse(Animal):
    pass


class Grass(Food):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    # 给猫猫喂鱼
    # def feed_cat(self, cat: Cat, fish: Fish):
    #     print(f"主人{self.name} 给动物: {cat.name} 喂的食物是: {fish.name}")
    #
    # # 给小狗喂骨头
    # def feed_dog(self, dog: Dog, bone: Bone):
    #     print(f"主人{self.name} 给动物: {dog.name} 喂的食物是: {bone.name}")

    # 主人给动物喂食物
    def feed(self, animal: Animal, food: Food):
        print(f"主人{self.name} 给动物: {animal.name} 喂的食物是: {food.name}")


# 测试
master = Master("老李")
cat = Cat("小花猫")
fish = Fish("草鱼")
dog = Dog("旺财")
bone = Bone("大棒骨")
horse = Horse("小马")
grass = Grass("青草")


master.feed(dog, bone)
master.feed(dog, bone)
master.feed(horse, grass)

# 问题分析：如果动物/食物的种类很多，怎么办
