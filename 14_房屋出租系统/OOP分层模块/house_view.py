# @Version  : 1.0
# @Author   : LiHongFei
# @File     : house_view.py
# @Time     : 2024/10/17 23:00
"""
    说明：界面层，显示界面，接收用户的输入，调用业务层的方法
"""

from house_service import *


class HouseView:
    # 定义属性house_operation [HouseService]
    house_operation: HouseService = HouseService()

    def add_house(self):
        """
        显示添加的界面，接收用户的输入，构建House对象
        :return:
        """
        print("添加房屋".center(32, "="))
        name = input("姓名: ")
        phone = input("电话: ")
        address = input("地址: ")
        rent = int(input("租金: "))
        state = input("状态: ")

        # 构建房屋对象
        new_house = House(0, name, phone, address, rent, state)
        # 调用service方法,添加new_house
        self.house_operation.add(new_house)
        print("添加房屋成功".center(32, "="))

    def list_houses(self):
        """
        显示房屋列表
        :return:
        """
        print("房屋列表".center(60, "="))
        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
        # 先得到houses列表
        houses = self.house_operation.get_houses()
        # 遍历houses这个列表
        for house in houses:
            print(house)

        print("房屋列表显示完毕".center(60, "="))

    def main_menu(self):
        """
        显示主菜单
        :return:
        """
        while True:
            print()
            print("房屋出租系统菜单".center(32, "="))
            print("\t\t\t1 新　增　房　源")
            print("\t\t\t2 查　找　房　屋")
            print("\t\t\t3 删　除　房　屋　信　息")
            print("\t\t\t4 修　改　房　屋　信　息")
            print("\t\t\t5 房　屋　列　表")
            print("\t\t\t6 退　　　　　出")
            key = input("请输入你的选择(1-6): ")
            if key in ["1", "2", "3", "4", "5", "6"]:
                if key == "1":
                    self.add_house()
                elif key == "2":
                    print("2 查　找　房　屋")
                elif key == "3":
                    print("3 删　除　房　屋　信　息")
                elif key == "4":
                    print("4 修　改　房　屋　信　息")
                elif key == "5":
                    self.list_houses()
                elif key == "6":
                    break
