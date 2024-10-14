# @Version  : 1.0
# @Author   : LiHongFei
# @File     : house_operation.py
# @Time     : 2024/10/14 22:29

"""
    说明：提供对房屋的各种操作
"""

# 1. 使用字典来存储房屋信息
# 2. 一个字典对象就对应一个房屋信息
# 3. 多个字典/房屋信息，就放到list中进行管理
# 4. 设计 houses = [{"id":2, "name":"tim", "phone":"112", "address":"海淀", "rent":800, "state":"未出租"}, {}...]


# 全局变量 即 houses,存放所有的房屋信息
# 为了测试方便，放一个测试数据到该列表
houses = [{"id": 1, "name": "tim", "phone": "112", "address": "海淀", "rent": 800, "state": "未出租"}]


# 全局变量id_counter 记录当前房屋的id
id_counter = 1


def add_house():
    """
    添加房屋信息
    @return:
    """
    print("添加房屋".center(32, "="))
    name = input("姓名: ")
    phone = input("电话: ")
    address = input("地址: ")
    rent = int(input("租金: "))
    state = input("状态: ")
    # 由系统分配添加的房屋id
    global id_counter
    id_counter += 1
    # 构建房屋信息对应的字典，加入到全局houses列表
    house = {"id": id_counter, "name": name, "phone": phone,
             "address": address, "rent": rent, "state": state}
    houses.append(house)
    print("添加房屋成功".center(32, "="))


def list_houses():
    """
    显示房屋列表
    @return:
    """
    print("房屋列表".center(60, "="))
    # 打印表头信息
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
    # 遍历houses这个列表
    # 取出的house就是一个字典 {"id": 2, "name": "tim", "phone": "112", "address": "海淀", "rent": 800, "state": "未出租"}
    #
    for house in houses:
        # 取出house的values，并进行遍历显示
        for value in house.values():
            print(value, end="\t\t")
        # 输出以一个完整的house信息后，换行
        print()
    print("房屋列表显示完毕".center(60, "="))


def main_menu():
    """
    显示主菜单，让用户选择
    @return:
    """
    print()
    print("房屋出租系统菜单".center(32, "="))
    print("\t\t\t1 新　增　房　源")
    print("\t\t\t2 查　找　房　屋")
    print("\t\t\t3 删　除　房　屋　信　息")
    print("\t\t\t4 修　改　房　屋　信　息")
    print("\t\t\t5 房　屋　列　表")
    print("\t\t\t6 退　　　　　出")