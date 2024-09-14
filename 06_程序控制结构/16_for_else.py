# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 16_for_else.py
# @Time     : 2024/9/14 23:58

# for-else 使用案例
nums = [1, 2, 3]
for i in nums:
    print("你好，韩顺平教育", i)
    # 演示一把中断-break
    # if i == 2:
    #     break  # 中断-提前结束for循环
else:
    print("没有循环数据了...")
