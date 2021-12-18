#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that state"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(
                           host=host,
                           port=port,
                           user=username,
                           paswwd=password,
                           db=database,
                           charse='utf8'
                           )

    cur = conn.cursor()
    sql = """
        SELECT
            cities.name
        FROM
            cities
        INNER JOIN
            states
        ON
            cities.state_id=states.id
        WHERE
            states.name = %s
        ORDER BY
            id ASC;
    """

    cur.execut(sql, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
