#!/usr/bin/python3
"""script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import db_connector
import sys

if __name__ == "__main__":
    """Defines username, password and database name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = db_connector.connect_to_db(username, password, database)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
