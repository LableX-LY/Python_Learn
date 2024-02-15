# -*- coding: utf-8 -*-
# @Time : 2024/1/20 14:16
# @Author : X_LY。
# @Title : 01_Python操作MySql.py
# @Description : Python操作MySql

"""
    首先通过 pip 下载对应的驱动
    pip3 install pymysql
    使用时导入相应的包即可
"""

# 导入下载的包
from pymysql import Connection

# 获取连接对象
conn = Connection(host='localhost', user='root', port=3306, password='Xly20020618')

# 获取游标对象
cursor = conn.cursor()
# 先选择数据库
conn.select_db("J2EE")
# 使用游标对象，执行sql语句
cursor.execute("select * from t_user")
# 将查询到的数据放到元组中存储
# fetchall()方法将所有查询到的数据作为列表返回
result: tuple = cursor.fetchall()
for row in result:
    print(row)

# 关闭连接
conn.close()

# """
#     通过Python向数据库中插入数据
#     可以在每次提交时手动commit,也可以在获取连接对象时设置自动提交
# """
# conn2 = Connection(host='localhost', user='root', port=3306, password='Xly20020618', autocommit=True)
#
# # 获取游标对象
# cursor2 = conn2.cursor()
#
# # 先选择数据库
# conn2.select_db("J2EE")
#
# # 使用游标对象，执行sql语句
# cursor2.execute("insert into t_user values (4,'司亚强',202145225132,'计科N211')")
#
# # 确认添加，提交
# # conn.commit()
#
# # 关闭连接
# conn2.close()