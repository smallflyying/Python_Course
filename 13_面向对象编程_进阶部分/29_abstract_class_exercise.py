# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 29_abstract_class_exercise.py
# @Time     : 2024/10/13 14:04
from abc import ABC, abstractmethod

# 编程题
# 1）编写一个Employee类，做成抽象基类，包含如下三个属性：name, id, salary，
# 提供必要的构造器和抽象方法：work()
# 2）对应 Manager类来说，他既是员工，还具有奖金(bonus)的属性，请使用继承的思想，设计
# CommonEmployee 类和Manager 类，要求实现work()，提示“经理/普通员工 名字 工作中......”
# OOP继承 + 抽象类


# 父类
class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


# 子类 CommonEmployee
class CommonEmployee(Employee):
    def work(self):
        print(f"普通员工 {self.name} 工作中......")


# 子类 Manager
class Manager(Employee):

    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理 {self.name} 工作中......")


# 测试
manager = Manager("tom", 1-10001, 10000, 100000)
manager.work()

commonEmployee = CommonEmployee("jack", 1-10010, 8000)
commonEmployee.work()

# 自己写的
# class Employee(ABC):
#     __name = None
#     __id = None
#     __salary = None
#
#     def __init__(self, name, id, salary):
#         self.__name = name
#         self.__id = id
#         self.__salary = salary
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_id(self, id):
#         self.__id = id
#
#     def get_id(self):
#         return self.__id
#
#     def set_salary(self, salary):
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class CommonEmployee(Employee):
#
#     def work(self):
#         print(f"普通员工 {self.name} 工作中......")
#
#
# class Manager(Employee):
#     __bonus = None
#
#     def __init__(self, name, id, salary, bonus):
#         super().__init__(name, id, salary)
#         self.__bonus = bonus
#
#     def work(self):
#         print(f"经理 {self.name} 工作中......")
#
#
# commonEmployee = CommonEmployee("tim", 1, 10000)
# commonEmployee.work()
#
# manager = Manager("tom", 2, 20000, 10000)
# manager.work()


