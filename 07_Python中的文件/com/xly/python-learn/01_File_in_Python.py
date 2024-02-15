# -*- coding: utf-8 -*-
# @Time : 2024/1/18 17:20
# @Author : X_LY。
# @Title : 01_File_in_Python.py
# @Description : Python中文件的基本操作

# 打开并读取文件，读取出的文件内信息以 字符串 的形式存在
f = open("/Users/x-ly/Code/PyCharm/Python_Learn/test.txt", "r", encoding="utf-8")
print(f"读取10个字节的内容为:{f.read(10)}")
print(f"全部读取的内容为:{f.read()}")

# 读取文件 -readlines(),读取文件的全部行，并封装到列表中
lines = f.readlines()

# 读取文件 -readline(),一行一行的读取

# for循环读取文件的每一行
for line in lines:
    print(f"每一行的内容是:{line}")

# with open 语法
# with open () as f:,这样写程序会自动为我们关闭文件，不需要我们手动进行关闭操作 xx.close()
with open("/Users/x-ly/Code/PyCharm/Python_Learn/test.txt", "r", encoding="utf-8") as f:
    print(f"全部读取的内容为:{f.read()}")

"""
    文件的写入
        1.打开文件
            f = open("/Users/x-ly/Code/PyCharm/Python_Learn/test.txt", "r", encoding="utf-8")
                a 模式:内容追加
                w 模式:覆盖写入模式
                r 模式:只读模式
        2.文件写入
            f.write("Hello World")
        3.内容刷新
            f.flush()
            
    直接调用write方法，内容并为真正的写入文件，而是积攒在程序的内存中，称为“缓冲区”
    调用flush()方法，内容才会真正的写入文件（硬盘中）
    
    一般情况下，执行完write()方法后，执行flush()方法，再执行.close()方法，关闭文件流
    当然，也可以不写flush()方法，直接.close()方法，因为执行.close()方法会自动触发flush()方法
"""
