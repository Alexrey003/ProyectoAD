#======================================================================================
# Libraries
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from views import admin, products, register
from utils.config import APP_TITLE
from database.connection import connect_to_database
import hashlib

#=====================================================================================
#LOGING APPLICATION
class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
#======================================================================================
        # WINDOW PROPERTIES
        self.title(APP_TITLE + "Ventana Inicio v1.5")
        self.geometry("550x350+200+100")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#======================================================================================
        # LOGIN HEADING
        self.heading = Label(
            self,
            text="Inicio sesión.",
            font=('Bahnscrift', 15, 'bold'),
            bg="MediumPurple4",
            fg="white"
        )
        self.heading.pack(side="top")
        
#======================================================================================
        # FRAME WHERE THE ITEMS ARE GONNA BE
        self.login_frame = Frame(
            self,
            bg="gray20",
            width=530,
            height=300,
            bd=10
        )
        self.login_frame.pack(side="top")

#======================================================================================
        #LOGIN TITLE 2
        self.login_title_2 = Label(
            self,
            text="Ingrese sus credenciales:",
            font=('Bahnscrift', 13, 'bold'),
            bg="gray20",
            fg="white"
        )
        self.login_title_2.place(x=176, y=31)
        
#======================================================================================
        # USERNAME ITEMS
        # USERNAME ENTRY
        self.username_entry = Entry(
            self,
            width=25,
            font=('Bahnscrift', 12),
            fg="White",
            bg="gray19",
            bd=0
        )
        self.username_entry.place(x=150, y=80)
        self.username_entry.insert(0, "Nombre de usuario")

        # BIND ENVENTS FOR PLACEHOLDER HANDLING
        self.username_entry.bind("<FocusIn>", self.on_focus_in_username)
        self.username_entry.bind("<FocusOut>", self.on_focus_out_username)
        
        self.username_frame = Frame(self,
                                    width=250,
                                    height=2,
                                    bg="MediumPurple3").place(x=150, y=101)
        
#======================================================================================
        # PASSWORD ENTRY
        self.password_entry = Entry(
            self,
            width=25,
            font=('Bahnscrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        )
        self.password_entry.place(x=150, y=150)
        self.password_entry.insert(0, "Contraseña")

        # BIND EVENTS FOR PLACEHOLDER HANDLING
        self.password_entry.bind("<FocusIn>", self.on_focus_in_password)
        self.password_entry.bind("<FocusOut>", self.on_focus_out_password)
        
        self.password_frame = Frame(self,
                                    width=250,
                                    height=2,
                                    bg="MediumPurple3").place(x=150, y=171)
        
        # EYE BUTTON
        self.openeye = PhotoImage(file='assets/openeye.png')
        
        self.eye_btn = Button(self,
                            image=self.openeye,
                            bd=0,
                            bg="gray19",
                            activebackground="Slateblue1",
                            cursor='hand2',
                            command=self.hide
                            )
        self.eye_btn.place(x=375, y=148)
        
#=====================================================================================
        #Forget Button
        self.forget_btn = Button(self,
                            text="¿Olvidaste tu contraseña?",
                            font=('Bahnscrift', 13),
                            fg="white",
                            bd=0,
                            bg="MediumPurple3",
                            activebackground="Slateblue1",
                            cursor='hand2',
                            relief="solid",
                            command = self.forgot_password_window
                            )
        self.forget_btn.place(x=40, y=270)
        
#====================================================================================
        #Register Button
        self.register_btn = Button(self,
                                text='Registrate',
                                font=('Bahnscrift', 13),
                                fg="white",
                                bd=0,
                                bg="MediumPurple3",
                                cursor='hand2',
                                activebackground="Slateblue1",
                                command= self.open_register_window,
                                relief="solid"
                                )
        self.register_btn.place(x=330, y=270)
        
#=====================================================================================
        #Login Button
        self.login_btn = Button(self,
                            text='Iniciar Sesión',
                            font=("Bahnschrift", 13, 'bold'),
                            fg="white",
                            bg="MediumPurple3",
                            activebackground="Slateblue1",
                            cursor='hand2',
                            command = self.login,
                            relief="solid",
                            bd=0
                            )
        self.login_btn.place(x=215, y=200)
        
#=======  METHODS  ==============================================================================
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
        
        register_window = register.RegisterWindow(on_close_callback=reopen_login_window)
        register_window.protocol("WM_DELETE_WINDOW", reopen_login_window)
        register_window.mainloop()
    def on_register_close(self):
        self.deiconify()
    
    def login(self):
        # GET THE USERNAME AND PASSWORD FROM THE ENTRIES
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        
        # HASH THE PASSWORD FOR SECURITY PURPOSES
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        
        # CONNECT TO THE DATABASE
        conn = connect_to_database()
        cursor = conn.cursor()
        
        try:
            # QUERY THAT HELPS TO THE LOGIN PAGE
            cursor.execute(
                "SELECT user_id, rol FROM users WHERE username=%s AND password=%s", (self.username, hashed_password)
            )
            self.resultado = cursor.fetchone()
            
            # LOGIC TO KNOW IF THE USER IS A CLIENT OR AN ADMIN
            if self.resultado:
                user_id, rol = self.resultado
                if rol == 'admin':
                    # OPEN ADMIN WINDOW
                    admin_window = admin.AdminWindow()
                    self.destroy()
                    admin_window.mainloop()
                elif rol == 'client':
                    # OPEN CLIENT WINDOW
                    client_window = products.ProductsWindow(user_id=user_id)
                    self.destroy()
                    client_window.mainloop()
            else:
                messagebox.showerror("Error: ", "Usuario o contraseña incorrecta")
        except Exception as e:
            messagebox.showerror("Error:", f"Error al iniciar sesion {e}")
        finally:
            conn.close()
            cursor.close()
        
    def forgot_password_window(self):
        from views.forgot_password import ForgotPasswordWindow
        
        self.destroy()
        
        forgot_password_window = ForgotPasswordWindow()
        forgot_password_window.mainloop()