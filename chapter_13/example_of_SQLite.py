# _*_ coding:utf-8 _*_
import sqlite3
conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()
conn.commit()
conn.close()