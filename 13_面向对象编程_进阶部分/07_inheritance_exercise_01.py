# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 07_inheritance_exercise_01.py
# @Time     : 2024/10/9 23:06


# 1、分析下面的代码，看看输出什么内容？
class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()

print(f"son.name = {son.name} son.age = {son.age} son.hobby = {son.hobby}")  # 大头儿子 39 旅游
