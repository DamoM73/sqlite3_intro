# datastore.py
import sqlite3

class DataStore:

    def __init__(self):
        """
        Initialise the Datastore instance
        """

        # ---- Attirbutes ---- #
        self.connection = sqlite3.connect("movies.db")
        self.cursor = self.connection.cursor()


    def __del__(self):
        """
        Write data in cache and close connection when program finishes
        """
        self.connection.commit()
        self.connection.close()


    def get_countries(self):
        """
        Returns a list of the countries in directors table

        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT DISTINCT country
            FROM director
            """
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results


    def get_members(self):
        """
        Returns a list of names from the members table

        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT memname
            FROM members
            """
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results


    def get_movies(self):
        """
        Returns a list of movie names from the movie table

        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            """
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results
    
    def get_dir_name_by_country(self, country):
        """
        Returns a list of directors from a given country
        
        country: str
        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT dirname
            FROM director
            WHERE country = :country
            """,
            {"country": country}
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results