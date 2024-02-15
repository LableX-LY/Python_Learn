# -*- coding: utf-8 -*-
# @Time : 2024/1/15 17:22
# @Author : X_LY。
# @Title : 01_Return_Progression.py
# @Description : Python中函数的进阶操作

"""
    return 返回多个返回值
        按照返回值的顺序，写对应顺序的多个变量接收即可
        变量之间用逗号隔开
        支持不同类型的数据return
"""
def test():
    return 1, 2

result1, result2 = test()
print(result1)
print(result2)
