#!/usr/bin/python3
''' write one that is safe from MySQL injections! '''

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id IN\
                (SELECT id FROM states WHERE name = %s)\
                ORDER BY cities.id", (state_name, ))
    query_rows = cur.fetchall()
    for index, row in enumerate(query_rows):
        if index < len(query_rows) - 1:
            sep = ', '
            end = ''
        else:
            sep = ''
        print(row[0] + sep, end=end)
    print()
    cur.close()
    conn.close()
