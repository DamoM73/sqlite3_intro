# main.py
from datastore import DataStore
from interface import UI

db = DataStore()
ui = UI()

running = True

while running:
    option = ui.main_menu()
    
    
    if option == "X":
        running = False
    