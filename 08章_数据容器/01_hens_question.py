# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 01_hens_question.py
# @Time     : 2024/9/20 21:42


"""
    思路： 定义 6 个变量，加起来 总体重
"""

# 代码实现
# hen1 = 3
# hen2 = 5
# hen3 = 1
# hen4 = 3.4
# hen5 = 2
# hen6 = 50
# # 计算总的体重
# total_weight = hen1 + hen2 + hen3 + hen4 + hen5 + hen6
# # 计算平均体重
# avg_weight = total_weight / 6
# # 方式一 round()
# print(f"总体重: {total_weight} 平均体重: {round(avg_weight, 2)}")
# 方式二 格式化字符串
# print(f"总体重: {total_weight} 平均体重: {avg_weight:.2f}")

# print(round(34.678, 1))

# 问题分析
# 1. 如果不是 6 只鸡而是600只鸡怎么办？
# 2. 不利于代码的维护，不灵活
# 3. 引出->列表知识点


# 使用列表解决养鸡场问题
hens = [3, 5, 1, 3.4, 2, 50]
# 计算总的体重
total_weight = 0.0
# 遍历 hens
for element in hens:
    # 累加
    total_weight += element

print(f"总体重: {total_weight} 平均体重: {round(total_weight / len(hens), 2)}")