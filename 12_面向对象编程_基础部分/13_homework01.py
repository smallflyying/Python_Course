# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 13_homework01.py
# @Time     : 2024/10/7 17:26


# 1.编写类A01，定义方法max，实现求某个float
# 列表list = [1.1, 2.9, -1.9, 67.9]的最大值，并返回

"""
    思路分析
    1. 类名：A01
    2. 方法：max(self, lst)，功能：返回列表的最大值
"""
class A01:
    def max(self, lst):
        return max(lst)

    # def __init__(self):
    #     print("ok")


#  完成测试
a = A01()
print("最大值=", a.max([1.1, 100, 2.9, -1.9, 67.9]))  # 100

