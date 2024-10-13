# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 34_homework03.py
# @Time     : 2024/10/13 21:19


# 3、编写Doctor类，属性：name,age,job,gender,sal,
# 5个参数的构造器，重写__eq__()方法，
# 并判断测试类中创建的两个对象是否相等(相等就是判断属性是否相同)

class Doctor:
    def __init__(self, name, age, job, gender, sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal

    # 重写__eq__
    def __eq__(self, other):
        # 如果other类型不是Doctor直接返回False
        if not isinstance(other, Doctor):
            return False
        # 如果所有的属性都相同，则返回True
        return (self.name == other.name and
                self.age == other.age and
                self.job == other.job and
                self.gender == other.gender and
                self.sal == other.sal)


# 测试
# doctor1 = Doctor("king", 20, "牙科医生", "男", 10000)
doctor1 = Doctor("king", 30, "牙科医生", "男", 20000)
doctor2 = Doctor("king", 20, "牙科医生", "男", 10000)

# print("doctor1 == doctor2", doctor1 == doctor2)  # True
print("doctor1 == doctor2", doctor1 == doctor2)  # False

# 自己写的
# class Doctor:
#     name = None
#     age = None
#     job = None
#     gender = None
#     sal = None
#
#     def __init__(self, name, age, job, gender, sal):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.gender = gender
#         self.sal = sal
#
#     def __eq__(self, other):
#         if not isinstance(other, Doctor):
#             return False
#         return (self.name == other.name
#                 and self.age == other.age
#                 and self.job == other.job
#                 and self.gender == other.gender
#                 and self.sal == other.sal)
