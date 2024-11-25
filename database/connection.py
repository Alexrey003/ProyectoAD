#LIBRARIES
import mariadb
from utils.config import DB_CONFIG
from tkinter import messagebox

# CONNECTION TO DATABASE
def connect_to_database():
    try:
        db_conection = mariadb.connect(
            user= DB_CONFIG.get('user'),
            password=DB_CONFIG.get('password'),
            host=DB_CONFIG.get('host'),
            port=DB_CONFIG.get('port'),
            database=DB_CONFIG.get('database')
        )
        return db_conection
    except mariadb.Error as e:
        print(f"Error connecting to database: {e}")