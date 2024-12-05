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

        self.name_label = Label(
            self,
            text=f"Nombre: {self.user_info['name']} {self.user_info['lastname']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.name_label.place(x=15, y=350)

        self.phone_label = Label(
            self,
            text=f"Telefono: {self.user_info['phone']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.phone_label.place(x=15, y=400)

        self.direction_label = Label(
            self,
            text=f"Direcciòn: {self.user_info['direction']}",
            fg="white",
            bg="gray19",
            font=("Bahnscrift", 13, 'bold')
        )
        self.direction_label.place(x=15, y=450)

        # ACCEPT BUTTON
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
        )
        self.proceed_btn.place(x=460, y=550)

        self.submit_card =  Button(
            self,
            text="Añadir tarjeta",
            font=('Bahnscrift', 13, 'bold'),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.linking_card
        )
        self.submit_card.place(x=250, y=550)
#=======  METHODS   ===========================================================
    def go_back(self):
        from views.shopping_cart import ShoppingCartWindow
        self.destroy()
        shopping_cart_window = ShoppingCartWindow(self.user_id)
        shopping_cart_window.mainloop()
    
    def linking_card(self):
        try:
            selected_month = self.expiration_month_var.get()
            selected_year = self.expiration_year_var.get()
            
            if selected_month == 'MM' or selected_year == 'YY':
                messagebox.showerror("Error", "Por favor, seleccione la fecha de expiración.")
                return
            
            expiration_date = f"{selected_month}/{selected_year}"
            
            result = register_card(
                self.user_id,
                self.card_number_entry.get(),
                self.name_owner_entry.get(),
                expiration_date,
                self.ccv_entry.get()
            )
            if "correctamente" in result:
                messagebox.showinfo("Exito", result)
            else:
                messagebox.showerror("Error", result)
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")