#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database
    )
    cur = db.cursor()

    query = ("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """)
    cur.execute(query, (state_name,))
    print(", ".join(map(lambda x: x[0], cur.fetchall())))

    cur.close()
    db.close()
