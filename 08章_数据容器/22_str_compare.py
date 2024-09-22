# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 22_str_compare.py
# @Time     : 2024/9/22 21:53


# 字符串比较-实例，分析输出结果
print("tom" > "lhf") # True
print("tom" > "to")  # True
print("tom" > "tomcat")  # False
print("tom" < "老李")  # True
print("tom" > "tom")  # False
print("tom" <= "tom")  # True


print(ord('t'), ord('老'), ord('李'))