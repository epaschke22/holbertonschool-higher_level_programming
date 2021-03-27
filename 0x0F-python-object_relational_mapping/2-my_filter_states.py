#!/usr/bin/python3
"""Lists all states from a database that match 4th argument"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
                '{}' ORDER BY id ASC;".format(sys.argv[4]))
    rows = cur.fetchall()
    print(rows[0])
    cur.close()
    conn.close()
