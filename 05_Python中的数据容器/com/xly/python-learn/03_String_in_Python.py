# -*- coding: utf-8 -*-
# @Time : 2024/1/15 11:10
# @Author : X_LY。
# @Title : 03_String_in_Python.py
# @Description : String"字符容器"

"""
    字符串是“字符”的容器，一个字符串可以存放任意数量的字符

    字符串同样支持下标访问
        从前向后，下标从0开始
        从后向前，下标从1开始

    字符串和元组一样，不支持修改内容
"""

str = "  I am learning Python    "

# index方法,返回某个内容的起始下标
print(str.index("learning"))

# replace()方法，替换字符串中的某个内容，“得到一个新的字符串”
str.replace("Python", "Java")

# spilt()方法，字符串的分割，按照指定的字符分割字符串，并存入列表对象中，字符串本身不变

# strip()方法，字符串的规整操作
# 去除字符串前、后的空格
print(str.strip())
# 去除指定的内容
print(str.strip("I"))

