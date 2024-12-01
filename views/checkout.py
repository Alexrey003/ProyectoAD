#LIBRARIES
from tkinter import *

#================================================================
class CheckOut(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #WINDOWS PROPERTIES
        self.title("Ventana de pago v1.0")
        self.geometry("800x650+180+50")
        self.configure(bg="black")
        self.resizable(False, False)
        
        #FRAME HEADING
        self.heading_frame = Frame(
            self,
            bg="gray60",
            width=800,
            height=100
        )
        self.heading_frame.pack(side="top")
        
        self.heading_title = Label(
            self.heading_frame,
            text="Ventana de pago",
            fg="black",
            font=('Bahnscrift', 23),
            bg="gray63"
        )
        self.heading_title.place(x=10, y=50)
        
        #JUMPING OUT FROM DE CHECKOUT WINDOW BUTTON
        self.goback_btn = Button(
            self.heading_frame,
            text="Atras",
            bg="gray70",
            #command=
        )
        self.goback_btn.place(x=10, y=10)
        
        #CHECKOUT FIELDS
        self.card_number_label = Label(
            self,
            text="Numero de tarjeta:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray63",
            fg="black"
        )
        self.card_number_label.place(x=25, y=150)

if __name__ == "__main__":
    app = CheckOut()
    app.mainloop()