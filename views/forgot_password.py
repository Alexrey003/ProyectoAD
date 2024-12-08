#===================================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from utils.config import APP_TITLE
import hashlib

#===================================================================================
# FORGOT PASSWORD APPLICATION
class ForgotPasswordWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
#===================================================================================
        # WINDOWS PROPERTIES
        self.title(APP_TITLE + "Recuperar contraseña v1.5")
        self.geometry("700x430+150+20")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#===================================================================================
        # HEADING ITEMS
        self.heading_title = Label(
            self,
            text="Olvidaste tu contraseña",
            font=('Bahnscrift', 15, 'bold'),
            fg="white",
            bg="MediumPurple4"
        )
        self.heading_title.place(x=15, y=20)
        
        self.heading_subtitle = Label(
            self,
            text="Para recuperar tu contraseña completa la siguiente información.",
            font=('Bahnscrift', 13, 'bold'),
            fg="white",
            bg="MediumPurple4"
        )
        self.heading_subtitle.place(x=15, y=50)
        
#===================================================================================
        # FRAME WHERE THE INFORMATION IS GONNA BE
        self.frame1 = Frame(
            self,
            bg="gray20",
            width=770,
            height=550
        )
        self.frame1.place(x=15, y=80)
        
#===================================================================================
        # FIELDS FOR RESTORE THE PASSWORD
        # PHONE ITEMS
        self.phone_label = Label(
            self.frame1,
            text="Teléfono vinculado a tu cuenta:",
            font=('Bahnschrift', 13, 'bold'),
            fg="white",
            bg="gray19"
        )
        self.phone_label.place(x=20, y=70)
        
        self.phone_entry = Entry(
            self.frame1,
            width=20,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
            # textvariable=self.phone
        )
        self.phone_entry.place(x=260, y=73)
        
        self.password_frame = Frame(
            self.frame1,
            width=230,
            height=2,
            bg="MediumPurple3"
            
        ).place(x=260, y=95)
        
#===================================================================================
        # EMAIL ITEMS
        self.email_label = Label(
            self.frame1,
            text="Correo electrónico vinculado a tu cuenta:",
            font=('Bahnschrift', 13, 'bold'),
            fg="white",
            bg="gray19"
        )
        self.email_label.place(x=20, y=130)
        
        self.email_entry = Entry(
            self.frame1,
            width=20,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
            # textvariable=self.email
        )
        self.email_entry.place(x=340, y=133)
        
        self.email_frame = Frame(
            self.frame1,
            width=230,
            height=2,
            bg="MediumPurple3"
        ).place(x=340, y=155)
        
#===================================================================================
        # USERNAME ITEMS
        self.username_label = Label(
            self.frame1,
            text="Nombre de usuario vinculado a tu cuenta:",
            font=('Bahnschrift', 13, 'bold'),
            fg="white",
            bg="gray19"
        )
        self.username_label.place(x=20, y=190)
        
        self.username_entry = Entry(
            self.frame1,
            width=20,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
            # textvariable=self.username
        )
        self.username_entry.place(x=345, y=193)
        
        self.username_frame = Frame(
            self.frame1,
            width=230,
            height=2,
            bg="MediumPurple3"
        ).place(x=345, y=213)
        
#===================================================================================
        # VALIDATION BUTTON
        self.validate_button = Button(
            self.frame1,
            text="Validar tus datos",
            font=('Bahnschrift', 12, 'bold'),
            fg="white",
            bg="MediumPurple3",
            activebackground="SlateBlue1",
            width=15,
            cursor="hand2",
            relief="solid",
            bd=0,
            command=self.validate_data
        )
        self.validate_button.place(x=430, y=250)
        
#=====  METHODS  ==============================================================================
    def validate_data(self):
        from database.connection import connect_to_database
        
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT user_id
                FROM users
                WHERE phone=%s AND email=%s AND username=%s
                """, (phone, email, username)
            )
            result = cursor.fetchone()
            
            if result:
                messagebox.showinfo("Éxito: ", "Datos validados correctamente.")
                self.open_reset_password_window(result[0])
            else:
                messagebox.showinfo("Error", "Datos incorrectos.\nPorfavor intenta de nuevo.")
        except Exception as e:
            messagebox.showerror("Error:", f"Error al validar los datos: {e}")
        finally:
            cursor.close()
            conn.close()
    
#==============================================================================================
    def open_reset_password_window(self, user_id):
        #WINDOWS PROPERTIES
        reset_window = Toplevel(self)
        reset_window.title("Restableces contraseña")
        reset_window.geometry("400x200")
        reset_window.configure(bg="MediumPurple4")
        
        # frame_1 = Frame(
        #     reset_window,
        #     bg="gray20",
        #     width=380,
        #     height=180
        # ).place(x=15, y=50)
        
        new_password_label = Label(
            reset_window,
            text="Nueva contraseña:",
            font=('Bahnscrift', 12, 'bold'),
            fg="white",
            bg="gray19"
        )
        new_password_label.place(x=20, y=50)
        
        new_password_entry = Entry(
            reset_window,
            width=25,
            font=('Bahnscrift', 12),
            fg="white",
            bg="gray19",
            bd=0,
            show="*"
        )
        new_password_entry.place(x=180, y=53)
        
        new_password_frame = Frame(
            reset_window,
            width=230,
            height=2,
            bg="MediumPurple3"
        )
        new_password_frame.place(x=180, y=73)
        
        confirm_btn = Button(
            reset_window,
            text="Confirmar",
            font=('Bahnscrift', 12, 'bold'),
            fg="white",
            bg="MediumPurple3",
            activebackground="SlateBlue1",
            width=15,
            cursor="hand2",
            relief="solid",
            bd=0,
            command=lambda: self.update_password(user_id, new_password_entry.get())
        )
        confirm_btn.place(x=150, y=120)
        
    def update_password(self, user_id, new_password):
        from database.connection import connect_to_database
        from views.login import LoginWindow
        
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            cursor.execute(
                """
                UPDATE users
                SET password=%s
                WHERE user_id=%s
                """, (hashed_password, user_id)
            )
            conn.commit()
            messagebox.showinfo("Éxito: ", "Contraseña restablecida correctamente.")
            self.destroy()
            login_window = LoginWindow()
            login_window.mainloop()
        except Exception as e:
            messagebox.showerror("Error:", f"Error al restablecer la contraseña: {e}")
        finally:
            cursor.close()
            conn.close()