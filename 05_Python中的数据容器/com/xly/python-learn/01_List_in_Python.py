# -*- coding: utf-8 -*-
# @Time : 2024/1/14 10:25
# @Author : X_LY。
# @Title : 01_List_in_Python.py
# @Description : Python中的List集合

"""
    基本定义语法：

        定义字面量（常量）
            [元素1，元素2，元素3，元素4......]

        定义变量
            变量名称 = [元素1，元素2，元素3，元素4......]

        定义空列表
            变量名称 = []
            变量名称 = list()

        List列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套(即 列表中再存放列表)

        List的下标支持反向读取，即从右向左读
            [1, 2, 3, 4, 5, 6]
            -6  -5  -4 -3  -2 -1
"""
my_list = [[1, 2, 3], [4, 5, 6]]

my_list2 = [1, 2, 3, 4, 5, 6]
print(my_list2[-1])



"""
    List列表的常用操作
"""

mylist = ["My", "name", "is", "XLY"]

# 1.查找某元素再列表中的下标索引
index = mylist.index("XLY")
print("下标索引为%d" % index)

# 2.修改特定下标索引的值
mylist[3] = "X-LY。"
print(f"修改后的内容为:{mylist}")

# 3.在指定下标位置插入新的元素
mylist.insert(3, "not")
print(f"修改后的内容为:{mylist}")

# 4.在列表的末尾追加"""一个"""元素
mylist.append("hahahaha")
print(f"追加元素后的列表为:{mylist}")

# 5.在列表的末尾追加"""多个"""元素
mylist2 = ["What's", "your", "name", "?"]
mylist.append(mylist2)
print(f"追加另一个列表后的列表为:{mylist}")

# 6.删除列表中的某个元素
del mylist[2]

# 7.取出列表中的某个元素，并返回（作用类似于删除）
deleted = mylist.pop(3)
print(deleted)

# 8.删除某元素在列表中的第一个匹配项
mylist2.remove("your")
print(mylist2)

# 9.清空列表的内容
mylist.clear()

# 10.统计某元素在列表内的数量
print(my_list.count("My"))

