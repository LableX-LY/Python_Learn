# -*- coding: utf-8 -*-
# @Time : 2024/1/11 20:09
# @Author : X_LY。
# @Title : 06_Identifier_in_Python.py
# @Description : Python中的命名规则语法

"""
变量的命名规范
    1.见名知意
    2.下划线命名法
    3.英文字母全小写
"""

# 规则1：内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能以数字开头
# 错误的代码示范：1_name =“张三”
# 错误的代码示范：name_！=“张二”
name_ = "张三"
_name = "张三"
name_1 = "张三"

# 规则2:大小写敏感
age = 23
print(age)
Age = 24
print(Age)

# 规则3:不能使用内置的关键字
