# LIBRARIES
from database.connection import connect_to_database

#================================================================

class Product:
    @staticmethod
    def register_product(reference_code, brand, model, category, description, price, disponibility, certificate):
        # CONNECT TO THE DATABASE
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            # QUERY TO REGISTER PRODUCTS IN THE DATABASE
            query = """
                INSERT INTO products
                (reference_code, brand, model, category, description, price, disponibility, certificate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query,
                        (reference_code, brand, model, category, description, price, disponibility, certificate))
            cursor.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al ejecutar la consulta: {e}")
            raise e
        finally:
            cursor.close()
            conn.close()