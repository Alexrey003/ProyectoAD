#============================================================================
#Libraries
from tkinter import *
from PIL import ImageTk
from utils.config import APP_TITLE
from controllers.auth_controller import register_user
from tkinter import messagebox

#============================================================================
# REGISTER APPLICATION
class RegisterWindow(Toplevel):
    def __init__(self, on_close_callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
#=============================================================================
        self.on_close_callback = on_close_callback
        
        # WINDOW PROPERTIES
        self.title(APP_TITLE + "Ventana registro v1.5")
        self.geometry("530x620+120+20")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#=============================================================================
        # REGISTER HEADING
        # REGISTER TOP FRAME
        self.register_top_frame = Frame(
            self,
            bg="MediumPurple4",
            width=500,
            height=80
        )
        self.register_top_frame.pack(side="top")
        
        # REGISTER TITLE 
        self.register_label = Label(
            self,
            text="Crea una cuenta.",
            font=('Bahnscrift', 15, 'bold'),
            bg='MediumPurple4',
            fg='white',
            width=29
        )
        self.register_label.place(x=-90, y=5)
        
        # REGISTER TOP LABEL 2
        self.register_text = Label(
            self,
            text="Complete los siguientes campos para tener acceso a nuestro sito!",
            font=('Bahnschrift', 10, 'bold'),
            bg='MediumPurple4',
            fg='white',
            width=65
        )
        self.register_text.place(x=-35, y=45)
#==============================================================================
        #REGISTER FORM
        #REGISTER FORM FRAME
        self.register_form_frame = Frame(
            self,
            bg="gray20",
            width=515,
            height=530
        )
        self.register_form_frame.pack(side="top")
        
#==============================================================================
        #NAME ITEMS
        self.name_label = Label(
            self,
            text="Nombre:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.name_label.place(x=20, y=95)
        
        self.name_entry = Entry(
            self,
            width=35,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.name_entry.place(x=93, y=99)
        
        self.name_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=93, y=118)
#==============================================================================
        # LASTNAME ITEMS
        self.lastname_label = Label(
            self,
            text="Apellidos:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.lastname_label.place(x=20, y=150)
        
        self.lastname_entry = Entry(
            self,
            width=35,
            font=('Bahnscrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.lastname_entry.place(x=99, y=154)
        
        self.lastname_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
            ).place(x=99, y=174)
#===============================================================================
        # DIRECTION ITEMS
        self.direction_label = Label(
            self,
            text="Dirección:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.direction_label.place(x=20, y=210)
        
        self.direction_entry = Entry(
            self,
            width=35,
            font=('Bahnscrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.direction_entry.place(x=101, y=210.5)
        
        self.direction_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=101, y=230)
#===============================================================================
        # PHONE ITEMS
        self.phone_label = Label(
            self,
            text="Teléfono:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.phone_label.place(x=20, y=270)
        
        self.phone_entry = Entry(
            self,
            width=35,
            font=('Bahsnachrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.phone_entry.place(x=99, y=272)
        
        self.phone_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=99, y=292)
#===================================================================================
        #Email field
        self.email_label = Label(
            self,
            text="Correo electrónico:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.email_label.place(x=20, y=335)
        
        self.email_entry = Entry(
            self,
            width=35,
            font=('Bahsnachrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.email_entry.place(x=170, y=337)
        
        self.email_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=170, y=357)
#===================================================================================
        #Username field
        self.username_label = Label(
            self,
            text="Nombre de usuario:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.username_label.place(x=20, y=400)
        
        self.username_entry = Entry(
            self,
            width=35,
            font=('Bahsnachrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.username_entry.place(x=175, y=402)
        
        self.username_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=175, y=423)
#===================================================================================
        #Password field
        self.password_label = Label(
            self,
            text="Contraseña:",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg="gray20",
        )
        self.password_label.place(x=20, y=460)
        
        self.password_entry = Entry(
            self,
            width=35,
            font=('Bahsnachrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.password_entry.place(x=119, y=462)
        
        self.password_frame = Frame(
            self,
            width=330,
            height=2,
            bg="MediumPurple3"
        ).place(x=119, y=483)
#===================================================================================
        #Sent button
        self.sent_btn = Button(
            self,
            text="Enviar",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg='MediumPurple3',
            activebackground="SlateBlue1",
            command= self.on_register_complete,
            width=20
        )
        self.sent_btn.place(x=165, y=520)
    
#========== METHODS ============================================================
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
