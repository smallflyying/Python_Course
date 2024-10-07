# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 18_homework06.py
# @Time     : 2024/10/7 21:14


# 6、试写出以下代码的运行结果(?)
class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i =", self.i)  # 101
        print("j =", j)  # 101


d1 = Demo()
d2 = d1
d2.m()
print(d1.i)  # 101
print(d2.i)  # 101
