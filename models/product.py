# # LIBRARIES
# from database.connection import connect_to_database

# #================================================================

# class Product():
#     @staticmethod
#     def register_product(reference_code, brand, model, category, price):
#         # CONNECT TO THE DATABASE
#         conn = connect_to_database()
#         cursor = conn.cursor()
#         try:
#             # CHECK IF THE PRODUCT ALREADY EXISTS IN THE DATABASE
#             check_query = "SELECT stock FROM products WHERE reference_code = %s"
#             cursor.execute(check_query, (reference_code,))
#             result = cursor.fetchone()
            
#             if result:
#                 update_query = "UPDATE products SET stock = stock + 1 WHERE reference_code = %s"
#                 cursor.execute(update_query, (reference_code,))
#             else:
#                 add_query = """
#                     INSERT INTO products
#                     (reference_code, brand, model, category, price, stock)
#                     VALUES (%s, %s, %s, %s, %s)
#                 """
#                 cursor.execute(add_query,
#                             (reference_code, brand, model, category, price, 1))
#             cursor.commit()
#         except Exception as e:
#             conn.rollback()
#             print(f"Error al ejecutar la consulta: {e}")
#             raise e
#         finally:
#             cursor.close()
#             conn.close()