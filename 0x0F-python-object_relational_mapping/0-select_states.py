#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
