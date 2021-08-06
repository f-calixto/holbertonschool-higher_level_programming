#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''

from sys import argv
import MySQLdb

db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
cursor = db.cursor()
sql = "SELECT * FROM states;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
