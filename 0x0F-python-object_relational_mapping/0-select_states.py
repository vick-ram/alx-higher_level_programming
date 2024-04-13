#!/usr/bin/python3
"""A script to fetch and print all states from a database"""
import sys
import db_connector

if __name__ == "__main__":
    """
    The main function of the script.
    It takes command line arguments for the username, password,
    and database name,
    connects to the database, fetches all states, and prints them.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = db_connector.connect_to_db(username, password, database)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
