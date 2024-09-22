# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 12_tuple_while.py
# @Time     : 2024/9/22 10:51


# while 遍历元组
tuple_color = ('red', 'green', 'blue', 'yellow', 'white', 'black')


# index=0 表示从第一个元素进行遍历
index = 0
while index < len(tuple_color):
    print(f"第{index + 1} 个元素的值: {tuple_color[index]}")
    index += 1
