# interface_eg.py

from utils import convert_mins

class UI:

    def __init__(self):
        pass

    
    def main_menu(self):
        """
        Diplays the menu options for player to choose

        return: str
        """

        # Display menu
        print("Main Menu")
        print("==========")
        print("A. Queries")
        print("X. Quit\n")
        print("Please choose an option (A or X)")
        
        # get option
        while True:
            response = input("> ").upper()
            if response in ["A", "X"]:
                return response
            else:
                print("Incorrect choice\n")


    def query_menu(self):
        """
        Displays the query options

        return: str
        """

        # display menu
        print("Query Menu")
        print("==========")
        print("A. List countries")
        print("B. List memebers")
        print("C. List movies")
        print("D. List directors by country")
        print("E. List member details")
        print("F. Show movies on hire to a member")
        print("G. List movies by a director")
        print("H. List movie details")
        print("I. List all movies on loan")
        print("X. Return to main menu\n")
        print("Please choose an option (A to I or X)")

        # get option
        while True:
            response = input("> ").upper()
            if response in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "X"]:
                return response
            else:
                print("Incorrect choice\n")


    def display_list_results(self, results):
        """
        Displays the results from a list one result per line

        results: list[str]
        """

        for result in results:
            print(result)

        input("\npress <enter> to continue\n")
        
    
    def get_value(self, prompt):
        """
        Displays prompt and returns user response
        
        prompt: str
        return: str
        """
        
        print(prompt)
        return input("> ")
        
    
    def display_member_details(self,member):
        """
        Displays the member name, address and amount owing
        
        member: (str,str,float)
        """
        
        print(f"{member[0]}\t{member[1]}\t{member[2]}")
        
        input("\npress <enter> to continue\n")
        
    
    def display_movie_details(self,movies):
        """
        Displays the details of the movies in the database
        
        movies: list
        """

        for movie in movies:
            print(f"{movie[0]} ({movie[2]}) directed by {movie[3]}. Run time {convert_mins(movie[1])}")
            
        input("\npress <enter> to continue\n")
        
    
    def display_movies_on_loan(self,movies):
        """
        Displays the movies that are one loan
        
        movies: list[(str,str,str)]
        """
        
        for movie in movies:
            print(f"{movie[0]} on loan to {movie[1]}. Due back on {movie[2]}")
            
        input("\npress <enter> to continue\n")