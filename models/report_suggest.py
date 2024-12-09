#==================================================================================
# LIBRARIES
from database.connection import connect_to_database

#==================================================================================
class ReportAndSuggest():
    def __init__(self, user_id):
        self.conn = connect_to_database()
        self.user_id = user_id
    
    def generate_report_suggest(self, title, description, report_date):
        try:
            conn = self.conn
            cursor = conn.cursor()
            
            cursor.execute(
                """
                INSERT INTO report_suggestion (user_id, title, description, report_date)
                VALUES (%s, %s, %s, %s)
                """, (self.user_id,title, description, report_date)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")
            raise e
        finally:
            cursor.close()
            conn.close()