# main.py
from datastore_eg import DataStore
from interface_eg import UI

db = DataStore()
ui = UI()

running = True

while running:
    option = ui.main_menu()

    if option == "A":
        queries = True
        while queries:
            query = ui.query_menu()

            if query == "A":
                ui.display_list_results(db.get_countries())
            elif query == "B":
                ui.display_list_results(db.get_members())

            elif query == "X":
                print("\n")
                queries = False
    
    elif option == "X":
        running = False