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


    def get_dir_by_country(self, country):
        """
        Returns a list of directors names from the provided country

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
            {"country" : country}
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results


    def get_member_details(self, member):
        """
        Returns a the provided member's details

        member: str
        return: tuple(str,str,float)
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT memname, address, owes
            FROM members
            WHERE memname = :member
            """,
            {"member" : member}
        )
        results = self.cursor.fetchall()

        # clean results
        return results[0]

    
    def get_member_movies(self, member):
        """
        Returns a the movies currently on hire to the member

        member: str
        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            WHERE movienumb IN (
                SELECT movienumber
                FROM movies_onhire
                WHERE memberid IN (
                    SELECT memberid
                    FROM members
                    WHERE memname = :member
                )
            )
            """,
            {"member" : member}
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results


    def get_director_movies(self, director):
        """
        Returns a the movies directed by provided director

        director: str
        return: list[str]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            WHERE dirnumb IN (
                SELECT dirnumb
                FROM director
                WHERE dirname = :director
            )
            """,
            {"director" : director}
        )
        results = self.cursor.fetchall()

        # clean results
        clean_results = []
        for item in results:
            clean_results.append(item[0])

        return clean_results


    def get_movie_details(self):
        """
        Returns all the movies details of name, length, year and director

        return: list[(str,int,int,str)]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT m.movname, m.length, m.year, d.dirname
            FROM movie AS m
            JOIN director AS d
            ON m.dirnumb = d.dirnumb
            """
        )
        results = self.cursor.fetchall()

        return results


    def get_loan_details(self):
        """
        Returns the details of all the movies on loan
        movie name, member name, due date

        return: list[(str,str,str)]
        """

        # excute query and get results
        self.cursor.execute(
            """
            SELECT mov.movname, mem.memname, hire.duedate
            FROM movie AS mov
            JOIN movies_onhire AS hire
            ON mov.movienumb = hire.movienumber
            JOIN members AS mem
            ON mem.memberid = hire.memberid
            """
        )
        results = self.cursor.fetchall()

        return results
    
    
    def add_new_member(self,name,address):
        """
        Add new member details
        
        name: str
        address: str
        """
        
        # find new member id
        self.cursor.execute(
            """
            SELECT MAX(memberid)
            FROM members
            """
        )
        
        member_id = self.cursor.fetchone()[0] + 1
        
        # add details to database
        self.cursor.execute(
            """
            INSERT INTO members
            VALUES (:memberid,:name,:address,:owes)
            """,
            {
                "memberid": member_id,
                "name": name,
                "address": address,
                "owes": None
            }
        )
        
        return f"Member {name} added" 
        