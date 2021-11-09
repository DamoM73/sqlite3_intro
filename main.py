# main.py
from datastore import DataStore

db = DataStore()

print(db.get_dir_name_by_country("US"))
