# @Version  : 1.0
# @Author   : LiHongFei
# @File     : lingxing_01.py
# @Time     : 2024/9/15 21:21

#

"""
    思路分析：
    - 先死后活
    1. 先不考虑层数的变化，假定就是9层，后面做活
    - 化繁为简
    1. 打印矩形
    2. 打印上下两个直角三角形
    3. 打印实心菱形
    4. 打印空心菱形
"""

"""
    * -> *********
    1. 打印矩形
    *********
    *********
    *********
    *********
    *********
    *********
    *********
    *********
    *********
    2. 打印上下两个直角三角形
    上三角形如下：
    *           1层: 1个*
    ***         2层: 3个*
    *****       3层: 5个*
    *******     4层: 7个*
    *********   5层: 9个*
    下三角形如下：
    *******     1层: 7个*
    *****       2层: 5个*
    ***         3层: 3个*
    *           4层: 1个*
    3. 打印实心菱形
    上实心三角形如下(5层)：
        *         1层: 1个*  2*1-1  空格 4  5-1
       ***        2层: 3个*  2*2-1  空格 3  5-2
      *****       3层: 5个*  2*3-1  空格 2  5-3
     *******      4层: 7个*  2*4-1  空格 1  5-4
    *********     5层: 9个*  2*5-1  空格 0  5-5
    下实心三角形如下(4层)：
     *******      1层: 7个*  2*4-1  空格 1  1
      *****       2层: 5个*  2*3-1  空格 2  2 
       ***        3层: 3个*  2*2-1  空格 3  3
        *         4层: 1个*  2*2-1  空格 4  4
    4. 打印空心金字塔
        *        分析: 每层的两边输出*
       * *         
      *   *        
     *     *       
    *       *
     *     *
      *   * 
       * *  
        *     
"""

# 方式一: for循环
# for i in range(1, 6):
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * (i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")
# for i in range(1, 5):
#     for k in range(i):
#         print(" ", end="")
#     # j 范围 0 - 2*（5-i) + 1 - 1
#     for j in range(2*(4-i) + 1):
#         # print("*", end="")
#         if j == 0 or j == 2*(4-i):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

# 方式二: while循环
i = 1
while i <= 5:
    k = 0
    while k < 5 - i:
        print(" ", end="")
        k += 1
    j = 0
    while j < 2 * i - 1:
        if j == 0 or j == 2 * (i - 1):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1
i = 1
while i <= 4:
    k = 0
    while k < i:
        print(" ", end="")
        k += 1
    # j 范围 0 - 2*（5-i) + 1 - 1
    j = 0
    while j < 2*(4-i) + 1:
        # print("*", end="")
        if j == 0 or j == 2*(4-i):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1