# -*- coding: utf-8 -*-
# @Time : 2024/1/18 15:23
# @Author : X_LY。
# @Title : 03_Lambda_Function.py
# @Description : Python中的lambda匿名函数

"""
    函数的定义中
        def关键字，可以定义带有名称的函数
        lambda关键字，可以定义匿名函数（无名称）

        有名称的函数，可以基于名称重复使用。
        无名称的匿名函数，只可以使用一次。(不可重复使用)

    匿名函数的定义语法
        lambda 传入参数 : 函数体(只能写一行代码)
"""
def lambda_func(add):
    result = add(1, 2)
    print("运算结果是%d" % result)

lambda_func(lambda x, y :x + y)
