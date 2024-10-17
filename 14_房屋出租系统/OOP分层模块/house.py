# @Version  : 1.0
# @Author   : LiHongFei
# @File     : house.py
# @Time     : 2024/10/17 22:55
"""
    说明：数据层：House类，一个House对象表示一个房屋信息
"""


class House:

    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state
