# _*_ coding:utf-8 _*_
import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor() # 创建游标

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]

print query
curs.execute(query) # 执行sql语句
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row): # 并行迭代
        print '%s: %s' % pair
    print