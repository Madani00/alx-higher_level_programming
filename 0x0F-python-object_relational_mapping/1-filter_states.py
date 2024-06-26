#!/usr/bin/python3
"""
- a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
- the host=localhost and port=3306, exists by default
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
    sql_com = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"
    cur.execute(sql_com)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
