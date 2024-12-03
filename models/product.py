#================================================================================
# LIBRARY
from database.connection import connect_to_database

#================================================================================
class Products():
    def __init__(self):
        self.conn = connect_to_database()
    def insert_product(self, reference_code, brand, model, category, price, stock):
        cursor = self.conn.cursor()
        