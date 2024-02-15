# -*- coding: utf-8 -*-
# @Time : 2024/1/19 16:54
# @Author : X_LY。
# @Title : 03_Python中的继承.py
# @Description : Python中的继承

"""
    Python中的继承分为单继承和多继承(Java是单继承，一个类只能同时继承一个类)

    在多继承中，如果要使用的变量或者方法在多个类中同时存在，即重名了，那么依照“先继承先使用”的原则，使用先继承的那个(从左向右)

    在多继承中，关键字pass的作用是“占位”
        即“继承了某个类，但自己没有其他的属性与方法，只是使用父类的属性与方法。但语法层面有不允许什么都不写，这时就可以写pass来占位“

    Python中的继承同样支持方法重写

    子类调用父类的方法可以使用super()方法，也可以直接使用 父类名.方法名 的方式调用
"""


# 单继承
class Phone:
    IMEI = None
    producer = None

    def call_by_4g(self):
        print("使用4g网络进行通话")


class Phone2(Phone):
    def call_by_5g(self):
        print("使用5g网络进行通话")

phone_5g = Phone2()
phone_5g.call_by_4g()

# 多继承

class Iphone:
    def info(self):
        print("我是Iphone")
class Phone3(Phone, Iphone):
    print("我使用了多继承，即同时继承多个类")
