#!/usr/bin/python3
"""A script to fetch and print all states from a database"""
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

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
