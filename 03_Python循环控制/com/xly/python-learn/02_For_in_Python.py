# -*- coding: utf-8 -*-
# @Time : 2024/1/12 15:22
# @Author : X_LY。
# @Title : 02_For_in_Python.py
# @Description : Python中的for循环

"""
    for循环的语法格式是
        for 临时变量 in 待处理数据集
            要执行的代码
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in arr:
    print(i)


"""
    range语句，可以获得一个简单的数字序列
    
        语法一：
            range(num),获取一个从0开始，到num结束的数字序列（不包括num本身）
            range(5)则得到：[0，1，2，3，4]
            
        语法二：
            range(num1,num2),获取一个从num1开始，到num2结束的数字序列（不包括num2本身）
            range(5,10)则得到：[5,6,7,8,9]
            
        语法三：
            range(num1,num2,step)，获取一个从num1开始，到num2结束的数字序列（不包括num2本身）
            数字之间的步长由step来决定，如不设置，则step默认为1
            range(5,10,2)则得到：[5,7,9]
"""

"""
    continue
        结束本次循环，直接进入到下一次循环
    break
        直接结束循环，不论循环条件怎样，直接退出循环，不再进行循环
"""
