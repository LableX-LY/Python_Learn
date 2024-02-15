# -*- coding: utf-8 -*-
# @Time : 2024/1/18 19:45
# @Author : X_LY。
# @Title : 01_Exception_in_Python.py
# @Description : Python中的异常机制

"""
    基本捕获语法
        try:
            ......
        except:
            ......

    捕获指定异常
        try:
            ......
        except NameError as e:
            print("出现变量未定义异常")

    捕获多个异常
        try:
            ......
        except (NameError, ZeroDivisionError) as e:
            ......

    捕获所有异常
        try:
            ......
        except Exception as e:
            ......

    完整的异常捕获语句为：
        try:
            ......
        except:
            ......
        else:       没有出现异常时需要执行的内容
            ......
        finally:    不论有没有异常出现都要执行的内容
            ......
"""