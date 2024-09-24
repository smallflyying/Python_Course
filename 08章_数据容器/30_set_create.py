# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 30_set_create.py
# @Time     : 2024/9/24 22:26



set1 = {ele * 2 for ele in range(1, 5)}
print("set1:", set1)  # {8, 2, 4, 6}


# 思考题：
set2 = {ele + ele for ele in "你好呀"}
print("set2:", set2)  # {'你你', '好好', '呀呀'}