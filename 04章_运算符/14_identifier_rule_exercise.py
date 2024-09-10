# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 14_identifier_rule_exercise.py
# @Time     : 2024/9/10 21:40

# 练习题：判断变量名是否正确，并说明理由  (2min)

hello = 1  # True
hello12 = 2  # True
# 1hello = 1  # False, 不能以数字开头
# h-b = 1  # False，不能包含-
# x h = 1  # False，不能包含空格
# h$4 = 1  # False，不能包含$
# class = 1  # False，不能以关键字作为变量名
int = 1  # True
# or = 1  # False，or是关键字
# and = 1  # False，and是关键字
# if = 1  # False，if是关键字
_if = 600  # True
stu_name = 1  # True