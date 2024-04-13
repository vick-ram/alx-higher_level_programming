#!/usr/bin/python3
"""
This script connects to a MySQL database and
fetches data from the 'states' table.
The script then fetches all rows from the 'states' table,
ordered by 'id' in ascending order,
and prints each row to the console.

Usage:
    python3 script.py <username> <password> <database>
"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    password=password,
    database=database
    )

cursor = db.cursor()
cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.close()
