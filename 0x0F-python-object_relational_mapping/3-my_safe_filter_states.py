#!/usr/bin/python3
"""
- a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
- write one that is safe from MySQL injections!
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
    comm = "SELECT * FROM states WHERE name = %s LIKE BINARY '{}' \
    ORDER BY id".format(argv[4])
    cur.execute(comm, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
