# -*- coding: utf-8 -*-
# @Time : 2024/1/19 16:41
# @Author : X_LY。
# @Title : 02_Python中的封装.py
# @Description : Python中的封装

"""
    在Python中，封装指的是将 类中的属性和方法变为私有的成员和方法

    如何定义私有属性和方法？
        在属性和方法的名称前加两个下划线即可 __

    类对象无法访问私有属性和私有方法
    私有属性和私有方法的使用范围仅局限在 整个类中
"""

class Person():
    __name  = None
    def __init__(self):
        self.__name = "hahaha"

person1 = Person()
# 这样写会报错，提示该类中没有name属性
person1.name