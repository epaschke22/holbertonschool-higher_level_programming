#!/usr/bin/python3
"""Lists all cities from a database"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name, states.name FROM states LEFT JOIN cities \
                ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    try:
        output = []
        for row in rows:
            if row[1] == sys.argv[4]:
                output.append(row[0])
        for i in range(len(output)):
            print(output[i], end='')
            if i < len(output) - 1:
                print(', ', end='')
    except:
        pass
    print('')
    cur.close()
    conn.close()
