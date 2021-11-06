# main.py
from datastore import DataStore

db = DataStore()

print(db.get_loan_details())
