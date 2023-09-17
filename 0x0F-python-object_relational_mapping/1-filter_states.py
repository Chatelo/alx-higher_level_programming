#!/usr/bin/python3
"""
Script lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]

    cursor.close()
    db.close()
