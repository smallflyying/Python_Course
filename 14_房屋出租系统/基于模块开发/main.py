# @Version  : 1.0
# @Author   : LiHongFei
# @File     : main.py
# @Time     : 2024/10/14 22:29
"""
    说明：出租系统的主程序
"""

# 导入模块house_operation
from house_operation import *


def main():
    """
    这是主函数，也就是程序的执行入口
    @return:
    """
    # 调用main_menu函数显示主菜单
    # 循环显示菜单
    while True:
        main_menu()
        key = input("请输入你的选择(1-6): ")
        if key in ["1", "2", "3", "4", "5", "6"]:
            if key == "1":
                print("输入了1-后面我们会处理逻辑")
            elif key == "2":
                print("输入了2-后面我们会处理逻辑")
            elif key == "3":
                print("输入了3-后面我们会处理逻辑")
            elif key == "4":
                print("输入了4-后面我们会处理逻辑")
            elif key == "5":
                print("输入了5-后面我们会处理逻辑")
            elif key == "6":
                break


# 测试
if __name__ == "__main__":
    main()
    print("你退出了程序,欢迎下次使用...")