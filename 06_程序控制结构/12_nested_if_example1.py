# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 12_nested_if_example1.py
# @Time     : 2024/9/14 20:49


# 参加歌手比赛，如果初赛成绩大于8.0进入决赛，否则提示淘汰。
# 并且根据性别提示进入男子组或女子组。【先练习】，
# 输入成绩和性别，进行判断和输出信息。

"""
    思路分析
    1. 定义两个变量 score, gender 接收用户的输入
    2. score接收成绩，然后使用if-else判断 是否进入决赛
    3. 如果进入决赛，接收性别，再使用if-else判断，是进入男子组还是女子组
    4. 根据判断，输出对应的信息即可
"""
score = float(input("请输入成绩: "))
if score > 8.0:
    gender = input("请输入性别(男|女): ")
    if gender == "男":
        print("进入男子组决赛")
    else:
        print("进入女子组决赛")
else:
    print("成绩不达标，你被淘汰了!")