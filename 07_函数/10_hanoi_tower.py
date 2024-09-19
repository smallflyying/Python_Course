# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 10_hanoi_tower.py
# @Time     : 2024/9/19 22:08


# https://www.novelgames.com/zh/tower/
def hanoi_tower(num, a, b, c):
    """
    输出指定的num个盘子移动的顺序
    @param num: 指定盘子数
    @param a: 表示A柱子
    @param b: 表示B柱子
    @param c: 表示C柱子
    @return:
    """
    if num == 1:
        print(f"第1个盘从: ", a, "->",  c)
    else:
        # 有多个盘，我们认为只有两个，上面所有的盘和最下面的盘
        # 移动上面所有的盘到B柱子，这个过程会借助到C柱子
        hanoi_tower(num - 1, a, c, b)
        # 移动最下面的盘
        print(f"第{num}个盘从:  {a} -> {c}")
        # 把上面所有的盘从B柱子移动到C柱子，这个过程会使用到A柱子
        hanoi_tower(num - 1, b, a, c)


# 测试一把
hanoi_tower(5, "A", "B", "C")