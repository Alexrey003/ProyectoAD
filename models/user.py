#LIBRARIES
from database.connection import connect_to_database

#================================================================
class User():
    @staticmethod
    def create_user(name, lastname, direction, phone, email, username, password):
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO users 
                (name, lastname, direction, phone, email, username, password) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, lastname, direction, phone, email, username, password))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error al ejecutar la consulta: {e}")
            raise e
        finally:
            cursor.close()
            conn.close()