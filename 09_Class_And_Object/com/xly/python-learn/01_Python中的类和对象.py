# -*- coding: utf-8 -*-
# @Time : 2024/1/19 15:04
# @Author : X_LY。
# @Title : 01_Python中的类和对象.py
# @Description : Python中的类和对象

"""
    Python中的构造方法
        __init__()

    Python中的toString()方法
        __str__
        但需要自己定义输出什么内容

    Python中的eq方法，类似于equals()方法
        一个类中如果实现了eq()方法，则两个对象进行 == 操作时就会按照实现的方法进行比较
        一个类中如果没有实现eq()方法，则两个对象进行 == 操作时一定是false，因为比较的是内存地址

    在Python中，成员方法的参数中都必须写上 self 参数
    访问类中的成员变量时，必须使用self. 的形式
"""

class Person(object):
    name = None
    age = None

    # 这里的self 优点类似于Java中的 this 的作用，访问类中的成员变量时，必须使用self. 的形式
    # 传参时不用传self
    def hello(self):
        print(f"Hello,everybody,I'am {self.name}")

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __eq__(self, other):
        return self.age == other.age

XLY = Person()
XLY.name = "XLY"
XLY.age = 22

XLY.hello()

xly = Person()
xly.name = "XLY"
xly.age = 23

print(XLY == xly)

