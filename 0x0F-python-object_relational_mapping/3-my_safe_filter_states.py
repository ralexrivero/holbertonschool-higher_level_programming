#!/usr/bin/python3
"""
takes in arguments and sisplays all values in the sates table of database
where name matches the argument, safe from MySQL injections
"""

import MySQLdb
import sys

host = 'localhost'
port = 3306
username = sys.argv[1]
password = sys.argv[2]
name = sys.argv[3]


if __name__ == "__main__":
    """ not be executed when imported """
    conn = MySQLdb.connect(host=host, port=port, user=username,
                           passwd=password, db=name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
