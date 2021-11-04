import sqlite3

class DataStore:

    def __init__(self):
        self.connection = sqlite3.connect("movies.db")
        self.cursor = sqlite3.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()