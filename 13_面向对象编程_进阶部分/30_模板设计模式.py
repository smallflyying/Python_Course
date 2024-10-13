# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 30_模板设计模式.py
# @Time     : 2024/10/13 14:34


"""
1）有多个类，完成不同的任务job
2）要求统计得到各自完成任务的时间
3）请编程实现  传统方式实现
"""
import time


class AA:
    def job(self):
        # 得到开始的时间，秒数
        start = time.time()
        num = 0
        for i in range(1, 800001):
            num += i
        # 得到结束的时间，秒数
        end = time.time()
        print("计算任务 执行时间(秒):", (end - start))


class BB:
    def job(self):
        # 得到开始的时间，秒数
        start = time.time()
        num = 1
        for i in range(1, 90001):
            num -= i
        # 得到结束的时间，秒数
        end = time.time()
        print("计算任务 执行时间:", (end - start))


# 测试
if __name__ == '__main__':
    a = AA()
    a.job()
    b = BB()
    b.job()
