# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 33_dict_detail.py
# @Time     : 2024/9/24 23:26


# 1、字典的Key(关键字)通常是字符串或数字，Value可以是任意数据类型

dict_a = {
    "jack": [100, 200, 300],
    "mary": (10, 20, "hello"),
    "nono": {"apple", "pear"},
    "smith": "计算机老师",
    "周星驰": {
        "性别": "男",
        "age": 18,
        "地址": "香港"
    },
    "key1": 100,
    "key2": 9.8,
    "key3": True,
    123: "key4",
    ("sss", "sss"): "key5",
    # ["sss", "sss"]: "key6"  # TypeError: unhashable type: 'list'
    # {"sss", "sss"}: "key5"  # TypeError: unhashable type: 'set'

}
print(f"dict_a: {dict_a} 类型: {type(dict_a)}")
