# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 16_tuple_exercise.py
# @Time     : 2024/9/22 12:00


# 定义一个元组，('大话西游','周星驰', 80, ['周新驰', '小甜甜'])，
# 信息为(片名, 导演, 票价, 演员列表)
#
#
# 1）查询票价对应索引
# 2）遍历所有的演员
# 3）删除 '小甜甜'，增加 '牛魔王'、'猪八戒'

tuple_movie = ('大话西游', '周星驰', 80, ['周新驰', '小甜甜'])
# 1）查询票价对应索引
print(f"票价对应的索引为: {tuple_movie.index(80)}")  # 2

# 2）遍历所有的演员
for ele in tuple_movie[3]:
    print(f"演员的名字: {ele}")

# 3）删除 '小甜甜'，增加 '牛魔王'、'猪八戒'
del tuple_movie[3][1]
tuple_movie[3].append('牛魔王')
tuple_movie[3].append('猪八戒')
print("-----------------------")
for ele in tuple_movie[3]:
    print(f"演员的名字: {ele}")




print(ord('李'))  # 26446
print(ord('a'))  # 97



# 自己写的：
# 1）查询票价对应索引
# tuple_movie = ('大话西游', '周星驰', 80, ['周新驰', '小甜甜'])
# print("票价对应的索引为:", tuple_movie.index(80))  # 2
#
# # 2）遍历所有的演员
# for ele in tuple_movie:
#     if type(ele) == list:
#         for ele_2 in ele:
#             print(ele_2)
#
#
# # 3）删除 '小甜甜'，增加 '牛魔王'、'猪八戒'
# del tuple_movie[3][1]
# tuple_movie[3].append('牛魔王')
# tuple_movie[3].append('猪八戒')
# print(tuple_movie)  # ('大话西游', '周星驰', 80, ['周新驰', '牛魔王', '猪八戒'])
