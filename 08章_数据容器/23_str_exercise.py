# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 23_str_exercise.py
# @Time     : 2024/9/22 21:59


# 1、定义一个字符串，str_names = "tom jack mary nono smith lhf",
# - 统计一共有多少个人名
# - 如果有 "lhf" 则替换成 "老李"
# - 如果人名是英文，则把首字母改成大写


"""
    统计一共有多少个人名
    思路分析:
    1。 使用split方法进行分割 " "
    2. 然后统计有多少个人名即可
"""
str_names = "tom jack mary nono smith lhf 李四"
# - 统计一共有多少个人名
str_names_list = str_names.split(" ")
print(f"一共有 {len(str_names_list)} 个人名")  # 6

# - 如果有 "lhf" 则替换成 "老李"
str_names_re = str_names.replace("lhf", "老李")
print(f"替换后的结果是 {str_names_re}")

# - 如果人名是英文，则把首字母改成大写
"""
    思路分析：
    "tom jack mary nono smith lhf 张三" => "Tom Jack Mary Nono Smith Lhf 张三"
    1. 定义字符串 str_names_upper 来保持新的结果
    2. 遍历 str_names_list 列表如果发现是英文名，则将其首字母改成大写str.capitalize()
    3. 拼接到 str_names_upper即可
"""
str_names_upper = ""
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize() + " "
    # else:
    #     str_names_upper += element + " "
# 去掉两边的 " "
str_names_upper = str_names_upper.strip(" ")
print(f"如果人名是英文，则把首字母改成大写 处理结果是: {str_names_upper}")

# 自己写的
# str_names = "tom jack mary nono smith lhf"
# print(len(str_names.split()))
# if "lhf" in str_names:
#     str_names = str_names.replace("lhf", "老李")
# print(str_names)
# for name in str_names.split():
#     if name.isalpha():
#         print(name.capitalize())