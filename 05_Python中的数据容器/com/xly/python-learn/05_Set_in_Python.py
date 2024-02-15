# -*- coding: utf-8 -*-
# @Time : 2024/1/15 14:20
# @Author : X_LY。
# @Title : 05_Set_in_Python.py
# @Description : Set集合

"""
    定义字面量（常量）
            {元素1，元素2，元素3，元素4......}

        定义变量
            变量名称 = {元素1，元素2，元素3，元素4......}

        定义空列表
            变量名称 = {}
            变量名称 = set()

    集合中的内容无序，且内容不能重复，但集合允许修改
"""

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 添加新元素 add()方法
print(my_set.add(10))

# 移除元素 remove()方法，集合本身被修改
print(my_set.remove(1))

# 随机取出一个元素（取出的元素从集合中被删除）
element = my_set.pop()
print(element)

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {4, 5, 6}
# 取出集合1中有而集合2中没有的数据，返回一个新集合
set3 = set1.difference(set2)
print(set3)

# 消除两个集合的差集
# 对比集合1和集合2，在集合1中，删除和集合2相同的元素
# 集合1被修改，而集合2不变
set4 = {1, 2, 3, 4}
set5 = {1, 3, 4, 6}
set4.difference_update(set5)
print(set4)
print(set5)

# 合并两个集合，xx.union(xxx)，原本的两个集合不变，得到一个新的集合
set6 = set4.union(set5)

# 集合不支持下标，所以无法使用while循环遍历，但可以使用for循环遍历