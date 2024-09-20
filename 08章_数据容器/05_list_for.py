# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 05_list_for.py
# @Time     : 2024/9/20 22:15


# for 遍历列表
"""
    思路分析
    1. 因为 for 循环是直接从列表中依次取出，所以直接操作即可
    2. 每取出一个就输出/或者根据自己的业务处理
"""
list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']
for element in list_color:
    print(f"元素是: {element}")
