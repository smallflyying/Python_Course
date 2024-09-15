# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 26_stars.py
# @Time     : 2024/9/15 11:26

# 请编写一个程序，可以接收一个整数，表示层数(total_level)，打印出空心金字塔

"""
    思路分析：
    - 先死后活
    1. 先不考虑层数的变化，假定就是5层，后面做活
    - 化繁为简
    1. 打印矩形
    2. 打印直角三角形
    3. 打印金字塔
    4. 打印空心金字塔
"""

"""
    * -> *****
    1. 打印矩形
    *****
    *****
    *****
    *****
    *****
    2. 打印直角三角形
    *      1层: 1个*
    **     2层: 2个*
    ***    3层: 3个*
    ****   4层: 4个*
    *****  5层: ...
    3. 打印金字塔
        *         1层: 1个*  2*1-1  空格 4  5-1
       ***        2层: 3个*  2*2-1  空格 3  5-2
      *****       3层: 5个*  2*3-1  空格 2  5-3
     *******      4层: 7个*  2*4-1  空格 1  5-4
    *********     5层: 9个*  2*5-1  空格 0  5-5
    4. 打印空心金字塔
        *        分析: 每层的两边输出* 和最后一层输出* 
       * *         
      *   *        
     *     *       
    *********      
"""

# 总层数
total_level = 5

# i 控制层数
# range(1, 6) 表示从1开始，到6结束，不包含6
for i in range(1, total_level + 1):
    # k: 控制输出空格数
    for k in range(total_level - i):
        print(" ", end="")
    # j 控制每层输出的*号个数
    for j in range(2 * i - 1):
        # 这里end=""，表示输出不换行
        if j == 0 or j == 2 * (i - 1) or i == total_level:
            print("*", end="")
        else:
            print(" ", end="")
    # 每层输出后，换行
    print("")
