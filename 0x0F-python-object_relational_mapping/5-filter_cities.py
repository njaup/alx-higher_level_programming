#!/usr/bin/python3
"""This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`."""
import MySQLdb as database
from sys import argv

if __name__ == "__main__":
    """Access to the database and get the cities
    from the database."""

    database_connect = database.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], database=argv[3])

    with database_connect.cursor() as database_cursor:
        database_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        rows_selected = database_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
