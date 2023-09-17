#!/usr/bin/python3
"""
Script takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Create the SQL query using format to include the user input
    query = "SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4])

    # Execute the query to retrieve states with the matching name
    cursor.execute(query)
    
    states = cursor.fetchall()

    # Print the states
    [print(state) for state in states]

    # Close cursor and database connection
    cursor.close()
    db.close()
