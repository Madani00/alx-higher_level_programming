#!/usr/bin/python3
"""
- a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
- i didn't specify the host=localhost and port=3306, exist by default
"""
import MySQLdb
from sys import argv

if __name__ = "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
            'N%' ORDER BY id ASC")
    output = cursor.fetchall()
    for row in output:
        print(row)
    cursor.close()
    db.close()
