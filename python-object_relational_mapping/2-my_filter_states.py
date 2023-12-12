#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
=======
"""
    script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    cursor = conn.cursor()
    sql = """ SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY id ASC """.format(sys.argv[4])

    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    conn.close()
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
