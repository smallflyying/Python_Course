# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 35_return_use.py
# @Time     : 2024/9/16 21:14

# 观察下面的代码: 分析输出的结果是什么?

def f1():
    for i in range(1, 5):
        if i == 3:
            # return 就是跳出函数
            # return
            # break
            continue
        print("i = ", i)
    print("结束了for...")


# 调用f1函数-> 执行f1函数
f1()

# return 的用法
# i =  1
# i =  2

# break 的用法
# i = 1
# i = 2
# 结束了for...

# continue 的用法
# i = 1
# i = 2
# i = 4
# 结束了for...
