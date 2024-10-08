# @Version  : 2.0
# @Author   : LiHongFei
# @File     : 05_why_inheritance.py
# @Time     : 2024/10/8 22:54


# 使用继承的代码
# 编写父类Student
class Student:
    name = None
    age = None
    __score = None
    gender = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score


# 小学生类- 继承 Student
class Pupil(Student):

    def testing(self):
        print("...小学生在考小学数学...")


# 大学生类- 继承 Student
class Graduate(Student):

    def testing(self):
        print("...大学生在考高等数学...")


# 测试
student1 = Pupil("apple", 10)
student1.testing()
student1.set_score(70)
student1.show_info()

print("--------------------------------")
student2 = Graduate("grape", 22)
student2.testing()
student2.set_score(80)
student2.show_info()


# 继承给编程带来的便利
# 1) 代码的复用性提高了
# 2) 代码的扩展性和维护性提高了
