#!/usr/bin/python3
"""
- a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    sql_com = "SELECT cities.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    WHERE states.name = %s"
    cur.execute(sql_com, (argv[4],))
    result = ""
    rows = cur.fetchall()
    for row in rows:
        if result == "":
            result += row[0]
        else:
            result += ", " + row[0]
    print(result)

    cur.close()
    db.close()
