#!/usr/bin/python3
"""
- a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
- must use 'format' to create the SQL query with the user input
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    sql_com = "SELECT * FROM states WHERE BINARY name = '{}'
    \ ORDER BY id ASC".format(argv[4])
    cur.execute(sql_com)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
