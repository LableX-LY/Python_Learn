# -*- coding: utf-8 -*-
# @Time : 2024/1/11 21:47
# @Author : X_LY。
# @Title : 10_Input_in_Python.py
# @Description :

"""
数据类型转换，将会是我们以后经常使用的功能。
如：
• 从文件中读取的数字，默认是字符串，我们需要转换成数字类型
• 后续学习的input（）语句，默认结果是字符串，若需要数字也需要转换
• 将数字转换成字符串用以写出到外部系统
• 等等
"""

# 将数字类型转换为字符串
num_str = str(11)
print(type(num_str))

num_str2 = str(13.14)
print(type(num_str2))

# 将字符串转换为数字类型
num_str3 = int("1234")
print(type(num_str3))

num_str4 = int("13.14")
print(type(num_str4))

# 错误示例
# num_str = int("哈哈哈哈")
# print(type(num_str))

# 整数转换为浮点数
num1 = float(11)
print(type(num1))

# 浮点数转换为整数
# 整数转换为浮点数时会丢失一定的精度
num2 = int(13.14)
print(type(num2))
