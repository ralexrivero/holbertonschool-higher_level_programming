#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states tables of a database
where name matches the argument
"""

import MySQLdb
import sys

host = 'localhost'
port = 3306
username = sys.argv[1]
password = sys.argv[2]
name = sys.argv[3]
state = str(sys.argv[4])

if __name__ == "__main__":
    conn = MySQLdb.connect(host=host, port=port, user=username,
                           passwd=password, db=name, charset="utf8")
    """ not be executed when imported """
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}'ORDER BY id ASC"
                .format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()