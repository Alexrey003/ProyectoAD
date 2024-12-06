#=================================================================
#LIBRARIES
from tkinter import *
from tkinter import ttk
from utils.config import APP_TITLE
from controllers.cart_controller import register_card
from database.connection import connect_to_database
from tkinter import messagebox
import datetime

#================================================================
class CheckOut(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.conn = connect_to_database()
        self.user_id = user_id
        
        # FETCH USER INFORMATION
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT name, lastname, direction, phone FROM users WHERE user_id = %s  
            """,(self.user_id,)
        )
        row = cursor.fetchone()
        
        if row:
            self.user_info = {
                "name":row[0] if row[0] else "N/A",
                "lastname":row[1] if row[1] else "N/A",
                "direction":row[2] if row[2] else "N/A",
                "phone":row[3] if row[3] else "N/A"
            }
        else:
            self.user_info = {
                "name": "N/A",
                "lastname": "N/A",
                "direction": "N/A",
                "phone": "N/A"
            }
        cursor.close()
#===================================================================
        #WINDOWS PROPERTIES
        self.title(APP_TITLE + "Ventana de pago v1.5")
        self.geometry("800x650+180+50")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
#===================================================================
        #FRAME HEADING
        self.heading_frame = Frame(
            self,
            bg="MediumPurple4",
            width=800,
            height=100
        )
        self.heading_frame.pack(side="top")
        
        self.heading_title = Label(
            self.heading_frame,
            text="Ventana de pago",
            fg="white",
            font=('Bahnscrift', 18, 'bold'),
            bg="MediumPurple4"
        )
        self.heading_title.place(x=80, y=5)

        self.heading_text_1 = Label(
            self.heading_frame,
            text="Por favor, ingrese los datos de su tarjeta para confirmar el pago.",
            font=('Bahnscrift', 13, 'bold'),
            bg="MediumPurple4",
            fg="white"
        )
        self.heading_text_1.place(x=80, y=45)
#==================================================================
        #JUMPING OUT FROM DE CHECKOUT WINDOW BUTTON
        self.goback_btn = Button(
            self.heading_frame,
            text="Atras",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 10, 'bold'),
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.go_back
        )
        self.goback_btn.place(x=12, y=10)
#=================================================================
        #CHECKOUT FIELDS
        #CHECKOUT FRAME
        self.checkout_frame = Frame(
            self,
            bg="gray20",
            width=800,
            height=500,
            bd=10
        )
        self.checkout_frame.pack(side="top")
        
        #CARD NUMBER ITEMS
        self.card_number_label = Label(
            self,
            text="Numero de tarjeta:",
            font=('Bahnscrift', 14, 'bold'),
            bg="gray19",
            fg="white"
        )
        self.card_number_label.place(x=30, y=150)
        
        self.card_number_entry = Entry(
            self,
            width=20,
            font=("Bahnscrift", 13),
            fg="white",
            bg="gray19"
        )
        self.card_number_entry.place(x=210, y=153)
        
        #NAME OF THE OWNER ITEMS
        self.name_owner_label = Label(
            self,
            text="Nombre del propietario:",
            font=('Bahnscrift', 14, 'bold'),
            bg="gray19",
            fg="white"
        )
        self.name_owner_label.place(x=30, y=250)
        
        self.name_owner_entry = Entry(
            self,
            width=20,
            font=("Bahnscrift", 13),
            fg="white",
            bg="gray19"
        )
        self.name_owner_entry.place(x=260, y=253)
        
        #EXPIRATION DATE ITEMS
        self.expiration_date_label = Label(
            self,
            text="Fecha de expiración:",
            font=('Bahnscrift', 14, 'bold'),
            bg="gray19",
            fg="white"
        )
        self.expiration_date_label.place(x=450, y=150)
        
        #MONTH SELECTOR
        self.expiration_month_var = StringVar()
        self.expiration_month_menu = ttk.Combobox(
            self,
            textvariable=self.expiration_month_var,
            values=[f"{i:02d}" for i in range(1,13)],
            state="readonly",
            width=3,
            font=('Bahnscrift', 13)
        )
        self.expiration_month_menu.set('MM')
        self.expiration_month_menu.place(x=655, y=153)
        
        #YEAR SELECTOR
        current_year = datetime.datetime.now().year
        self.expiration_year_var = StringVar()
        self.expiration_year_menu = ttk.Combobox(
            self,
            textvariable=self.expiration_year_var,
            values=[str(year)[2:] for year in range(current_year, current_year + 20)],
            state="readonly",
            width=5,
            font=('Bahnscrift', 13)
        )
        self.expiration_year_menu.set('YY')
        self.expiration_year_menu.place(x=700, y=153)
        
        # #CCV ITEMS
        self.ccv_label = Label(
            self,
            text="CCV:",
            font=('Bahnscrift', 14, 'bold'),
            bg="gray19",
            fg="white"
        )
        self.ccv_label.place(x=450, y=250)
        
        self.ccv_entry = Entry(
            self,
            width=5,
            font=("Bahnscrift", 13),
            fg="white",
            bg="gray19"
        )
        self.ccv_entry.place(x=505, y=253)

        self.div_frame = Frame(
            self,
            bg="SlateBlue1",
            width=800,
            height=2
        )
        self.div_frame.place(y=300)

#========================================================================================================
        # USER INFORMATION ITEMS
        self.user_info_label = Label(
            self,
            text="Informaciòn de entrega de los productos.",
            fg="white",
            bg="gray20",
            font=("Bahnscrift", 13, 'bold')
        )
        self.user_info_label.place(x=10, y=310)
        
        # USER NAME LABEL
        self.name_label = Label(
            self,
            text=f"Nombre: {self.user_info['name']} {self.user_info['lastname']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.name_label.place(x=15, y=350)
        
        # PHONE LABEL
        self.phone_label = Label(
            self,
            text=f"Telefono: {self.user_info['phone']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.phone_label.place(x=15, y=400)
        
        # DIRECTION LABEL
        self.direction_label = Label(
            self,
            text=f"Direcciòn: {self.user_info['direction']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.direction_label.place(x=15, y=450)
        
        #TOTAL PRICE LABEL
        self.total_price_label = Label(
            self,
            text="Total a pagar: $0.00",
            font=("Bahnscrift", 13, 'bold'),
            bg="gray19",
            fg="white"
        )
        self.total_price_label.place(x=15, y=500)
        
#=======================================================================================================
        # CONFIRM PURCHASE BUTTON
        self.proceed_btn = Button(
            self,
            text="Confirmar pago",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15, 'bold'),
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command= self.confirm_purchase
        )
        self.proceed_btn.place(x=600, y=550)

        # SUBMIT CARD BUTTON
        self.submit_card =  Button(
            self,
            text="Añadir tarjeta",
            font=('Bahnscrift', 14, 'bold'),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.linking_card
        )
        self.submit_card.place(x=450, y=552)
        
        self.saved_cards_var = StringVar()
        self.saved_cards_menu = ttk.Combobox(
            self,
            textvariable=self.saved_cards_var,
            values=[],
            state="readonly",
            width=40,
            font=('Bahnscrift', 14, 'bold')
        )
        self.saved_cards_menu.place(x=10, y=105)
        self.saved_cards_menu.set('Selecciona una tarjeta')
        self.load_saved_cards()
        
        self.populate_btn = Button(
            self,
            text="Usar tarjeta seleccionada",
            font=('Bahnscrift', 13, 'bold'),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.populate_card_details
        )
        self.populate_btn.place(x=490, y=105)
        
#=======  METHODS   ===========================================================
    #METHOD TO GO BACK TO THE SHOPPING-CART WINDOW
    def go_back(self):
        from views.shopping_cart import ShoppingCartWindow
        self.destroy()
        shopping_cart_window = ShoppingCartWindow(self.user_id)
        shopping_cart_window.mainloop()

#================================================================================
    #METHOD THAT SAVE THE DATA OF THE CARD IN THE DATABASE
    def linking_card(self):
        try:
            # GETTING THE MONTH AND YEAR FROM THE COMBOBOX
            selected_month = self.expiration_month_var.get()
            selected_year = self.expiration_year_var.get()
            
            # VALIDATION OF THE MONTH AND YEAR
            if selected_month == 'MM' or selected_year == 'YY':
                messagebox.showerror("Error", "Por favor, seleccione la fecha de expiración.")
                return
            
            expiration_date = f"{selected_month}/{selected_year}" #SAVING IN A VARIABLE THE MONTH AND YEAR
            
            #GETTING TE REST OF THE DATA OF THE CARD
            result = register_card(
                self.user_id,
                self.card_number_entry.get(),
                self.name_owner_entry.get(),
                expiration_date,
                self.ccv_entry.get()
            )
            
            # IF THE CARD WAS REGISTERED CORRECTLY, SHOWING AN INFORMATION MESSAGE
            if "correctamente" in result:
                messagebox.showinfo("Exito", result)
            else:
                messagebox.showerror("Error", result)
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
    
#=========================================================================================
    def create_bill (self, sale_id):
        #LIBRARIES
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.platypus import Table
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        import sys
        import os

        try:
            cursor = self.conn.cursor() #CURSOR FOR THE DATABASE
            
            #QUERY THAT SELECT THE INFORMATION FOR THE BILL
            cursor.execute(
                """
                SELECT s.sale_date, s.total_amount, c.card_number, u.name, u.lastname, u.direction
                FROM sales s
                INNER JOIN cards c ON s.card_id = c.card_id
                INNER JOIN users u ON s.user_id = u.user_id
                WHERE s.sale_id = %s
                """, (sale_id,)
            )
            sale_info = cursor.fetchone()
            
            if not sale_info:
                messagebox.showerror("Error", "No se encontro información de la venta")
                return
            
            sale_date, total_amount, card_number, name, lastname, direction = sale_info
            
            cursor.execute(
                """
                SELECT p.brand, p.model, sd.quantity, sd.subtotal
                FROM sale_details sd
                INNER JOIN products p ON sd.product_code= p.reference_code
                WHERE sd.sale_id = %s
                """, (sale_id,)
            )
            sale_details = cursor.fetchall()
            
            if not sale_details:
                messagebox.showerror("Error", "No se encontro información de los detalles de la venta")
                return
            
            products = [["Producto", "Modelo", "Cantidad", "Subtotal"]]
            for brand, model, quantity, subtotal in sale_details:
                products.append([brand, model, quantity, f"{subtotal:.2f}"])
            
            pdf_file = f"bills/factura_{sale_id}.pdf"
            c = canvas.Canvas(pdf_file, pagesize=letter)
            width, height = letter
            
            c.setFont('Helvetica-Bold', 16)
            c.drawString(100, height - 50, f"Factura #{sale_id}")
            c.drawString(100, height - 70, f"Fecha: {sale_date}")
            c.drawString(100, height - 100, f"Cliente: {name} {lastname}")
            c.drawString(100, height - 120, f"Dirección: {direction}")
            c.drawString(100, height - 140, f"Tarjeta: **** **** **** {card_number[-4:]}")
            
            table = Table(products, colWidths=[20, 200, 50, 50])
            table.wrapOn(c, width, height)
            table.drawOn(c, 50, height - 300)
            
            c.drawString(50, height - 350, f"Total a pagar: ${total_amount:.2f}")
            c.drawString(50, height - 400, "Gracias por su compra.")
            
            c.save()
            
            cursor.execute(
                """
                UPDATE sales SET bill_file = %s WHERE sale_id = %s;
                """, (pdf_file, sale_id)
            )
            self.conn.commit()
            
            messagebox.showinfo("Factura generada", f"La factura #{sale_id} se ha generado correctamente")
            os.startfile(os.path.abspath(pdf_file))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado al generar la factura: {e}")
        finally:
            cursor.close()
#=====================================================================================================================
    def load_saved_cards(self):
        try:
            cursor = self.conn.cursor()
            
            cursor.execute(
                """
                SELECT card_id, card_number, cardholder_name, expiration_date
                FROM cards
                WHERE user_id = %s
                """, (self.user_id,)
            )
            saved_cards = cursor.fetchall()
            
            self.saved_cards_menu['values'] = [
                f"{card_id} - **** **** **** {card_number[-4:]} - {cardholder_name} - {expiration_date}"
                for card_id, card_number, cardholder_name, expiration_date in saved_cards
            ]
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado al cargar las tarjetas guardadas: {e}")
        finally:
            cursor.close()
        
    def populate_card_details(self):
        selected_card = self.saved_cards_var.get()
        if selected_card:
            parts = selected_card.split(' - ')
            if len(parts) == 4:
                card_id, _, cardholder_name, expiration_date = parts
                self.selected_card_id = int(card_id)
                messagebox.showinfo(
                    "Tarjeta seleccionada",
                    f"Tarjeta seleccionada: {cardholder_name}, Exp: {expiration_date}"
                )
            else:
                messagebox.showerror("Error", "Error al extraer los datos de la tarjeta")            
    def confirm_purchase(self):
        if hasattr(self, 'selected_card_id'):
            self.make_purchase(self.selected_card_id)
        else:
            messagebox.showerror("Error", "Por favor, seleccione una tarjeta para la compra")
            
    def make_purchase(self, card_id):
        try:
            cursor = self.conn.cursor()
            
            cursor.execute(
                """
                SELECT sc.product_code, p.price, sc.quantity
                FROM shopping_cart sc
                INNER JOIN products p ON sc.product_code = p.reference_code
                WHERE sc.user_id = %s;
                """, (self.user_id,)
            )
            cart_items = cursor.fetchall()
            
            if not cart_items:
                messagebox.showerror("Error", "No hay productos en el carrito de compras")
                return
            
            total_amount = sum(price * quantity for _, price, quantity in cart_items)
            
            sale_date = datetime.datetime.now()
            cursor.execute(
                """
                INSERT INTO sales (user_id, sale_date, total_amount, card_id)
                VALUES (%s, %s, %s, %s)
                """, (self.user_id, sale_date, total_amount, card_id)
            )
            self.conn.commit()
            sale_id = cursor.lastrowid
            
            for product_code, price, quantity in cart_items:
                subtotal = price * quantity
                
                cursor.execute(
                    """
                    INSERT INTO sale_details (sale_id, product_code, quantity, subtotal)
                    VALUES (%s, %s, %s, %s)
                    """, (sale_id, product_code, quantity, subtotal)
                )
                
                cursor.execute(
                    """
                    UPDATE products
                    SET stock = stock - %s
                    WHERE reference_code = %s
                    """, (quantity, product_code)
                )
                
            cursor.execute(
                """
                DELETE FROM shopping_cart
                WHERE user_id = %s;
                """, (self.user_id,)
            )
            
            self.create_bill(sale_id)
        
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error inesperado al realizar la compra: {e}")
        finally:
            cursor.close()