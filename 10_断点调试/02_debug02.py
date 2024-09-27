# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 02_debug02.py
# @Time     : 2024/9/28 0:20


name_list = ["jordan", "kobe", "james", "Messi"]
i = 0
# debug list 索引越界
while i <= len(name_list):
    print(f"name_list[{i}]={name_list[i]}")
    i += 1
