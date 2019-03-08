#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/3 01:15
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : insert_big_data_to_mysql.py
import math
import time

import gevent
import pymysql

from secure import HOST, PORT, USER, PASSWORD


class InsertBigData:
    def __init__(self, host, port, username, password, db, data, sql, charset='utf8'):
        # pymysql连接mysql数据库,需要的参数host,port,user,password,db,charset
        self.conn = pymysql.connect(host=host, port=port, user=username, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()  # 创建游标
        self.data = data  # 需要写入 MySQL 的数据，类型为元组的列表，单条记录是元组
        self.sql = sql  # 插入查询的 sql 语句
        self.asynchronous()  # 连接mysql后执行的函数

    def insert(self, n_min, n_max, length):
        data_list = []
        for j in range(n_min, n_max):
            if j <= length:
                item = self.data[j - 1]
                data_list.append(item)

        content = self.cur.executemany(self.sql, data_list)  # 执行多行插入，executemany(sql语句,数据(需一个元组类型))
        if content:
            print('成功插入第{}条数据'.format(n_max - 1))

        self.conn.commit()  # 提交数据,必须提交，不然数据不会保存

    def asynchronous(self):
        max_line = 10000  # 定义每次最大插入行数(max_line=10000,即一次插入10000行)
        length = len(self.data)  # length 表示所插入数据的长度

        if length <= max_line:
            number = length + max_line  # 如果数据条数少于10000，则将上限定位（10000 + length）
        else:
            number = math.ceil(length / max_line) * max_line  # 如果数据条数大于10000，则将上限定为数据条数向上取整

        # g_l 任务列表，定义了异步的函数: 这里用到了一个gevent.spawn方法
        g_l = [gevent.spawn(self.insert, i, i + max_line, length) for i in range(1, number, max_line)]

        gevent.joinall(g_l)  # gevent.joinall 等待所以操作都执行完毕
        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭pymysql连接


if __name__ == '__main__':
    # 向 db20 表插入 300 万条测试数据
    big_data = []
    for i in range(1, 3000001):
        result = (i, 'bob' + str(i), 'male', 'bob' + str(i) + '@qq.com')
        big_data.append(result)
    sql_seq = 'insert into userinfo(id,name,gender,email) values (%s,%s,%s,%s)'  # 定义sql语句,插入数据id,name,gender,email
    DATABASE = 'test'

    start_time = time.time()  # 计算程序开始时间
    insert_big_data = InsertBigData(HOST, PORT, USER, PASSWORD, DATABASE, big_data, sql_seq)  # 实例化类，传入必要参数
    print('程序耗时{:.2f}'.format(time.time() - start_time))  # 计算程序总耗时
