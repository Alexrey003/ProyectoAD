#=================================================================
#LIBRARIES
from tkinter import *
from utils.config import APP_TITLE

#================================================================
class CheckOut(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
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
            font=('Bahnscrift', 15, 'bold'),
            bg="MediumPurple4"
        )
        self.heading_title.place(x=50, y=10)
#==================================================================
        #JUMPING OUT FROM DE CHECKOUT WINDOW BUTTON
        self.goback_btn = Button(
            self.heading_frame,
            text="Atras",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 10),
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.go_back
        )
        self.goback_btn.place(x=10, y=10)
#=================================================================
        #CHECKOUT FIELDS
        #CHECKOUT FRAME
        self.checkout_frame = Frame(
            self,
            bg="gray73",
            width=800,
            height=500,
            bd=10
        )
        self.checkout_frame.pack(side="top")
        
        #INTRODUCTION LABEL
        self.intro_label = Label(
            self,
            text="Introduzca los detalles de su tarjeta de credito.",
            font=('Bahnscrift', 15, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.intro_label.place(y=100)
        
        #CARD NUMBER ITEMS
        self.card_number_label = Label(
            self,
            text="Numero de tarjeta:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.card_number_label.place(x=25, y=150)
        
        self.card_number_entry = Entry(
            self,
            width=20,
            font=("Bahnscrift", 13, 'bold'),
            fg="black",
            bg="gray64"
        )
        self.card_number_entry.place(x=180, y=150)
        
        #NAME OF THE OWNER ITEMS
        self.name_owner_label = Label(
            self,
            text="Nombre del propietario:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.name_owner_label.place(x=380, y=150)
        
        self.name_owner_entry = Entry(
            self,
            width=20,
            font=("Bahnscrift", 13, 'bold'),
            fg="black",
            bg="gray64"
        )
        self.name_owner_entry.place(x=575, y=150)
        
        #EXPIRATION DATE ITEMS
        self.expiration_date_label = Label(
            self,
            text="Fecha de expiración:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.expiration_date_label.place(x=25, y=280)
        
        self.expiration_date_entry = Entry(
            self,
            width=10,
            font=("Bahnscrift", 13, 'bold'),
            fg="black",
            bg="gray64"
        )
        self.expiration_date_entry.place(x=196, y=280)
        
        #CCV ITEMS
        self.ccv_label = Label(
            self,
            text="CVV:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.ccv_label.place(x=380, y=280)
        
        self.ccv_entry = Entry(
            self,
            width=5,
            font=("Bahnscrift", 13, 'bold'),
            fg="black",
            bg="gray64"
        )
        self.ccv_entry.place(x=428, y=280)
#=======  METHODS   ===========================================================
    def go_back(self):
        from views.shopping_cart import ShoppingCartWindow
        self.destroy()
        shopping_cart_window = ShoppingCartWindow(self.user_id)
        shopping_cart_window.mainloop()