# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 01_cal_question.py
# @Time     : 2024/9/17 17:30


# 接受用户的输入
n1 = float(input("请输入一个数: "))
n2 = float(input("请输入一个数: "))
oper = input("请输入一个运算符 +,-,*,/ : ")
# 统计结果
res = 0.0
# 多分支的判断
if oper == "+":
    res = n1 + n2
elif oper == "-":
    res = n1 - n2
elif oper == "*":
    res = n1 * n2
elif oper == "/":
    res = n1 / n2
else:
    print("输入的运算符不对.")

print(n1, oper, n2, " = ", res)

# 如果还有这样的需求 -> 拷贝？
