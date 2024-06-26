#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
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

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities JOIN states states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)
    res = cur.fetchall()

    for row in res:
        print(row)

    cur.close()
    db.close()
