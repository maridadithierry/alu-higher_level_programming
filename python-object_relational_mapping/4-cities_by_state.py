#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
=======
"""
    A script that lists all cities from the database hbtn_0e_4_usa
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

    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    cursor.execute(sql)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
