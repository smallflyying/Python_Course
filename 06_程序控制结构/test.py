# @Version  : 1.0
# @Author   : LiHongFei
# @File     : test.py
# @Time     : 2024/9/14 23:29

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(nums, id(nums), nums[0], id(nums[0]))
# print(nums, id(nums), nums[1], id(nums[1]))
# print(nums, id(nums), nums[2], id(nums[2]))
#
# print(id(1))
#
# nums2 = [1, 2]
# print(nums2, id(nums2), nums2[0], id(nums2[0]))


# 演示random.randint() 的使用
# 导入random模块
# import random
#
# # 1<=n<=100
# for i in range(8):
#     n = random.randint(1, 100)
#     print("n = ", n)

n = 90
if n > 300:
    print("n > 300")
elif n > 200:
    print("n > 200")
elif n > 100:
    print("n > 100")
# else:
#     print("不满足上述条件")
