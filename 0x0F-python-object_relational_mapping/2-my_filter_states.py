#!/usr/bin/python3
"""
- a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
- must use 'format' to create the SQL query with the user input
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
            '{}' ORDER BY id ASC".format(argv[4]))
    output = cursor.fetchall()
    for row in output:
        print(row)
    cursor.close()
    db.close()
