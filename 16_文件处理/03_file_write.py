# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 03_file_write.py
# @Time     : 2024/10/20 12:43


# - 需求：
# 1）在d盘的 a 目录下创建 abc.txt 文件，并写入10句 "hello, 你好呀" 到我呢见
# 2）将abc.txt 内容覆盖成新的内容10句 "hi, 哈哈"
# 3）在abc.txt 原有内容基础上追加10句 "你好!python"


"""
    说明细节：
    1. mode = "w" 打开文件，如果文件不存在，会创建，如果文件已经存在，
        会先截断打开的文件，也就是清空文件内容
    2. 如果我们希望以追加的方式写入，需要 mode = "a"
"""
# w 模式打开文件，文件阶段原来的内容
# f = open("d://a//abc.txt", "w", encoding="utf-8")
# a 模式打开文件，是在原来的基础上追加内容
f = open("d://a//abc.txt", "a", encoding="utf-8")

# 1）在d盘的 a 目录下创建 abc.txt 文件，并写入10句 "hello, 你好呀" 到我呢见
# i = 1
# while i <= 10:
#     f.write(f"hello, 你好呀~\n")
#     i += 1
#
# f.close()

# 2）将abc.txt 内容覆盖成新的内容10句 "hi, 哈哈"
# i = 1
# while i <= 10:
#     f.write(f"hi, 哈哈~\n")
#     i += 1
# f.close()

# 3）在abc.txt 原有内容基础上追加10句 "你好!python", mode 指定为 "a" 追加模式即可
i = 1
while i <= 10:
    f.write(f"你好!python~\n")
    i += 1
f.close()

