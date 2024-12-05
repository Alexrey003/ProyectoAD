#==================================================================
# LIBRARIES
from database.connection import connect_to_database

#==================================================================
class Card():
    def __init__(self, user_id):
        self.conn = connect_to_database()
        self.user_id = user_id
#====================================================================
    def link_card(self, card_number, cardholder_name, expiration_date, ccv):
        conn = self.conn
        cursor = conn.cursor()
        try:
            month, year = map(int, expiration_date.split('/'))
            formatted_expiration_date = f"20{year:02d}-{month:02d}-01"
            
            query = """
                INSERT INTO cards
                (user_id, card_number, cardholder_name, expiration_date, ccv)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (self.user_id, card_number, cardholder_name, formatted_expiration_date, ccv))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()