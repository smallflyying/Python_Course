# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 11_if_elif_else_exercise.py
# @Time     : 2024/9/13 23:26

# 大家都知道,男大当婚,女大当嫁.那么女方家长要嫁女儿,当然要提出一定的条件:
# 高: 180cm以上; 富: 财富1千万以上; 帅: 是. 条件从控制台输入.
# 如果这三个条件同时满足,则: "我一定嫁给他!"
# 如果三个条件有为真的情况,则: "嫁吧, 比上不足,比下有余... "
# 如果三个条件都不满足, 则: "不嫁!"
"""
    思路分析:
    1. 定义三个变量 height, money, handsome
    2. 根据输入+题给出的判断条件进行多分支判断, 输出相应的提示
    3. 使用if-elif .. - else
"""

height = float(input("身高(cm): "))
money = float(input("钱(万): "))
handsome = input("颜值(帅, 不帅): ")

if height > 180 and money > 1 and handsome == "帅":
    print("我一定嫁给他!")
elif height > 180 or money > 1 or handsome == "帅":
    print("嫁吧, 比上不足,比下有余...")
else:
    print("不嫁! ")




# 自己写的
# shenggao = bool(input("请输入身高180cm以上: "))
# caifu = bool(input("请输入财富1千万以上: "))
# shuai = bool(input("请输入帅: "))
#
# if shenggao and caifu and shuai:
#     print("我一定嫁给他!")
# elif shenggao or caifu or shuai:
#     print("嫁吧, 比上不足,比下有余.")
# else:
#     print("不嫁!")