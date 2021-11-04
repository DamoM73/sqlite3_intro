import sqlite3
user_input = input("Enter Country: ")

with sqlite3.connect("movies.db") as db:
    cursor = db.cursor()
    cursor.execute(
        f"""
        SELECT dirname
        FROM director
        WHERE country = :input
        """, {'input': user_input}
    )

    results = cursor.fetchall()

    for record in results:
        print(record[0])