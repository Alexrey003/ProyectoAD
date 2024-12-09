#===================================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from utils.config import APP_TITLE
from database.connection import connect_to_database

#===================================================================================
# PROFILE APPLICATION
class ProfileWindow(Tk):
    def __init__(self, user_id,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.conn = connect_to_database()
        cursor = self.conn.cursor()
        
        cursor.execute(
            """
            SELECT name, lastname, direction, phone, email, username
            FROM users
            WHERE user_id = %s
            """, (self.user_id,)
        )
        row = cursor.fetchone()
        
        if row:
            self.user_information = {
                'name': row[0] if row[0] else "No se pudo cargar...",
                'lastname': row[1] if row[1] else "No se pudo cargar...",
                'direction': row[2] if row[2] else "No se pudo cargar...",
                'phone': row[3] if row[3] else "No se pudo cargar...",
                'email': row[4] if row[4] else "No se pudo cargar...",
                'username': row[5] if row[5] else "No se pudo cargar...",
            }
        else:
            self.user_information = {
                'name': "No se pudo cargar...",
                'lastname': "No se pudo cargar...",
                'direction': "No se pudo cargar...",
                'phone': "No se pudo cargar...",
                'email': "No se pudo cargar...",
                'username': "No se pudo cargar...",
            }
        cursor.close()
#===================================================================================
        # WINDOW PROPERTIES
        self.title(APP_TITLE + "Información de perfil v1.5")
        self.geometry('800x650+150+20')
        self.resizable(False, False)
        self.configure(background='MediumPurple4')
        
#===================================================================================
        # HEADING CONFIG
        self.heading_label = Label(
            self,
            text="Información de Perfil",
            font=("Bahnschrift", 20, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        self.heading_label.place(x=15, y=10)
        
        self.heading_label_2 = Label(
            self,
            text="Esta ventana te muestra tus datos personales y podras modificarlos si asi lo deseas.",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        self.heading_label_2.place(x=15, y=50)
        
        self.go_back_btn = Button(
            self,
            text="Atras",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnschrift', 15, 'bold'),
            relief="solid",
            bd=0,
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.go_back
        )
        self.go_back_btn.place(x=700, y=50)
        
#===================================================================================
        # USER INFO CONFIG
        #MAIN FRAME
        self.main_frame = Frame(
            self,
            bg="gray20",
            width=780,
            height=580,
        )
        self.main_frame.place(x=20, y=100)
        
#=========================================================================================
        # NAME CONFIG
        self.name_info_label = Label(
            self.main_frame,
            text=f"Nombre: {self.user_information['name']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.name_info_label.place(x=30, y=20)
        
        #NAME FRAME
        self.name_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.name_frame.place(x=-1, y=50)
        
#=========================================================================================
        # LASTNAME CONFIG
        self.lastname_info_label = Label(
            self.main_frame,
            text=f"Apellido: {self.user_information['lastname']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.lastname_info_label.place(x=30, y=100)
        
        self.lastname_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.lastname_frame.place(x=-1, y=130)
        
#===========================================================================================
        # DIRECTION CONFIG
        self.direction_info_label = Label(
            self.main_frame,
            text=f"Dirección: {self.user_information['direction']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.direction_info_label.place(x=30, y=180)
        
        self.direction_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.direction_frame.place(x=-1, y=210)
        
#================================================================================================
        # PHONE CONFIG
        self.phone_info_label = Label(
            self.main_frame,
            text=f"Teléfono: {self.user_information['phone']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.phone_info_label.place(x=30, y=260)
        
        self.phone_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.phone_frame.place(x=-1, y=290)
        
#===============================================================================================
        # EMAIL CONFIG
        self.email_info_label = Label(
            self.main_frame,
            text=f"Correo Electrónico: {self.user_information['email']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.email_info_label.place(x=30, y=340)
        
        self.email_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.email_frame.place(x=-1, y=370)
        
#===============================================================================================
        # USERNAME CONFIG
        self.username_info_label = Label(
            self.main_frame,
            text=f"Nombre de usuario: {self.user_information['username']}",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.username_info_label.place(x=30, y=420)
        
        self.username_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.username_frame.place(x=-1, y=450)
        
#===============================================================================================
        self.password_info_label = Label(
            self.main_frame,
            text="Contraseña: ************",
            font=("Bahnschrift", 15, "bold"),
            bg="gray19",
            fg="white",
        )
        self.password_info_label.place(x=30, y=500)
        
        self.password_frame = Frame(
            self.main_frame,
            width=750,
            height=2,
            bg="MediumPurple3"
        )
        self.password_frame.place(x=-1, y=530)
        
#===============================================================================================
        # BUTTONS CONFIG
        # DIRECTION EDIT
        self.edit_direction_button = Button(
            self.main_frame,
            text="Editar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=15,
            command=self.edit_direction,
        )
        self.edit_direction_button.place(x=600, y=178)
        
#================================================================================================
        # PHONE EDIT
        self.edit_phone_button = Button(
            self.main_frame,
            text="Editar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=15,
            command=self.edit_phone,
        )
        self.edit_phone_button.place(x=600, y=258)
        
#===============================================================================================
        # EMAIL EDIT
        self.edit_email_button = Button(
            self.main_frame,
            text="Editar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=15,
            command=self.edit_email,
        )
        self.edit_email_button.place(x=600, y=338)
        
#===============================================================================================
        # USERNAME EDIT
        self.edit_username_button = Button(
            self.main_frame,
            text="Editar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=15,
            command=self.edit_username,
        )
        self.edit_username_button.place(x=600, y=418)
        
#===============================================================================================
        # PASSWORD EDIT
        self.edit_password_button = Button(
            self.main_frame,
            text="Editar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=15,
            command=self.edit_password,
        )
        self.edit_password_button.place(x=600, y=498)
        
#====  METHODS  ==============================================================================
    def edit_direction(self):
        self.open_update_window("Dirección", "direction")
    
    def edit_phone(self):
        self.open_update_window("Teléfono", "phone")
    
    def edit_email(self):
        self.open_update_window("Correo Electrónico", "email")    
    def edit_username(self):
        self.open_update_window("Nombre de Usuario", "username")
    def edit_password(self):
        self.open_update_window("Contraseña", "password", masked=True)
        
    def open_update_window(self, label, field, masked=False):
        subwindow = Toplevel(self)
        subwindow.geometry("700x200")
        subwindow.title(f"Editar {label}")
        subwindow.configure(bg="MediumPurple4")
        
        field_label = Label(
            subwindow,
            text=f"Ingrese el nuevo {label.lower()}:",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        field_label.place(x=10, y=50)
        
        entry_options = {
            "font": ("Bahnschrift", 12),
            "bg": "gray19",
            "fg": "white",
            "width": 30,
        }
        if masked:
            entry_options["show"] = "*"
        
        new_field_entry = Entry(subwindow, **entry_options)
        new_field_entry.place(x=270, y=50)
        
        confirm_button = Button(
            subwindow,
            text="Confirmar",
            font=("Bahnschrift", 13, "bold"),
            bg="MediumPurple3",
            fg="white",
            bd=0,
            relief="solid",
            cursor="hand2",
            activebackground="SlateBlue1",
            width=10,
            command=lambda: self.update_field(field, new_field_entry.get(), subwindow),
        )
        confirm_button.place(x=250, y=150)
        
    def update_field(self, field, new_value, subwindow):
        import hashlib
        if not new_value.strip():
            messagebox.showwarning("Error", f"El campo {field} no puede estar vacio.")
            return
        
        if field == "password":
            new_value = hashlib.sha256(new_value.encode()).hexdigest()

        question = messagebox.askquestion("Confirmación", f"¿Está seguro de cambiar su {field}?")
        if question == "yes":
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE users SET {field} = %s WHERE user_id = %s",
                        (new_value, self.user_id)
                    )
                    self.conn.commit()
                    
                messagebox.showinfo("Éxito", f"Se ha actualizado el {field} correctamente.")
                
                if hasattr(self, f"{field}_info_label"):
                    if field == "password":
                        label_value = "****************"
                    else:
                        label_value = new_value
                        
                    getattr(self, f"{field}_info_label").config(text=f"{field.capitalize()}: {label_value}")
                subwindow.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un error al intentar actualizar el {field}.\nError: {str(e)}")
        else:
            subwindow.lift()

    def go_back(self):
        from views.products import ProductsWindow
        self.destroy()
        product_window = ProductsWindow(user_id=self.user_id)
        product_window.mainloop()