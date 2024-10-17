# @Version  : 1.0
# @Author   : LiHongFei
# @File     : house_service.py
# @Time     : 2024/10/17 23:11
"""
    说明：业务层：提供对房屋操作方法
"""


from house import *


class HouseService:
    # 定义属性houses列表，存放房屋信息(对象)
    houses = []
    # 定义属性id_counter: 记录当前房屋的id
    id_counter = 1

    def add(self, new_house: House):
        """
        将接收到的new_house添加到houses
        :param new_house:
        :return:
        """
        # 分配id给new_house
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def __init__(self):
        # 为了测试方便，在houses列表中增加一个测试数据
        house = House(1, "小明", "112", "北京", 120, "未出租")
        self.houses.append(house)

    def get_houses(self):
        """
        返回房屋列表
        :return:
        """
        return self.houses

