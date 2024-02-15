# -*- coding: utf-8 -*-
# @Time : 2024/1/15 11:55
# @Author : X_LY。
# @Title : 04_Sequence_in_Python.py
# @Description : Python中序列的切片操作

"""
    什么是序列的切片？
        切片：从一个序列中，取出一个子序列

    语法：
        序列[起始下标:结束下标:步长]
            表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列：
            • 起始下标表示从何处开始，可以留空，留空视作从头开始
            • 结束下标（不含）表示何处结束，可以留空，留空视作截取到结尾
            • 步长表示，依次取元素的间隔
            • 步长1表示，一个个取元素
            • 步长2表示，每次跳过1个元素取步长N表示，每次跳过N-1个元素取
            • 步长为负数表示，反向取（注意，起始下标和结束下标也要反向标
"""

my_list = [1, 2, 3, 4, 5, 6]
result = my_list[::-1]
print(result)
