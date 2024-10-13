# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 22_poly_exercise_02.py
# @Time     : 2024/10/12 23:08


# 3、编程题：
# 1）定义员工类Employee，包含私有属性(姓名和月工资)，以及计算年工资get_annual的方法
# 2）普通员工(Worker)和经理(Manager)继承员工类，经理类多了奖金bonus属性和管理manage方法，
# 普通员工多了work方法，普通员工和经理类要求根据需要重写get_annual方法
# 3）编写函数show_emp_annual(e: Employee)，实现获取任何员工对象的年工资
# 4）编写函数working(e: Employee)，如果是普通员工，则调用work方法，
# 如果是经理，则调用manage方法

"""
    思路分析：
"""


# 父类Employee
class Employee:
    # 包含私有属性(姓名和月工资)
    __name = None
    __salary = None

    # 构造器
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # 计算年工资get_annual的方法
    def get_annual(self):
        return self.__salary * 12

    # 编写set_xxx 和 get_xxx
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


# 子类Worker
class Worker(Employee):

    def work(self):
        print(f"普通工人: {self.get_name()} 正在工作中...")


# 子类Manager
class Manager(Employee):
    __bonus = None

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.__bonus = bonus

    def manage(self):
        print(f"经理: {self.get_name()} 正在管理中...")

    # 根据需要，重写manager的年工资方法
    def get_annual(self):
        # self().get_annual()将会调用自身的get_annual方法,将会产生死递归循环
        # return self().get_annual() + self.__bonus
        return super().get_annual() + self.__bonus


# 编写函数show_emp_annual(e: Employee)，实现获取任何员工对象的年工资
def show_emp_annual(e: Employee):
    print(f"{e.get_name()} 年工资是: {e.get_annual()}")


# 测试
worker = Worker("king", 10000)
show_emp_annual(worker)

manager = Manager("lucy", 20000, 100000)
show_emp_annual(manager)


# 4）编写函数working(e: Employee)，如果是普通员工，则调用work方法，
# 如果是经理，则调用manage方法

def working(e: Employee):
    # 如果是普通员工
    if isinstance(e, Worker):
        e.work()
    # 如果是经理
    elif isinstance(e, Manager):
        e.manage()
    else:
        print("无法确定工作状态...")


working(worker)
working(manager)

# 自己写的
# class Employee:
#     __name = None
#     __month_salary = None
#
#     def __init__(self, name, month_salary):
#         self.__name = name
#         self.__month_salary = month_salary
#
#     def get_annual(self):
#         return self.__month_salary * 12
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_month_salary(self, month_salary):
#         self.__month_salary = month_salary
#
#     def get_month_salary(self):
#         return self.__month_salary
#
#
# class Worker(Employee):
#
#     def __init__(self):
#         pass
#
#     def work(self):
#         print("I'm working")
#
#     def get_annual(self):
#         return super().get_annual()
#
#
# class Manager(Employee):
#     __bonus = None
#
#     def __init__(self, bonus):
#         self.__bonus = bonus
#
#     def manage(self):
#         print("I'm managing")
#
#     def get_annual(self):
#         return super().get_annual() + self.__bonus
#
#
# def show_emp_annual(e: Employee):
#     print(e.get_annual())
#
#
# def working(e: Employee):
#     if isinstance(e, Worker):
#         e.work()
#     elif isinstance(e, Manager):
#         e.manage()
#
#
# # 测试代码
# work = Worker()
# work.set_name("张三")
# work.set_month_salary(5000)
# manager = Manager(50000)
# manager.set_name("李四")
# manager.set_month_salary(50000)
# show_emp_annual(work)
# working(work)
# show_emp_annual(manager)
# working(manager)
