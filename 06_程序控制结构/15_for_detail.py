# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 15_for_detail.py
# @Time     : 2024/9/14 23:42

# 1. 虽然被称为函数，但range 实际上是一个不可变的序列类型
# 2. range 默认增加的步长step 是1，也可以指定，start 默认是0
# 2. 通过list() 可以查看range() 生成的序列包含的数据
# 3. range() 生成的数列是 前闭后开 range(1,5) => 1,2,3,4

# 1. 需求: 生成一个 [1,2,3,4,5]

# r1 = range(1, 6, 1)
r1 = range(1, 6)
print("r1 = ", list(r1))

# 2. 需求: 生成一个 [0,1,2,3,4,5]
# r2 = range(0, 6, 1)
r2 = range(6)
print("r2 = ", list(r2))

# 3. 需求: 生成一个 [1,3,5,7,9]
r3 = range(1, 10, 2)
print("r3 = ", list(r3))

# 4. 需求 使用for+range 方式输出10句 "hello, python"

for i in range(10):
    print("hello, python", i)
