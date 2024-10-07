# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 15_homework03.py
# @Time     : 2024/10/7 17:44


# 3.定义一个圆类Circle，定义属性：半径，提供显示圆周长的功能的方法，
# 提供显示圆面积的方法

"""
    思路分析：
    1. 类名：Circle
    2. 属性：radius
    3. 构造器：__init__(self,radius)
    4. 方法：len(self) 显示圆周长
    5. 方法：area(self) 显示面积
"""

# 导入math
import math


class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def len(self):
        len = 2 * math.pi * self.radius
        print("圆周长:", len)

    def area(self):
        area = math.pi * self.radius * self.radius
        print("圆面积:", round(area, 2))


# 测试
circle = Circle(6)
circle.len()  # 周长  37.69911184307752
circle.area()  # 面积  113.1
