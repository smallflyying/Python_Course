# @Version  : 1.0
# @Author   : LiHongFei
# @File     : lhf_module1.py
# @Time     : 2024/9/28 11:18

# 在lhf_module1.py 中，没有 __all__时，会导入所有的功能
# 使用了__all__ = ['ok'] 在其它文件使用 from lhf_module1 import * 只会导入 ok()
# 注意：import 模块 方式，不受 __all__ 的限制

# 表示如果其它文件使用的是 from lhf_module1 import * 导入，则只能导入ok函数
# __all__ = ['ok', 'hi']
__all__ = ['ok']

def hi():
    print("lhf hi")


def ok():
    print("lhf ok")


# 有时我们在模块中，会写一下测试代码
if __name__ == "__main__":
    hi()

# print("lhf_module1.py:", __name__)
