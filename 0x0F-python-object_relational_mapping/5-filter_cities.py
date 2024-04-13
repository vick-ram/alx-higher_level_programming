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

    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
    cur.execute(query, (state_name,))

    res = cur.fetchone()[0]
    if res:
        print(res)

    cur.close()
    db.close()
