# Libraries
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from utils.config import APP_TITLE, APP_BG, FONT_HEADING, FONT_MAIN
from database.connection import connect_to_database
import os

# ================================================================================
# Products application
class ProductsWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window properties
        self.title(APP_TITLE + "Ventana Productos v1.0") 
        self.geometry("1220x650+100+5")
        self.configure(bg=APP_BG)
        self.resizable(False, False)
        
        # HEADING FRAME
        self.heading_frame = Frame(
            self,
            bg="gray60",
            width=1220,
            height=120,
        )
        self.heading_frame.place(x=1)
        
        self.heading_title = Label(
            self,
            text="Productos",
            bg="gray60",
            fg="black",
            font=FONT_HEADING,
        )
        self.heading_title.pack()  # MODIFICAR POSICIÓN DEL TÍTULO DE LA PÁGINA
        
        # AGREGAR IMAGEN DE CARRITO DE COMPRAS
        # cart_image = ImageTk.PhotoImage(file='assets/shoppingcart.jpg')
        self.cart_btn = Button(
            self.heading_frame,
            # image= cart_btn,
            text="carrito de compras",
            bg="gray70",
        )
        self.cart_btn.place(x=750, y=50)
        
        self.search_bar = Frame(
            self.heading_frame,
            bg="gray70",
            width=200,
            height=25,
            bd=1,
            relief="solid"
        )
        self.search_bar.place(x=890, y=50)
        
        self.search_btn = Button(
            self.heading_frame,
            text="Buscar",
            bg="gray63",
            fg="black",
            font=('Bahnschrift', 10)
            # image=
        )
        self.search_btn.place(x=1090, y=50)
        
        self.profile_btn = Button(
            self.heading_frame,
            text="Mi perfil",
            bg="gray70",
            fg="black",
            font=FONT_MAIN
        )
        self.profile_btn.place(x=30, y=40)
        
        # PRODUCT FRAME WITH SCROLLBAR
        self.products_frame = Frame(
            self,
            bg="gray63",
            width=1180,
            height=510
        )
        self.products_frame.place(x=10, y=130)
        
        self.canvas = Canvas(
            self.products_frame,
            bg="gray63",
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
            bg="gray63",
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
        
        #SHOW PRODUCTS
        self.display_products()
# #=======METHODS=====================================================================
    def fetch_products(self):
        #DATABASE CONNECTION AND CURSOR
        conn = connect_to_database()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT brand,model,price,stock,image FROM products")
            products = cursor.fetchall()
            return products
        except Exception as e:
            messagebox.showerror("Error:", f"error al recuperar productos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    def add_to_cart(self, brand):
        messagebox.showinfo("Carrito", f"Producto de {brand} añadido al carrito.")
    
    def display_products(self):
        for widget in self.scrollable_inner_frame.winfo_children():
            widget.destroy()
        
        products = self.fetch_products()
        if not products:
            Label(
                self.scrollable_inner_frame,
                text="No hay productos disponibles",
                bg="gray63",
                font=FONT_MAIN,
                justify="center",
                pady=20
            ).pack(pady=10)
            return
        
        for i, product in enumerate(products):
            brand, model, price, stock, image = product
            
            product_frame = Frame(
                self.scrollable_inner_frame,
                bg="gray63",
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
                image_label = Label(product_frame, image=product_image, bg="gray73")
                image_label.image = product_image
                image_label.pack(side="left", padx=10)
            except Exception as e:
                Label(product_frame, text="Imagen no disponible", bg="gray73").pack(side="left", padx=10)
            
            detais_frame = Frame(
                product_frame,
                bg="gray73"
            )
            detais_frame.pack(side="left", fill="both", expand=True)
            
            Label(
                detais_frame,
                text=f"Marca: {brand}\nModelo: {model}\nPrecio: ${price:.2f}",
                bg="gray73",
                font=FONT_MAIN,
                justify="left"
            ).pack(anchor="w")
            
            if stock > 0:
                add_button = Button(
                        product_frame,
                        text="Añadir al carrito",
                        bg="green",
                        fg="white",
                        font=('Bahnscrift', 10, 'bold'),
                        command= lambda brand=brand: self.add_to_cart(brand)
                    )
                add_button.pack(side="right", padx=10)
            else:
                no_stock_label = Label(
                    product_frame,
                    text="Sin stock",
                    bg="red",
                    font=FONT_MAIN,
                    fg="white"
                )
                no_stock_label.pack(side="right", padx=10)
