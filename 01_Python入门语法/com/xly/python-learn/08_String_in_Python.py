# -*- coding: utf-8 -*-
# @Time : 2024/1/11 20:34
# @Author : X_LY。
# @Title : 08_String_in_Python.py
# @Description : Python中有关字符串的拓展

# 1.单引号定义法
print('Hello World!')

# 2.双引号定义法
print("Hello World!")

# 3.三引号定义法，支持换行
print("""Hello World!""")
name = """
    X
    L
    Y
"""
print(name)

"""
单引号定义法，可以内含双引号

双引号定义法，可以内含单引号

可以使用转义字符 \ 对引号进行转义，使其变成普通的内容
"""
print("\"Hello World!\"")
# 此时输出的内容为 "Hello World!"

