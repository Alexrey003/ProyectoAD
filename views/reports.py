#===================================================================================
# LIBRARIES
from tkinter import *
from utils.config import APP_TITLE
from database.connection import connect_to_database

#===================================================================================
# REPORT AND SUGGESTIONS APPLICATION
class ReportAndSuggestionsUsersWindow(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.user_id = user_id
        
        self.conn = connect_to_database()
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT username FROM users WHERE user_id=%s", (self.user_id,))
        result = cursor.fetchone()
        
        if result:
            self.username_info = {
                "username" : result[0] if result[0] else "...",
            }
        else:
            self.username_info = {
                "username" : "...",
            }
        cursor.close()
#====================================================================================
        # WINDOW MAIN PROPERTIES
        self.title(APP_TITLE + "Reportes y sugerencias v1.5")
        self.geometry("750x450+200+100")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#====================================================================================
        # ADMIN HEADING
        self.user_heading = Label(
            self,
            text=f"Bienvenido usuario: {self.username_info['username']}",
            font=('Bahnschrift', 15, 'bold'),
            bg="MediumPurple4",
            fg="white"
        )
        self.user_heading.place(x=10, y=10)
        
        self.user_heading_text = Label(
            self,
            text="Aqui podras enviar reportes y sugerencias a los desarrolladores.",
            fg="white",
            bg="MediumPurple4",
            font=('Bahnschrift', 13, 'bold')
        )
        self.user_heading_text.place(x=10, y=40)
        
        self.go_back_btn = Button(
            self,
            text="Atras",
            font=('Bahnschrift', 13, 'bold'),
            bg="MediumPurple3",
            fg="white",
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            command=self.go_back
        )
        self.go_back_btn.place(x=580, y=25)
        
        self.send_button = Button(
            self,
            text="Enviar",
            font=('Bahnschrift', 13, 'bold'),
            bg="MediumPurple3",
            fg="white",
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            command=self.send_data
        )
        self.send_button.place(x=650, y=25)
        
#====================================================================================
        # CONTENT
        self.main_frame = Frame(
            self,
            width=725,
            height=375,
            bg="gray19"
            
        )
        self.main_frame.place(x=15, y=70)
#==================================================================================
        self.report_suggestion_title_label = Label(
            self.main_frame,
            text="Titulo:",
            font=('Bahnschrift', 13, 'bold'),
            bg="gray20",
            fg="white"
        )
        self.report_suggestion_title_label.place(x=25, y=20)
        
        self.report_suggestion_title_entry = Entry(
            self.main_frame,
            width=40,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray20",
        )
        self.report_suggestion_title_entry.place(x=80, y=20)
        
        self.report_suggestion_description_label = Label(
            self.main_frame,
            text="Descripcion:",
            font=('Bahnschrift', 13, 'bold'),
            bg="gray20",
            fg="white"
        )
        self.report_suggestion_description_label.place(x=25, y=70)
        
        self.report_suggestion_description_entry = Text(
            self.main_frame,
            width=77,
            height=14,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray20",
        )
        self.report_suggestion_description_entry.place(x=15, y=100)
        
#=====================================================================================
    def send_data(self):
        from controllers.report_controller import create_report_suggest
        from tkinter import messagebox
        import datetime
        
        try:
            report_date = datetime.datetime.now()
            title = self.report_suggestion_title_entry.get().strip()
            description = self.report_suggestion_description_entry.get("1.0", "end-1c").strip()
            result = create_report_suggest(
                self.user_id,
                title,
                description,
                report_date
                
            )
            messagebox.showinfo("Reporte/Sugerencia", result)
            
            if "correctamente" in result:
                self.go_back()
        except Exception as e:
            messagebox.showerror("Error:", f"Error al enviar el reporte/sugerencia: {e}")
            
    def go_back(self):
        from views.products import ProductsWindow
        self.destroy()
        products_window = ProductsWindow(user_id=self.user_id)
        products_window.mainloop()