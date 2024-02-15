# -*- coding: utf-8 -*-
# @Time : 2024/1/18 14:50
# @Author : X_LY。
# @Title : 02_Type_of_Parameter.py
# @Description : Python函数中的参数类型

"""
    位置参数
        位置参数就是我们默认情况下使用的参数
"""

"""
    关键字参数
        函数调用时通过 键=值 的形式进行传参
    函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
"""
def function1 (name, age, height) :
    print(f"姓名是{name}, 年龄是{age}, 身高是{height}")

function1(name='X_LY', age=20, height=170)
function1(age=20, height=170, name='X_LY')

"""
    缺省参数（默认值）
        在定义函数的时候就为参数赋值（后续可覆盖）
    使用缺省参数时，缺省参数必须放在所有参数的最后面
"""
def function2 (name, age, height = 170) :
    print(f"姓名是{name}, 年龄是{age}, 身高是{height}")

function2(name='X_LY', age=20)
function2(name='X_LY', age=20, height = 175)

"""
    位置不定长参数，使用 *号
    即不确定要传入几个参数，使用不定长参数来接收
    不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
"""
def function3 (*args) :
    print("参数的内容是:%s" %args)

"""
    关键字不定长参数
    使用 **号
    传入的参数必须是 key = value 的形式
"""
def function4 (**kwargs) :
    print("参数的内容是:%s" %kwargs)