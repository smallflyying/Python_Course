# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 03_exceptions_example.py
# @Time     : 2024/10/18 22:37


# 1、IndexError: 当序列抽取超出范围时将被引发
# str = "hello,abc"  # 9
# print(str[100])

# list_a = ["jack", "tom", "yoyo", "nono", "lhf"]
# # print(list_a[5])

# 2、KeyError: 当在现有键集合中找不到指定的映射(字典) 键时将被引发
# dict_a = {"name": "jack", "age": 10, "gender": "男"}
# print(dict_a["sex"])

# 3、NameError：当某个局部或全局名称未找到时将被引发，比如你使用了一个没有定义的变量名
# print("nums is:", nums)

# 4、TypeError：当一个操作或函数使用了类型不适当的对象时将被引发
# a = "hello"
# b = 5
# # TypeError: can only concatenate str (not "int") to str
# print(a + b)

# 5、ValueError：当操作或函数接收到具有正确类型但值不适合的参数时将引发
# print(int("123"))  # 123
# ValueError: invalid literal for int() with base 10: 'abc'
# print(int("abc"))  # 抛出/触发/引发异常

# 6、ZeroDivisionError: 当除法或取余运算的第二个参数为零时将被引发
# ZeroDivisionError: division by zero
# print(1 / 0)

# 7、FileNotFoundError: 请求的文件或目录不存在时将被引发
# FileNotFoundError: [Errno 2] No such file or directory: 'd://ttt/t.txt'
# f = open("d://ttt/t.txt", "r")

# 8、AttributeError: 当属性引用或赋值失败时将被引发
class A:
    def hi(self):
        pass

# AttributeError: 'A' object has no attribute 'name'
a = A()
print(a.name)

