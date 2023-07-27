#!/usr/bin/python3
""" This python file that contains the class definition of a State and an
    instance Base = declarative_base().
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    cities = ""
    sql = """SELECT cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id;"""
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute(sql)
    states = cur.fetchall()
    for i in states:
        if i[1] == argv[4]:
            if cities != "":
                cities += ", "
            cities += i[0]
    print(cities)
