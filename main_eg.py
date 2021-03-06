# main.py
from datastore_eg import DataStore
from interface_eg import UI

db = DataStore()
ui = UI()

running = True

# ----- MAIN LOOP ----- #
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
                country = ui.input_value("Which country?")
                ui.display_list_results(db.get_dir_by_country(country))
            # E. List member details
            elif query == "E":
                member = ui.input_value("Which member?")
                ui.display_member_details(db.get_member_details(member))
            # F. Show movies on hire to a member
            elif query == "F":
                member = ui.input_value("Which member?")
                ui.display_list_results(db.get_member_movies(member))
            # G. List movies by a director
            elif query == "G":
                director = ui.input_value("Which director?")
                ui.display_list_results(db.get_director_movies(director))
            # H. List movie details
            elif query == "H":
                ui.display_movie_details(db.get_movie_details())
            # I. List all movies on loan
            elif query == "I":
                ui.display_movies_on_loan(db.get_loan_details())
            # X. Return to main menu
            elif query == "X":
                print("\n")
                queries = False
    
    # B. Update
    elif option == "B":
        updates = True
        while updates:
            update = ui.update_menu()
            # A. Add memeber
            if update == "A":
                mem_name, mem_address = ui.input_member_details()
                ui.operation_results(db.add_member(mem_name,mem_address))
            # B. Add movie
            elif update == "B":
                title, length, year, director = ui.input_movie_details()
                ui.operation_results(db.add_movie(title,length,year,director))
            # C. Add directors
            elif update == "C":
                name, country = ui.input_director_details()
                ui.operation_results(db.add_director(name,country))
            # D. Movie loan
            elif update == "D":
                movie,member = ui.input_loan_details()
                ui.operation_results(db.add_loan(movie,member))
            # E. Return movie
            elif update == "E":
                movie = ui.input_return_details(db.get_loan_details())
                ui.operation_results(db.return_movie(movie))
            # F. Pay fees
            elif update == "F":
                member = ui.input_member_name()
                owing = db.get_amount_owing(member)
                if not owing[0]:
                    ui.operation_results(owing)
                else:
                    payment = ui.input_payment(owing[1])
                    new_debt = owing[1] - payment
                    ui.operation_results(db.update_amount_owing(member,new_debt))                
            # X. Return to main menu
            elif update == "X":
                updates = False

    # X. Quit program        
    elif option == "X":
        running = False