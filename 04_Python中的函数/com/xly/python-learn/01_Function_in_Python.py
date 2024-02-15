# -*- coding: utf-8 -*-
# @Time : 2024/1/12 16:05
# @Author : X_LY。
# @Title : 01_Function_in_Python.py
# @Description : Python中的函数

# 函数：即组织好的，可重复使用的，用来实现特定功能的代码段

# 计算字符串的长度，不使用内置的len()函数
str = "XLY"
count = 0
for i in str:
    count += 1
print("str的长度是：%d" % count)

# 使用自定义函数
def my_len(data):
    """
    自定义的计算字符串长度的函数
    :param data:
    :return:
    """
    count = 0
    for i in data:
        count += 1
    print("传入的数据的长度是：%d" % count)

my_len("X_LY。")
