# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 03_format_output.py
# @Time     : 2024/9/3 22:29

# 格式化输出案例
# 定义变量
age = 80
score = 77.5
gender = '男'
name = "贾宝玉"

# %操作符输出 str-string
print("个人信息: %s-%d-%s-%.1f" % (name, age, gender, score))

# format()函数 注意：变量可以多几个，但是{}不能比变量少

print("个人信息: {} {} {}".format(name, age, gender))

# f-strings[推荐]
print("个人信息: {name} {age} {score} {gender}") # 个人信息: {name} {age} {score} {gender}
print(f"个人信息: {name} {age} {score} {gender}") # 个人信息: 贾宝玉 80 77.5 男
# print(f"个人信息: {name} {age} {score} {gender} {a}") # NameError: name 'a' is not defined