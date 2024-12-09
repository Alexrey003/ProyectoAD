#===================================================================================
# Libraries
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from utils.config import APP_TITLE
from database.connection import connect_to_database
from views.shopping_cart import ShoppingCartWindow

# ==================================================================================
# Products application
class ProductsWindow(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.user_id = user_id
        self.sidebar_visible = False
        
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
#===================================================================================
        # Window properties
        self.title(APP_TITLE + "Ventana Productos v1.5") 
        self.geometry("1220x650+100+5")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#===================================================================================
        # HEADING FRAME
        self.heading_frame = Frame(
            self,
            bg="MediumPurple4",
            width=1220,
            height=120,
        )
        self.heading_frame.place(x=1)
        
        self.heading_title = Label(
            self,
            text="Productos",
            bg="MediumPurple4",
            fg="white",
            font=('Bahsncrift', 15, 'bold'),
        )
        self.heading_title.pack()
        
        self.profile_btn = Button(
            self.heading_frame,
            text="Mi perfil",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15, 'bold'),
            relief="solid",
            bd=0,
            activebackground="SlateBlue1",
            cursor="hand2",
            command=self.toggle_menu
        )
        self.profile_btn.place(x=50, y=50)
#============================================================================================
        # AGREGAR IMAGEN DE CARRITO DE COMPRAS
        # cart_image = ImageTk.PhotoImage(file='assets/shoppingcart.jpg')
        self.cart_btn = Button(
            self.heading_frame,
            # image= cart_btn,
            text="Carrito",
            bg="MediumPurple3",
            bd=0,
            relief="solid",
            activebackground="SlateBlue1",
            fg="white",
            font=('Bahnscfrift', 13),
            cursor="hand2",
            command=self.open_cart,
        )
        self.cart_btn.place(x=790, y=50)
        
#==============================================================================================
        # SEARCH BAR AND SEARCH BUTTON
        self.search_entry = Entry(
            self.heading_frame,
            bg="gray20",
            fg="white",
            width=25,
            font=('Bahnscrift', 13),
        )
        self.search_entry.place(x=870, y=54)
        
        self.search_btn = Button(
            self.heading_frame,
            text="Buscar",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnschrift', 13),
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            # image=
            command= lambda: self.display_products(self.search_entry.get())
        )
        self.search_btn.place(x=1090, y=50)
        
#==============================================================================================
        # FRAME WHERE THE PRODUCTS ARE SHOWN WITH A USEFUL SCROLLBAR
        self.products_frame = Frame(
            self,
            bg="gray19",
            width=1180,
            height=510
        )
        self.products_frame.place(x=10, y=130)
        
        self.canvas = Canvas(
            self.products_frame,
            bg="gray19",
            width=1180,
            height=510
        )
        self.scrollbar = Scrollbar(
            self.products_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollable_inner_frame = Frame(
            self.canvas,
            bg="gray19",
            width=1180
        )
        
        self.scrollable_inner_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window(
            (0,0),
            window=self.scrollable_inner_frame,
            anchor="nw"
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        #SHOW PRODUCTS METHOD
        self.display_products()
        
#=======METHODS=====================================================================
        #FETCH PRODUCTS TO SHOW
    def fetch_products(self, search_query=""):
        #DATABASE CONNECTION AND CURSOR
        conn = connect_to_database()
        cursor = conn.cursor()
        
        try:
            if search_query:
                cursor.execute(
                    """
                    SELECT reference_code, brand, model, price, stock, image
                    FROM products
                    WHERE LOWER(brand) LIKE LOWER(%s) OR LOWER(model) LIKE LOWER(%s)
                    """,
                    (f"%{search_query}%", f"%{search_query}%")
                )
            else:
                cursor.execute("SELECT reference_code, brand, model, price, stock, image FROM products")
                
            products = cursor.fetchall()
            return products
        except Exception as e:
            messagebox.showerror("Error:", f"error al recuperar productos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
            
#======================================================================================================
    #ADDING PRODUCT MESSAGES
    def add_to_cart(self, product_code, user_id):
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT quantity
                FROM shopping_cart
                WHERE user_id=%s AND product_code=%s
                """,(user_id,product_code)
            )
            result = cursor.fetchone()

            if result:
                quantity = result[0] + 1
                cursor.execute(
                    """
                    UPDATE shopping_cart
                    SET quantity=%s
                    WHERE user_id=%s AND product_code=%s
                    """,
                    (quantity, user_id, product_code)
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO shopping_cart (user_id, product_code, quantity)
                    VALUES (%s, %s, 1)
                    """,
                    (user_id, product_code)
                )
            conn.commit()
            messagebox.showinfo("Éxito:", "Producto agregado al carrito de compras")
        except Exception as e:
            messagebox.showerror("Error:", f"Error al agregar producto al carrito de compras: {e}")
        finally:
            cursor.close()
            conn.close()
#=======================================================================================================
    #DISPLAYING PRODUCTS IN THE WINDOW
    def display_products(self,search_query=""):
        for widget in self.scrollable_inner_frame.winfo_children():
            widget.destroy()
        
        products = self.fetch_products(search_query)
        if not products:
            Label(
                self.scrollable_inner_frame,
                text="No hay productos disponibles",
                bg="gray20",
                fg="white",
                font=('Bahnscrift', 13),
                justify="center",
                pady=20
            ).pack(pady=10)
            return
        
        for i, product in enumerate(products):
            reference_code, brand, model, price, stock, image = product
            
            product_frame = Frame(
                self.scrollable_inner_frame,
                bg="gray19",
                pady=5,
                padx=5,
                bd=1,
                relief="solid",
                width=1130
            )
            product_frame.pack(fill="x", pady=5)
            
            try:
                img = Image.open(image).resize((100,100))
                product_image = ImageTk.PhotoImage(img)
                image_label = Label(product_frame, image=product_image, bg="gray20")
                image_label.image = product_image
                image_label.pack(side="left", padx=10)
            except Exception as e:
                Label(product_frame, text="Imagen no disponible", bg="gray20", fg="white").pack(side="left", padx=10)
            
            detais_frame = Frame(
                product_frame,
                bg="gray20"
            )
            detais_frame.pack(side="left", fill="both", expand=True)
            
            Label(
                detais_frame,
            text=f"Còdigo: {reference_code}\nMarca: {brand}\nModelo: {model}\nPrecio: ${price:.2f}",
                bg="gray20",
                font=('Bahnscrift', 13),
                justify="left",
                fg="white"
            ).pack(anchor="w")
            
            if int(stock) > 0:
                add_button = Button(
                        product_frame,
                        text="Añadir al carrito",
                        bg="MediumPurple3",
                        fg="white",
                        font=('Bahnscrift', 10, 'bold'),
                        relief="solid",
                        bd=0,
                        activebackground="SlateBlue1",
                        cursor="hand2",
                        command= lambda product_code=reference_code: self.add_to_cart(product_code, self.user_id)
                    )
                add_button.pack(side="right", padx=10)
            else:
                no_stock_label = Label(
                    product_frame,
                    text="Sin stock",
                    bg="red",
                    font=('Bahnscrift', 13),
                    fg="white"
                )
                no_stock_label.pack(side="right", padx=10)
    
    def open_cart(self):
        self.destroy()
        cart_window = ShoppingCartWindow(self.user_id)
        cart_window.mainloop()
        
#================================================================================================
    # METHODS FOR THE PROFILE SIDEBAR MENU
    def toggle_menu(self):
        def colapse_menu():
            self.sidebar_frame.destroy()
            
        self.sidebar_frame = Frame(
            self,
            bg="gray18",
        )
        
        self.window_height = 650
        self.sidebar_frame.place(x=0, y=0, height=self.window_height, width=350)
        
        self.colapse_btn = Button(
            self.sidebar_frame,
            text="Cerrar Menu",
            bg="gray18",
            fg="white",
            font=('Bahnscrift', 18),
            relief="solid",
            bd=0,
            cursor="hand2",
            activebackground="gray18",
            command=colapse_menu
        ).place(x=15, y=10)
        
        self.profile_label = Label(
            self.sidebar_frame,
            text=f"Bienvenido: {self.username_info['username']}",
            bg="gray18",
            fg="white",
            font=('Bahnscrift', 14),
            justify="center",
            pady=20
        ).place(x=15, y=50)
        
        self.profile_label_2 = Label(
            self.sidebar_frame,
            text="Aqui podras acceder a otras opciones.",
            bg="gray18",
            fg="white",
            font=('Bahnscrift', 12),
            justify="center",
            pady=20
        ).place(x=15, y=100)
        
        self.home_btn = Button(
            self.sidebar_frame,
            text="Productos",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15),
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            width=35,
            # command= DOESNT NEED COMMAND CAUSE IS IN THE PRODUCTS PAGE
        ).place(y=200)
        
        self.info_btn = Button(
            self.sidebar_frame,
            text="Información perfil",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15),
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            width=35,
            command= self.open_profile_info_window
        ).place(y=270)
        
        self.report_suggest_btn = Button(
            self.sidebar_frame,
            text="Reportar/Sugerir",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15),
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            width=35,
            command=self.open_report_suggest_window
        ).place(y=340)
        
        self.logout_btn = Button(
            self.sidebar_frame,
            text="Cerrar Sesión",
            bg="MediumPurple3",
            fg="white",
            font=('Bahnscrift', 15),
            activebackground="SlateBlue1",
            bd=0,
            relief="solid",
            cursor="hand2",
            width=35,
            command=self.logout
        ).place(y=410)
        
        
    def open_report_suggest_window(self):
        from views.reports import ReportAndSuggestionsUsersWindow
        self.destroy()
        report_suggest_window = ReportAndSuggestionsUsersWindow(self.user_id)
        report_suggest_window.mainloop()

    def open_profile_info_window(self):
        from views.profile import ProfileWindow
        self.destroy()
        profile_window = ProfileWindow(self.user_id)
        profile_window.mainloop()
    def logout(self):
        from views.login import LoginWindow
        
        logout_question = messagebox.askquestion("Cerrar Sesión.", "¿Esta seguro de querer salir de la sesión?")
        if logout_question == "yes":
            self.destroy()
            login_window = LoginWindow()
            login_window.mainloop()
        else:
            return