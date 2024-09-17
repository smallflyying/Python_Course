# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 04_function_detail.py
# @Time     : 2024/9/17 22:27


# 3、函数中的变量是局部的，函数外不生效
# def hi():
#     n = 10
#     print("n : ", n)
#
#
# hi()
# # 函数内部定义的n，在函数外部不能使用
# print("n : ", n)


# 4、如果同一个文件，出现两个函数名相同的函数，则以就近原则进行调用

# def cry():
#     print("cry()..hi...")
#
# # cry(10)
#
# def cry():
#     print("cry()..ok...")
#
#
# # 这个 cry 会默认就近原则，即第二个 cry()
# cry()


# 5、调用函数时，根据函数定义的参数位置来传递参数，这种传参方式就是位置参数，
# 传递的实参和定义的形参顺序和个数必须一致
# 同时定义的形参，不需要指定数据类型，会根据传入的实参决定

# def car_info(name, price, color):
#     print(f"name->{name} price->{price} color->{color}")
#
#
# # 传递的实参和定义的形参顺序和个数必须一致，否则报 TypeError 错误
# # car_info("宝马", 500000, "red")
# car_info("宝马", 500000, "red", 11)


# 6、函数可以有多个返回值
# 比如函数接收两个数，返回这两个数的和、差
# def f2(n1, n2):
#     return n1 + n2, n1 - n2
#
#
# r1, r2 = f2(10, 20)
# print(f"r1->{r1} r2->{r2}")


# 7、函数支持关键字参数，即：函数调用时，可以通过“形参名=实参值” 形式传递参数，
# 这样可以不受参数传递顺序的限制

# def book_info(name, price, author, amount):
#     print(f"name->{name} price->{price} author->{author} amount->{amount}")
#
#
# # 通常调用方式，一一对应
# book_info("红楼梦", 60, "曹雪芹", 30000)
# # book_info("红楼梦", 60, 30000, "曹雪芹")
#
#
# # 关键字参数
# print("--------------关键字参数---------------")
# book_info(name="红楼梦", price=60, amount=30000, author="曹雪芹")
# book_info("红楼梦", 60, amount=30000, author="曹雪芹")



# 8、函数支持默认参数/缺省参数
# - 定义函数时，可以给参数提供默认值，调用函数时，制定了实参，则以指定为准，没有指定，则以默认值weizhun
# - 默认参数，需要放在参数列表后
def book_info2(name='<<thinking in python>>', price=66.8, author='龟叔', amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 调用测试
book_info2()
# book_info2('<<study python>>')