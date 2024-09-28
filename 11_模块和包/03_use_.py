# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 03_use_.py
# @Time     : 2024/9/28 11:51
from math import fabs

# 导入包下的模块
# import lhf_package.module01
# import lhf_package.module02


# 使用导入的模块
# lhf_package.module01.hi()
# lhf_package.module02.ok()


# from 包名 import 模块，这种方式导入，在使用时，模块.功能，不用带包名
# from lhf_package import module01

# 直接使用模块名.功能名
# module01.hi()


# 导入包的模块的指定函数、类、变量
# from lhf_package.module01 import hi

# 直接使用功能名调用即可
# hi()


# from 包名.模块 import * : 表示导入包的模块的所有功能
# from lhf_package.module01 import *
#
# hi()
# hello()


# __init__.py 通过 __all__ 控制允许导入的模块

# from lhf_package import *
#
# module02.ok()
# 引入限制了module01模块引入，因此不能使用
# module01.hi()


# __all__ = ['module02'] 不能限制 下面的导入形式
# import lhf_package.module02
# import lhf_package.module01
#
# lhf_package.module02.ok()
# lhf_package.module01.hi()


# 包可以有多个层级
# 使用方式1，看起来很麻烦，但是很好理解
# import lhf_package.lhf_package2.module03
#
# lhf_package.lhf_package2.module03.cal(60, 30)


# 使用方式2
# from lhf_package.lhf_package2.module03 import cal

# 直接调用即可
# cal(60, 90)


# 使用方式3
# from lhf_package.lhf_package2 import module03
# 使用模块名.功能名调用
# module03.cal(90, 10)

# from math import fabs

print(fabs(-90.8))





