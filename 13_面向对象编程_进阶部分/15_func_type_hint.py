# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 15_func_type_hint.py
# @Time     : 2024/10/11 23:03


# 演示函数(方法)的类型注解


# 对字符串进行遍历
"""
    解读
    1. name: str 对形参name进行类型注解：标注name类型是str
    2. 在调用方法/函数时，传入的实参类型不是一样的，则会给出黄色的警告
"""


def fun1(name: str):
    for ele in name:
        print(ele)


# TypeError: 'int' object is not iterable
# fun1(100)
fun1("你好呀")


# 接收两个整数，返回整数
"""
    分析
    1. a: int, b: int : 对形参a，和b进行类型注解，，标注a，b的类型为int
    2. -> int 对返回值进行类型注解，标注返回值的类型为int
"""


def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果是: {fun2(10.1, 20)}")
