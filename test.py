from datastore_eg import DataStore
from utils import cal_due_date

db = DataStore()

db.cursor.execute(
    """
    SELECT dirnumb
    FROM director
    WHERE dirname = "Harry Wright"
    """
)

print(db.cursor.fetchone())