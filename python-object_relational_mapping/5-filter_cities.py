#!/usr/bin/python3
"""Script that lists all cities of a state, using the database
hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    print(", ".join(row[0] for row in rows))
