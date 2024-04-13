#!/usr/bin/python3
"""
This module provides a function to connect to the database.
It uses the MySQLdb library to establish a connection
to a MySQL database.
"""
import MySQLdb


def connect_to_db(username, password, database):
    """
    Connect to the MySQL database using the given
    username, password, and database name.
    Parameters:
    username (str): The username to use for the database connection.
    password (str): The password to use for the database connection.
    database (str): The name of the database to connect to.
    Returns:
    MySQLdb.connections.Connection: A connection to the database.
    """
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        username=username,
        password=password,
        datatbase=database
    )
