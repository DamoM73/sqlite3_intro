import sqlite3

with sqlite3.connect("movies.db") as db:
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT dirname
        FROM director
        """
    )

    print(cursor.fetchall())