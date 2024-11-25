#Libraries
from tkinter import *
from PIL import ImageTk
from utils.config import APP_TITLE, APP_BG, FONT_HEADING, FONT_MAIN
from controllers.auth_controller import register_user
from tkinter import messagebox

#============================================================================
class RegisterWindow(Toplevel):
# INTERFACE
    def __init__(self, on_close_callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.on_close_callback = on_close_callback
        
        # Window properties
        self.title(APP_TITLE + "Ventana registro v1.0")
        self.geometry("500x670+120+20")
        self.configure(bg=APP_BG)
        self.resizable(False, False)
        
        # Load background image
        try:
            self.bg_image = ImageTk.PhotoImage(file='assets/registerbg.jpg')
        except FileNotFoundError:
            print("Background image not found! Using default background color.")
            self.bg_image = None
        
        if self.bg_image:
            self.bg_label = Label(self, image=self.bg_image)
            self.bg_label.pack(fill=BOTH, expand=True)
        else:
            self.configure(bg='gray')
        
        # Register heading
        self.register_heading = Label(
            self,
            text="Crea una cuenta",
            font=FONT_HEADING,
            bg='gray60',
            fg='black',
            width=29
        )
        self.register_heading.place(x=1, y=20)
        
        # Entries fields
        
        #Name field
        self.name_label = Label(
            self,
            text="Nombre:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.name_label.place(x=10, y=100)
        
        self.name_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.name_entry.place(x=15, y=135)
        
        #Lastname field
        self.lastname_label = Label(
            self,
            text="Apellidos:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.lastname_label.place(x=10, y=170)
        
        self.lastname_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.lastname_entry.place(x=15, y=205)
        
        #Direction field
        self.direction_label = Label(
            self,
            text="Dirección:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.direction_label.place(x=10, y=240)
        
        self.direction_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.direction_entry.place(x=15, y=275)
        
        #Phone field
        self.phone_label = Label(
            self,
            text="Teléfono:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.phone_label.place(x=10, y=310)
        
        self.phone_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.phone_entry.place(x=15, y=345)
        
        #Email field
        self.email_label = Label(
            self,
            text="Correo electrónico:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.email_label.place(x=10, y=380)
        
        self.email_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.email_entry.place(x=15, y=415)
        
        #Username field
        self.username_label = Label(
            self,
            text="Nombre de usuario:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.username_label.place(x=10, y=450)
        
        self.username_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64"
        )
        self.username_entry.place(x=15, y=485)
        
        #Password field
        self.password_label = Label(
            self,
            text="Contraseña:",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg="gray73",
        )
        self.password_label.place(x=10, y=520)
        
        self.password_entry = Entry(
            self,
            width=35,
            font=FONT_MAIN,
            fg="black",
            bg="gray64",
        )
        self.password_entry.place(x=15, y=555)
        
        #Sent button
        self.sent_btn = Button(
            self,
            text="Enviar",
            font=("Bahnschrift", 15, 'bold'),
            fg='black',
            bg='gray60',
            width=25,
            command= self.on_register_complete
        )
        self.sent_btn.place(x=100, y=600)
    
#======================================================================
# METHODS
    def on_register_complete(self):
        try:
            # Proceed with registration
            result = register_user(
                str(self.name_entry.get()),
                str(self.lastname_entry.get()),
                str(self.direction_entry.get()),
                str(self.phone_entry.get()),  # Phone as a numeric string
                str(self.email_entry.get()),
                str(self.username_entry.get()),
                str(self.password_entry.get()),
            )
            messagebox.showinfo("Registro", result)
            
            if "exitosamente" in result:
                self.destroy()
                if self.on_close_callback:
                    self.on_close_callback()

        except ValueError as ve:
            messagebox.showerror("Error de Validación", str(ve))
