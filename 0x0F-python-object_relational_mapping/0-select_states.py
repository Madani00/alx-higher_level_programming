#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    output = cursor.fetchall()
    for row in output:
        print(row)
    cursor.close()
    db.close()
