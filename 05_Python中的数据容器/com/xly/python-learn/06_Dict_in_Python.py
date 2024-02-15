# -*- coding: utf-8 -*-
# @Time : 2024/1/15 14:47
# @Author : X_LY。
# @Title : 06_Dict_in_Python.py
# @Description : Python中的字典(即键值对)

"""
    定义字面量（常量）
            {key:value,key:value......}

        定义变量
            变量名称 = {key:value,key:value......}

        定义空列表
            变量名称 = {}
            变量名称 = dict()

    字典允许嵌套
"""

my_dict = {
    "key1": {
        "key2": "value2",
        "key3": "value3"
    }
}

my_dict2 = {"11": 22, "22": 33, "33": 44}

# 1.新增元素
my_dict2[44] = 55
print(f"更新后的字典为：{my_dict2}")

# 2.修改元素
my_dict2[11] = 11
print(f"修改后的字典为：{my_dict2}")

# 3.删除元素（取出元素并返回）
score = my_dict2[33]
print(score)

# 4.清空字典，clear()方法

# 获取全部的key，获取到的key组成一个新的集合并返回
# 获取到全部的key之后，方便进行遍历
# 当然，直接对字典进行for循环也是可以的，for key in my_dict2
keys = my_dict2.keys()
for key in keys:
    print(my_dict2[key])
