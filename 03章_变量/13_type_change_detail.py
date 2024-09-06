# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 13_type_change_detail.py
# @Time     : 2024/9/6 22:44

# 显式类型转换注意事项

# 不管什么值的int,float都可以转成str, str(x) 将对象 x 转换为字符串
n1 = 100
n2 = 123.65
print(str(n1))
print(str(n2))

# int 转成 float时, 会增加小数部分, 比如 100->100.0 ,
# float 转成 int时, 会去掉小数部分  比如 123.65->123

print(float(n1))  # 100.0
print(int(n2))   # 123

# str转int,float 使用 int(x) , float(x) 将对象 x 转换为 int/float

n3 = "12.3"
print(float(n3))  # 12.3
# print(int(n3))  # ValueError: invalid literal for int() with base 10: '12.3'

# 在将str 类型转成基本数据类型时，要确保str值能够转成有效的数据, 比如 我们可以把"123" ,
# 转成一个整数, 但是不能把"hello" 转成一个整数, 如果格式不正确, 程序会报 ValueError, 程序就会终止
n4 = "hello"
# print(float(n4)) # ValueError: could not convert string to float: 'hello'
# print(int(n4)) # ValueError: invalid literal for int() with base 10: 'hello'


i = 10
j = float(i)
print("i的值:", i, "i的类型:", type(i))  # 10, int
print("j的值:", j, "j的类型:", type(j))  # 10.0, float

k = str(i)
print("i的值:", i, "i的类型:", type(i))  # 10, int
print("k的值:", k, "k的类型:", type(k))  # "10", int