#==============================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from utils.config import APP_TITLE
from database.connection import connect_to_database
from PIL import Image, ImageTk

#==============================================================================
# SHOPPING CART APPLICATION
class ShoppingCartWindow(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
#==============================================================================
        # WINDOWS PROPERTIES
        self.title(APP_TITLE + "Carrito de compras v1.5")
        self.geometry("1190x650+100+50")
        self.configure(bg="MediumPurple4")
        self.resizable(False, False)
        
#==============================================================================
        # SHOPPING CART HEADING
        self.title_heading_label_1 =  Label(
            self,
            text="Carrito de compras",
            font=("Bahnschrift", 20, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        self.title_heading_label_1.place(x=1)
        
        self.title_heading_label_2 =  Label(
            self,
            text="Estos son los productos que has añadido, verifica que sean correctos:",
            font=("Bahnschrift", 15, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        self.title_heading_label_2.place(x=1, y=40)
        
        self.total_price_label = Label(
            self,
            text="Total: $0.00",
            font=("Bahnschrift", 15, "bold"),
            bg="MediumPurple4",
            fg="white",
        )
        self.total_price_label.place(x=700, y=40)
        
        # PROCEED TO PAYMENT BUTTON
        self.continue_btn = Button(
            self,
            text="Proceder pago",
            font=("Bahnschrift", 13, 'bold'),
            fg='white',
            bg='MediumPurple3',
            activebackground="SlateBlue1",
            relief="solid",
            bd=0,
            cursor='hand2',
            command=self.proceed_payment
        )
        self.continue_btn.place(x=870, y=40)
        
        # EXIT SHOPPING CART BUTTON
        self.exit_btn = Button(
            self,
            text="Atras",
            font=("Bahnschrift", 13),
            fg='white',
            bg='MediumPurple3',
            activebackground="SlateBlue1",
            relief="solid",
            bd=0,
            cursor='hand2',
            command=self.go_back
        )
        self.exit_btn.place(x=1125, y=20)
#===============================================================================
        # SHOPPING CART ITEMS
        self.product_base_frame = Frame(
            self,
            bg="gray20",
            width=1150,
            height=550,
        )
        self.product_base_frame.place(x=10, y=80) #FRAME WHERE THE PRODUCTS ARE GOING TO BE WITH A USEFUL SCROLLBAR
        
        self.canvas = Canvas(
            self.product_base_frame,
            bg="gray20",
            width=1150,
            height=550,
        )
        self.scrollbar = Scrollbar(
            self.product_base_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollable_inner_frame = Frame(
            self.canvas,
            bg="gray20",
            width=1150,
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

        self.display_cart_items()

#========   METHODS  ========================================================================
    def fetch_cart_items(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT p.reference_code, p.brand, p.model, sc.quantity, p.price, p.image
                FROM shopping_cart sc
                JOIN products p ON sc.product_code = p.reference_code
                WHERE sc.user_id = %s
                """,(self.user_id,))
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            messagebox.showerror("Error:", f"No se pudieron recuperrar los productos del carrito: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def display_cart_items(self):
        for widget in self.scrollable_inner_frame.winfo_children():
            widget.destroy()
        
        cart_items = self.fetch_cart_items()
        if not cart_items:
            Label(
                self.scrollable_inner_frame,
                text="No hay productos en el carrito.",
                font=("Bahnschrift", 15, "bold"),
                bg="gray20",
                fg="white",
            ).pack(pady=10)
            self.total_price_label.config(text="Total: $0.00")
            return
        
        total_price = 0
        for item in cart_items:
            reference_code, brand, model, quantity, price, image = item
            total_price += price * quantity
            
            item_frame = Frame(
                self.scrollable_inner_frame,
                bg="gray19",
                pady=5,
                padx=5,
                bd=1,
                relief="solid"
            )
            item_frame.pack(fill="x", pady=5, padx=10)
            
            try:
                img = Image.open(image).resize((50,50))
                product_image = ImageTk.PhotoImage(img)
                image_label = Label(item_frame, image=product_image, bg="gray19")
                image_label.image = product_image
                image_label.pack(side="left", padx=10)
            except Exception as e:
                Label(item_frame, text="Imagen no disponible", bg="gray19", fg="white").pack(side="left", padx=10)
                
            detais = f"Marca: {brand}\nModelo: {model}\nCantidad: {quantity}\nPrecio: ${price:.2f}"
            Label(
                item_frame,
                text=detais,
                font=("Bahnschrift", 12),
                bg="gray19",
                fg="white",
                justify="left"
            ).pack(side="left", padx=10)
            
            delete_btn = Button(
                item_frame,
                text="Eliminar",
                font=("Bahnschrift", 10),
                bg="red",
                fg="white",
                cursor="hand2",
                command=lambda ref=reference_code: self.remove_from_cart(ref)
            )
            delete_btn.pack(side="right", padx=10)
            
        
        self.total_price_label.config(text=f"Total: ${total_price:.2f}")
    def remove_from_cart(self, product_code):
        conn = connect_to_database()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                """
                DELETE FROM shopping_cart
                WHERE user_id = %s AND product_code = %s
                """,
                (self.user_id, product_code)
            )
            conn.commit()
            messagebox.showinfo("Éxito:", "Producto eliminado del carrito.")
            self.display_cart_items()
        except Exception as e:
            messagebox.showerror("Error:", f"No se pudo eliminar el producto del carrito: {e}")
        finally:
            cursor.close()
            conn.close()
    
    def go_back(self):
        from views.products import ProductsWindow
        self.destroy()
        product_window = ProductsWindow(self.user_id)
        product_window.mainloop()
    
    def proceed_payment(self):
        from views.checkout import CheckOut
        self.destroy()
        checkout_window = CheckOut(self.user_id)
        checkout_window.mainloop()