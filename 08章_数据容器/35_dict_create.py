# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 35_dict_create.py
# @Time     : 2024/9/25 22:35


books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book = {book: author for book, author in zip(books, authors)}
print("dict_book:", dict_book)  # {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}


# 思考
str1 = "你好呀"
dict_str1 = {ele1: ele2*2 for ele1, ele2 in zip(str1, str1)}
print("dict_str1:", dict_str1)  # {'你': '你你', '好': '好好', '呀': '呀呀'}


# 举例
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]

dict_color = {ch: en.upper() for ch, en in zip(chinese_list, english_list)}
print("dict_color:", dict_color)  # {'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}

# 生成一个字典：
# {'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}