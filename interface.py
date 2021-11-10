# interface.py

class UI:
    
    
    def __init__(self):
        pass
    
    # Display menu
    def main_menu(self):
        """
        Displays the menu and get choice
        
        return: str
        """
        
         # Display menu
        print("Main Menu")
        print("==========")
        print("A. Queries")
        print("X. Quit\n")
        print("Please choose an option (A or X)")
        
        return input("> ").upper()
        