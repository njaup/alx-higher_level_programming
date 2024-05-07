#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb as database
from sys import argv

if __name__ == '__main__':
    """Access to the database and get the states
    from the database."""

    database_connect = database.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], database=argv[3])
    database_cursor = database_connect.cursor()

    database_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = database_cursor.fetchall()

    for row in rows_selected:
        print(row)
