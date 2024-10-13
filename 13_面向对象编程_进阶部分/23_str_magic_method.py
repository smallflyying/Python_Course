# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 23_str_magic_method.py
# @Time     : 2024/10/13 10:26


class Monster:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 请输出Monster[name, job, sal] 对象的属性信息
    # 可以根据需要重写__str__
    """
        说明：
        1. 在默认情况下，调用的是父类object的__str__
        2. 父类object的__str__返回的就是类型+地址
        3. 可以根据需要重写__str__
    """

    def __str__(self):
        # return super().__str__()
        return f"{self.name} {self.age} {self.gender}"


m = Monster("hahha", 500, '111')

print(m)  # 默认输出类型+对象的地址


