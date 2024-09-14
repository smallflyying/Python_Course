# @Version  : 1.0
# @Author   : LiHongFei
# @File     : test.py
# @Time     : 2024/9/14 23:29

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums, id(nums), nums[0], id(nums[0]))
print(nums, id(nums), nums[1], id(nums[1]))
print(nums, id(nums), nums[2], id(nums[2]))

print(id(1))

nums2 = [1, 2]
print(nums2, id(nums2), nums2[0], id(nums2[0]))