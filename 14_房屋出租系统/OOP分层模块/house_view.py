# @Version  : 1.0
# @Author   : LiHongFei
# @File     : house_view.py
# @Time     : 2024/10/17 23:00
"""
    说明：界面层，显示界面，接收用户的输入，调用业务层的方法
"""


class HouseView:

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
                    print("1 新　增　房　源")
                elif key == "2":
                    print("2 查　找　房　屋")
                elif key == "3":
                    print("3 删　除　房　屋　信　息")
                elif key == "4":
                    print("4 修　改　房　屋　信　息")
                elif key == "5":
                    print("5 房　屋　列　表")
                elif key == "6":
                    break
