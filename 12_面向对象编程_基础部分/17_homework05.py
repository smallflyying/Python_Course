# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 17_homework05.py
# @Time     : 2024/10/7 21:04


# 5、定义Music类，里面有音乐名name、音乐时长times属性，并有播放play功能，和返回本身属性信息的方法get_info

"""
    思路分析：
    1. 类名：Music
    2. 属性：name, times
    3. 构造器: __init__(self, name, times)
    4. 方法：play(self), get_info(self)
"""


class Music:
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print(f"音乐名 {self.name} 正在播放中... 时长为{self.times}")

    def get_info(self):
        return f"音乐的信息为 name: {self.name} times: {self.times}"


# 测试
music = Music("月光曲", "300")
music.play()
print(music.get_info())

# 自己写的
# class Music:
#     name = None
#     times = None
#
#     def __init__(self, name, times):
#         self.name = name
#         self.times = times
#
#     def play(self):
#         print("正在播放:", self.name)
#
#     def get_info(self):
#         return "音乐名:" + self.name + " 音乐时长:" + str(self.times)
#
#
# # 测试
# music = Music("Hello", "4:30")
# music.play()
# print(music.get_info())
