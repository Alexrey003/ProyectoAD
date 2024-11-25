# Libraries
from tkinter import *
from PIL import ImageTk
from views.register import RegisterWindow
from utils.config import APP_TITLE, APP_BG, FONT_HEADING, FONT_MAIN

#================================================================
class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set window properties
        self.title(APP_TITLE + "Ventana Inicio v1.0")
        self.configure(bg=APP_BG)
        self.resizable(False, False)

        # Load background image
        try:
            self.bg_image = ImageTk.PhotoImage(file='assets/bg.jpg')
        except FileNotFoundError:
            print("Background image not found! Using fallback color.")
            self.bg_image = None

        if self.bg_image:
            self.bg_label = Label(self, image=self.bg_image)
            self.bg_label.pack(fill=BOTH, expand=True)
        else:
            self.configure(bg="gray")

        # Login label heading
        self.heading = Label(
            self,
            text="Inicio sesión",
            font=FONT_HEADING,
            bg="gray1",
            fg="SlateBlue1"
        )
        self.heading.place(x=20, y=20)

        # Entry for username
        self.username_entry = Entry(
            self,
            width=25,
            font=FONT_MAIN,
            fg="dark slate blue",
            bg="gray1",
            bd=0
        )
        self.username_entry.place(x=20, y=80)
        self.username_entry.insert(0, "Nombre de usuario")

        # Bind events for placeholder handling
        self.username_entry.bind("<FocusIn>", self.on_focus_in_username)
        self.username_entry.bind("<FocusOut>", self.on_focus_out_username)
        
        self.username_frame = Frame(self,
                                    width=250,
                                    height=2,
                                    bg="Slateblue1").place(x=20, y=101)
        
        #Entry password
        self.password_entry = Entry(
            self,
            width=25,
            font=FONT_MAIN,
            fg="dark slate blue",
            bg="gray1",
            bd=0
        )
        self.password_entry.place(x=20, y=150)
        self.password_entry.insert(0, "Contraseña")

        # Bind events for placeholder handling
        self.password_entry.bind("<FocusIn>", self.on_focus_in_password)
        self.password_entry.bind("<FocusOut>", self.on_focus_out_password)
        
        self.password_frame = Frame(self,
                                    width=250,
                                    height=2,
                                    bg="Slateblue1").place(x=20, y=171)
        
        # Eye Buttons
        self.openeye = PhotoImage(file='assets/openeye.png')
        
        self.eye_btn = Button(self,
                            image=self.openeye,
                            bd=0,
                            bg="black",
                            activebackground="Slateblue1",
                            cursor='hand2',
                            command=self.hide
                            )
        self.eye_btn.place(x=245, y=148)
        
        #Forget Button
        self.forget_btn = Button(self,
                            text="¿Olvidaste tu contraseña?",
                            font=FONT_MAIN,
                            fg="SlateBlue1",
                            bd=0,
                            bg="black",
                            activebackground="Slateblue1",
                            cursor='hand2'
                            #command = Aqui se debe poner la accion de llevar a la página de olvidar contraseña
                            )
        self.forget_btn.place(x=20, y=180)
        
        #Register Button
        self.register_btn = Button(self,
                                text='Registrate',
                                font=FONT_MAIN,
                                fg="SlateBlue1",
                                bd=0,
                                bg="black",
                                cursor='hand2',
                                activebackground="Slateblue1",
                                command= self.open_register_window
                                )
        self.register_btn.place(x=250, y=180)
        
        #Login Button
        self.login_btn = Button(self,
                            text='Iniciar Sesión',
                            font=("Bahnschrift",15, 'bold'),
                            fg="SlateBlue1",
                            bg="black",
                            activebackground="Slateblue1",
                            cursor='hand2',
                            #command = Aqui se debe poner la accion de llevar a la página de inicio de sesión
                            )
        self.login_btn.place(x=95, y=220)
        
#=====================================================================================
    # Placeholder logic for username
    def on_focus_in_username(self, event):
        if self.username_entry.get() == "Nombre de usuario":
            self.username_entry.delete(0, END)

    def on_focus_out_username(self, event):
        if self.username_entry.get().strip() == "":
            self.username_entry.insert(0, "Nombre de usuario")
            
    # Placeholder logic for password
    def on_focus_in_password(self, event):
        if self.password_entry.get() == "Contraseña":
            self.password_entry.delete(0, END)

    def on_focus_out_password(self, event):
        if self.password_entry.get().strip() == "":
            self.password_entry.insert(0, "Contraseña")

    def hide(self):
        self.openeye.config(file='assets/closeye.png')
        self.password_entry.config(show='*')
        self.eye_btn.config(command=self.show)
    
    def show(self):
        self.openeye.config(file='assets/openeye.png')
        self.password_entry.config(show='')
        self.eye_btn.config(command=self.hide)
    
    # Method to open de register window
    def open_register_window(self):
        self.withdraw()
        
        def reopen_login_window():
            self.deiconify()
        
        register_window = RegisterWindow(on_close_callback=reopen_login_window)
        register_window.protocol("WM_DELETE_WINDOW", reopen_login_window)
        register_window.mainloop()
    def on_register_close(self):
        self.deiconify()
