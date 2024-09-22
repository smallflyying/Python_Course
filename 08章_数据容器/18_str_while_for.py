# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 18_str_while_for.py
# @Time     : 2024/9/22 17:50


# 使用while 和 for 遍历字符串
str_b = "hi-你好呀嘿嘿"
# while 循环遍历
# 表示从第一个元素开始遍历
index = 0
while index < len(str_b):
    print(f"第 {(index + 1)} 个元素是-> {str_b[index]}")
    # 循环控制遍历增1
    index += 1

print("==============================")
# 上面的分隔符可以这样写
print("=" * 30)
#
# for 循环遍历
for ele in str_b:
    print(ele)