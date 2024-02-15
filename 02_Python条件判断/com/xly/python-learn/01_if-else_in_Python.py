# -*- coding: utf-8 -*-
# @Time : 2024/1/12 10:38
# @Author : X_LY。
# @Title : 01_if-else_in_Python.py
# @Description : Python中的条件判断

"""
    Python中条件判断的语法为：
        if 要判断的条件：
            条件成立时，要做的事情
"""

age = int(input("Please enter your age: "))
if age >= 18:
    print("您已成年，可以使用")
else:
    print("您未成年，无法使用")

# if-elif的使用
age = int(input("Please enter your age: "))
if age < 10 :
    print("您可以免费使用！")
else:
    level = int(input("Please enter your level:"))
    if level == 3:
        print("尊贵的VIP3级用户，您可以免费游玩")
    elif level == 2:
        print("您的VIP等级为2，需要支付10元")
    elif level == 1:
        print("您的VIP等级为1，需要支付20元")
    else:
        print("不好意思，您没有任何的优惠权限，请支付30元")