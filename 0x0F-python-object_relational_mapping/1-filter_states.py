#!/usr/bin/python3
import db_connector
import sys

if __name__ == "__main__":
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
