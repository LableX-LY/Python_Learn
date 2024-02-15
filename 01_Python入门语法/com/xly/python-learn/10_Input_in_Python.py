# -*- coding: utf-8 -*-
# @Time : 2024/1/11 21:47
# @Author : X_LY。
# @Title : 10_Input_in_Python.py
# @Description :

"""
    与 print()方法相对应的是 input()方法，接收用户从键盘输入的信息
    不过，不论用户输入的内容是什么，input()方法都会把内容转换为字符串
"""
print("Please enter you name")
name = input()
print("The type of your input is", type(name))
print("Please enter your age")
age = input()
