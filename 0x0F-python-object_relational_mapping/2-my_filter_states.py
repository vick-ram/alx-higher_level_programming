#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database
    )
    cur = db.cursor()

    query = (
        """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}' ORDER BY id ASC
        """
    )
    query = query.format(sys.argv[4])
    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
