# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 19_homework07.py
# @Time     : 2024/10/7 22:21


# 7、思考题
# 1）有个人Tom 设计他的成员变量，成员方法，可以进行电脑猜拳，电脑每次都会随机生成 0，1，2
# 2）0 表示石头 1 表示剪刀 2 表示布
# 3）并要可以显示 Tom 的输赢次数(清单)

import random


class Tom:
    win_times = 0
    lose_times = 0

    def __init__(self):
        pass

    # 2）0 表示石头 1 表示剪刀 2 表示布
    def play(self, tom_input):
        computer_num = random.randint(0, 2)
        if tom_input == computer_num:
            print("平局")
        elif ((tom_input == 0 and computer_num == 1)
              or (tom_input == 1 and computer_num == 2)
              or (tom_input == 2 and computer_num == 0)):
            print("tom 赢了")
            self.win_times += 1
        else:
            print("电脑赢了")
            self.lose_times += 1

    # 3）并要可以显示 Tom 的输赢次数(清单)
    def show_info(self):
        print(f"Tom 赢了 {self.win_times} 次，输了 {self.lose_times} 次")


tom = Tom()
# 模拟几轮游戏
competition_rounds = 3
for i in range(competition_rounds):
    print(f"第 {i + 1} 轮")
    tom_input = int(input("请输入 0 (石头), 1 (剪刀), 2 (布)："))
    tom.play(tom_input)
# 显示 Tom 的输赢次数(清单)
tom.show_info()
