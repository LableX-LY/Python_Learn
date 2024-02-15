# -*- coding: utf-8 -*-
# @Time : 2024/1/11 20:57
# @Author : X_LY。
# @Title : 09_StringFormat_in_Python.py
# @Description :

# Python与Java一样，使用 + 号对字符串进行拼接

# 在Python中，数字无法和字符串进行拼接

"""
    Python中字符串格式化的语法为
    "%占位符"%变量
    常用的占位符有三类
        字符串 : %s
        整数 : %d
        浮点数 : %f
"""
name = "XLY。"
print("My name is %s" % name)

"""
    Python精度控制语法
        m 控制宽度
        .n 控制小数点位数
        
    如果m比数字本身的宽度还小，则m宽度控制不会生效
    如果m超出了数字的宽度，则会在数字前面通过添加空格的方式进行补位
    小数点也会计入数据的宽度内
    
    使用.n来控制小数点位数时，会自动对数据进行四舍五入
"""
num = 52
print("%5d" %num)

num2 = 13.145
print("%5.2f" %num2)

# 当要多个数据进行格式化时，需要将数据用括号括起来(把%提取出来，写一次即可)
# 但这种方式不会理会数据的类型，不会对数据做精度控制
name = "XLY"
age = 23.23
print("My name is %5s,and my age is %2.f" %(name , age))

"""
    Python字符串格式化的快速写法
        f"内容{变量}"
"""
print(f"My name is {name} and my age is {age}")

"""
    对表达式进行格式化
        表达式：一条具有明确执行结果的代码语句
"""
print("1 + 1的结果是:%d"%(1 + 1))