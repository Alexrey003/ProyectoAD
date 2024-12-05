#================================================================================
# LIBRARY
from database.connection import connect_to_database

#================================================================================
class Products():
    def __init__(self):
        self.conn = connect_to_database()
        
    def insert_product(self, reference_code, brand, model, category, price, stock):
        cursor = self.conn.cursor()
        
        query = '''
        INSERT INTO products (reference_code, brand, model, category, price, stock)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        
        cursor.execute(query, (reference_code, brand, model, category, price, stock))
        self.conn.commit()
        cursor.close()
    
    def show_products(self):
        cursor = self.conn.cursor()
        
        query = '''
        SELECY * FROM products
        '''
        
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def search_product(self, brand, model):
        cursor = self.conn.cursor()
        
        query = '''
        SELECT * FROM products WHERE brand = %s OR model = %s
        '''
        cursor.execute(query, (brand, model))
        product = cursor.fetchall()
        cursor.close()
        return product
    
    def delete_product(self, brand, model):
        cursor = self.conn.cursor()
        
        query = '''
        DELETE FROM products WHERE brand = %s OR model = %s
        '''
        
        cursor.execute(query, (brand, model))
        self.conn.close()
        cursor.close()