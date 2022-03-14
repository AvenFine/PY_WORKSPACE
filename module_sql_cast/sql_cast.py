#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/21 9:24
# @Author : xxx
# @FileName: sql_cast.py
# @Software: PyCharm
"""
目标将mysql的建表和插入数据语句转换成其他数据库支持的可执行SQL
1. 读取mysql导出的文件
2. 提取字段，类型信息
3. 重新拼接成SQL
"""

col_name = []
new_sql = []
keyword_list =["PRIMARY", "CONSTRAINT"]
final_sql = ""
with open("E:\PY_WORKSPACE\SQL转换\\a.sql") as file:
    date = file.read()
    # 提取建表语句
    str1 = date[date.index("(")+1:]
    str2 = str1[:str1.index(";")]

    # 按照空格/换行符切割， 然后替换关键字生成新的sql
    list = str2.split(",")
    for i in range(len(list)):
        t = list[i].replace("\n", '').split()[0:2]
        if str(t[0]) not in keyword_list:
            new_sql.append(t)
    print(new_sql)

with open("E:\PY_WORKSPACE\SQL转换\\b.sql",'w') as file:
    # 拼接成sql
    for i in range(len(new_sql)):
        name, type1 = new_sql[i][0], new_sql[i][1]
        file.writelines(name + "\t" + type1 + ",")








#     # 按照换行符截取字符串，依赖 ` 提取
#     list = str2.split("\n")
#     for i in range(len(list)):
#         str = list[i]
#         if (str.find("`")) != -1:
#
#             # 表名和字段名
#             start_index = str.find("`")
#             end_index = str.find("`", start_index+1)
#             name = str[start_index+1:end_index]
#             col_name.append(name)
#
#
#
# print(col_name)






