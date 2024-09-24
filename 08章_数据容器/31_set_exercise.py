# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 31_set_exercise.py
# @Time     : 2024/9/24 22:30


# 1、用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)，
# s_history = {'小明', "张三", '李四', "王五", 'Lily', "Bob"}
# s_politic = {'小明', "小花", '小红', "二狗"}
# s_english = {'小明', 'Lily', "Bob", "Davil", "李四"}
#
# - 求选课学生总共有多少人
# - 求只选了第一个学科(history)的学生数量和学生名字
# - 求只选了一门学科的学生数量和学生名字
# - 求算了三门学科的学生数量和学生名字


# 定义3个集合
s_history = {'小明', "张三", '李四', "王五", 'Lily', "Bob"}
s_politic = {'小明', "小花", '小红', "二狗"}
s_english = {'小明', 'Lily', "Bob", "Davil", "李四"}

# - 求选课学生总共有多少人
"""
    思路分析
    1. 对三个集合求并集 【自动去重】
    2. 对新的集合求len()
"""
print(f"求选课学生总共有 {len(s_history | s_politic | s_english)} 人")
# print(f"求选课学生总共有 {len(s_history.union(s_politic).union(s_english))} 人")


# - 求只选了第一个学科(history)的学生数量和学生名字
"""
    思路分析
    1. 即求出只在s_history学员
    2. 使用差集即可 s_history - s_politic - s_english
"""
print(f"求只选了第一个学科(history)的学生数量 {len(s_history.difference(s_politic).difference(s_english))} 和学生名字 {s_history.difference(s_politic).difference(s_english)}")
# print(f"求只选了第一个学科(history)的学生数量 {len(s_history - s_politic - s_english)} 和学生名字 {s_history - s_politic - s_english}")


# - 求只选了一门学科的学生数量和学生名字
"""
    思路分析
    1. 求出只选择了s_history的学生
    2. 求出只选择了s_politic的学生
    3. 求出只选择了s_english的学生
    4. 然后求并集集合
"""
# 1. 求出只选择了s_history的学生
s1 = s_history.difference(s_politic).difference(s_english)
# 方式二
# s1 = s_history - s_politic - s_english
# 2. 求出只选择了s_politic的学生
s2 = s_politic.difference(s_history).difference(s_english)
# 方式二
# s2 = s_politic - s_history - s_english
# 3. 求出只选择了s_english的学生
s3 = s_english.difference(s_history).difference(s_politic)
# 方式二
# s3 = s_english - s_history - s_politic

print(f"求只选了一门学科的学生数量 {len(s1.union(s2).union(s3))} 和学生姓名 {s1.union(s2).union(s3)}")
# print(f"求只选了一门学科的学生数量 {len(s1 | s2 | s3)} 和学生姓名 {s1 | s2 | s3}")

# - 求算了三门学科的学生数量和学生名字
"""
    思路分析：
    1. 求出既在 s_politic 又在 s_history 还在 s_english中
    2. 就是对三个集合求交集
"""
print(f"求算了三门学科的学生数量为 {len(s_history.intersection(s_politic).intersection(s_english))} 和学生名字为 {s_history.intersection(s_politic).intersection(s_english)}")
# 方式二
# print(f"求算了三门学科的学生数量为 {len(s_history & s_politic & s_english)} 和学生名字为 {s_history & s_politic & s_english}")