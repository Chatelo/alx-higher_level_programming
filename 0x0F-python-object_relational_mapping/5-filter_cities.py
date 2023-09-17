#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve cities of the given state
    cursor.execute(
        "SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`"
    )

    # Fetch all the rows returned by the query
    cities = cursor.fetchall()

    # Print the cities
    print(", ".join([cities[2] for cities in cities
                     if cities[4] == state_name]))

    # Close cursor and database connection
    cursor.close()
    db.close()
