# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 13_identifier_rule.py
# @Time     : 2024/9/10 21:35

# 1、由26个英文字母大小写，0-9，_ 组成
num9_N = 100
# num~_N = 200
# 2、数字不可以开头
# 1num = 300
# 3、不可以使用关键字，，但能包含关键字
# if = 500
my_if = 600
# 4、Python 区分大小写
n = 700
N = 800
print("n= ", n, "N=", N)
# 5、标识符不能包含空格
# my name = "哈哈"