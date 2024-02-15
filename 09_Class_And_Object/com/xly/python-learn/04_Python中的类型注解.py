# -*- coding: utf-8 -*-
# @Time : 2024/1/19 19:14
# @Author : X_LY。
# @Title : 04_Python中的类型注解.py
# @Description : Python中的类型注解

"""
     Python中的类型注解类似于Java中的 泛型？或者类似TypeScript中的强制类型语法？

     实际上类型注解只起到一种提示作用，代码执行时会按照程序员写好的给定值执行，而不是按照注解的类型
     比如：
        var: int = "Hello World!"
        这个写法把变量var标记为int类型，但实际上赋值时却赋的是字符串类型
        虽然逻辑上有问题，但代码真正执行时并不会报错，程序会把"Hello World!"赋给var
"""

# 1.基础数据类型注解
var1: int = 10
var2: str = "Hello"
var3: bool = True


# 2.类对象类型注解
class Person:
    pass


XLY: Person = Person()

# 3.基础容器类型注解
list1: list[int] = [10, 2, 3, 4]
tuple1: tuple = (10, 2, 3, 4)
dict1: dict = {"name": "XLY"}

# 4.容器类型详细注解
list1: list[int] = [10, 2, 3, 4]
tuple1: tuple[int, str, bool] = (10, XLY, True)
dict1: dict[str, str] = {"name": "XLY"}

# 5.在注释中进行类型注释
var11 = 10  # type: int


# 6.对函数的返回值进行类型注解
def haha(data: int) -> list:
    return data


"""
    Union联合类型注解
"""
# 使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str]] = [10, 2, "as", "XLY"]

def func(data: Union[int, str]) -> Union[int, str]:
    return data