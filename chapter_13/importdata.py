# _*_ coding:utf-8 _*_
import sqlite3


def convert(value):
    if value.startswith('~'):
        return value.strip('~')  # 删除value中的'~'字符
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.d')
curs = conn.cursor()  # 创建游标
# 执行SQl语句
curs.execute('''
CREATE TABLE food(
    id         TEXT    PRIMARY KEY,
    desc       TEXT,
    water      FLOAT,
    kcal       FLOAT,
    protein    FLOAT,
    fat        FLOAT,
    ash        FLOAT,
    carbs      FLOAT,
    fiber      FLOAT,
    sugar      FLOAT
            )
            ''')
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?,)'

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_conut]]
    curs.execute(query, vals)

conn.commit()
conn.close()
