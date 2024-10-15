# @Version  : 1.0
# @Author   : LiHongFei
# @File     : my_tools.py
# @Time     : 2024/10/15 22:28
"""
    说明：编写工具函数，供程序员使用
"""


def read_confirm_select():
    """
    确认用户输入的是(Y/N), 不区分大小写，
    如果用户输入的不是Y/N 就反复输入
    :return:
    """
    print("请输入你的选择(Y/N), 请确认选择: ", end="")
    while True:
        key = input()
        # if key.lower() == "y" or key.lower() == "n":
        # 不区分大小写 casefold()
        if key.casefold() == "y" or key.casefold() == "n":
            break
        else:
            print("选择错误, 请重新输入: ", end="")
    return key.lower()


