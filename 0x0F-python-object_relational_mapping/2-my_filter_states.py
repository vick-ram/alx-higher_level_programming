#!/usr/bin/python3
import sys
import db_connector


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = db_connector.connect_to_db(username, password, database)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name = %s ORDER BY id ASC""", (state_name,))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
