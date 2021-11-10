# main.py
from datastore_eg import DataStore
from interface_eg import UI

db = DataStore()
ui = UI()

running = True

while running:
    option = ui.main_menu()
    
    # A. Queries
    if option == "A":
        queries = True
        while queries:
            query = ui.query_menu()

            # A. List countries
            if query == "A":
                ui.display_list_results(db.get_countries())
            # B. List memebers
            elif query == "B":
                ui.display_list_results(db.get_members())
            # C. List movies
            elif query == "C":
                ui.display_list_results(db.get_movies())
            # D. List directors by country
            elif query == "D":
                country = ui.get_value("Which country?")
                ui.display_list_results(db.get_dir_by_country(country))
                
            # X. Return to main menu
            elif query == "X":
                print("\n")
                queries = False
     # X. Quit program
    elif option == "X":
        running = False