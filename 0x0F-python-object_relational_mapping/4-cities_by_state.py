#!/usr/bin/python3
"""This script lists all cities from
the database `hbtn_0e_4_usa`."""
import MySQLdb as database
from sys import argv

if __name__ == '__main__':
    """Access the database and get the cities
    from the database."""

    database_connect = database.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], database=argv[3])

    with database_connect.cursor() as database_cursor:
        database_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = database_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
