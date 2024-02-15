# -*- coding: utf-8 -*-
# @Time : 2024/1/12 11:55
# @Author : X_LY。
# @Title : 01_While_in_Python.py
# @Description : Python中的循环控制

# 打印九九乘法表

i = 1;
while i <= 9:
    j = 1
    while j <= i:
        if j < i:
            print(f"{j} * {i} = {j*i}\t",end='')
        else:
            print("%d * %d = %d" % (j, i, i * j))
        j += 1
    i += 1

