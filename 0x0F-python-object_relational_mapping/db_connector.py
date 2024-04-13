#!/usr/bin/python3
"""Database connector module"""
import MySQLdb


def connect_to_db(username, password, database):
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
