# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 16_union_type_hint.py
# @Time     : 2024/10/11 23:16
# 如果要是有Union类型注解,则需要导入Union
from typing import Union

# 联合类型注解，a 可以是int 或者 str
a: Union[int, str, float] = 1.2

# my_list是list类型，元素可以是int 或者str
my_list: list[Union[int, str]] = [100, 200, 300, "tom"]


# 函数/方法使用联合类型注解
# 接收两个数(可以是int/float),返回数(int/float)
def cal(num1: Union[int, float],
        num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


# TypeError: can only concatenate str (not "float") to str
# print(f"结果是: {cal("10", 20.2)}")
print(f"结果是: {cal(10, 20.2)}")
