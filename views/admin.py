#==================================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from utils.config import APP_TITLE
from database.connection import connect_to_database

#====================================================================================
# ADMINISTRATION APPLICATION
class AdminWindow(Tk):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          # self.user_id = user_id
          
#======================================================================================
          # WINDOW PROPERTIES 
          self.title(APP_TITLE + " - Modo administrador V1.5")
          self.geometry("1150x650+120+10")
          self.configure(bg="MediumPurple4")
          self.resizable(False, False)
          
#========================================================================================
          # ADMIN HEADING
          self.admin_heading = Label(
               self,
               text="Modo administrador",
               font=('Bahscrift', 15, 'bold'),
               bg='MediumPurple4',
               fg='White'
          )
          self.admin_heading.place(x=1, y=10)
          
          self.admin_label_2 = Label(
               self,
               text="Bienvenido al modo administrador, aquí podras administrar los productos y usuarios.",
               font=('Bahnschrift', 13, 'bold'),
               bg='MediumPurple4',
               fg='white'
          )
          self.admin_label_2.place(x=1, y=40)
          
          self.admin_label_3 = Label(
               self,
               text="En esta sección podras añadir nuevas existencias a productos ya registrados",
               font=('Bahnschrift', 13, 'bold'),
               bg='MediumPurple4',
               fg='white'
          )
          self.admin_label_3.place(x=1, y=70)
          
          # BUTTON WITH DIFERENT SECTIONS FOR THE ADMINS
          self.register_product_btn = Button(
               self,
               text="Añadir productos",
               bg="MediumPurple3",
               fg="white",
               bd=0,
               relief="solid",
               activebackground="Slateblue1",
               cursor="hand2",
               font=('Bahnschrift', 13, 'bold'),
               #command=
          )
          self.register_product_btn.place(x=950, y=10)
          
#==========================================================================================
          # FRAME WHERE THE PRODUCTS ARE GOING TO BE WITH A USEFUL SCROLLBAR
          self.scrollable_frame = Frame(
               self,
               bg="gray20",
               width=1070,
               height=500,
               bd=10
          )
          self.scrollable_frame.place(x=20, y=100)
          
          self.canvas = Canvas(
               self.scrollable_frame,
               bg="gray20",
               width=1070,
               height=500
          )
          self.scrollbar = Scrollbar(
               self.scrollable_frame,
               orient="vertical",
               command=self.canvas.yview
          )
          self.scrollable_inner_frame = Frame(
               self.canvas,
               bg="gray20",
               width=1070,
          )
          
          self.scrollable_inner_frame.bind(
               "<Configure>",
               lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
          )
          
          self.canvas.create_window((0, 0), window=self.scrollable_inner_frame, anchor="nw")
          self.canvas.configure(yscrollcommand=self.scrollbar.set)
          
          self.canvas.pack(side="left", fill="both", expand=True)
          self.scrollbar.pack(side="right", fill="y")
          
          self.display_products()
#========  METHODS ================================================================================
     # FETCH THE PRODUCTS METHOD
     def fetch_products(self):
          conn = connect_to_database()
          cursor = conn.cursor()
          try:
               cursor.execute("SELECT reference_code, brand, model, category, price, stock FROM products")
               products = cursor.fetchall()
               return products
          except Exception as e:
               messagebox.showerror("Error", f"No se pudieron recuperar los productos: {e}")
               return []
          finally:
               cursor.close()
               conn.close()

#======================================================================================================
     # UPDATING THE PRODUCTS METHOD
     def update_stock(self, reference_code):
          conn = connect_to_database()
          cursor = conn.cursor()
          try:
               cursor.execute("UPDATE products SET stock = stock + 1 WHERE reference_code = %s", (reference_code,))
               conn.commit()
               messagebox.showinfo("Éxito", "El stock ha sido actualizado correctamente.")
               self.display_products()  # Redibujar productos
          except Exception as e:
               messagebox.showerror("Error", f"No se pudo actualizar el stock: {e}")
          finally:
               cursor.close()
               conn.close()

#======================================================================================================
     # DISPLAYING THE PRODUCTS METHOD
     def display_products(self):
          for widget in self.scrollable_inner_frame.winfo_children():
               widget.destroy()
               
          products = self.fetch_products()
          if not products:
               Label(
                    self.scrollable_inner_frame,
                    text="No hay productos disponibles.",
                    font=('Bahnscrift', 13),
                    bg="gray19"
               ).pack(pady=10)
               return

          for i, product in enumerate(products):
               reference_code, brand, model, category, price, stock = product

               # Crear frame para cada producto
               product_frame = Frame(self.scrollable_inner_frame, bg="gray19", pady=5, padx=5, bd=1, relief="solid")
               product_frame.pack(fill="x", pady=5)

               # Etiqueta con la información del producto
               product_label = Label(
                    product_frame,
                    text=(
                         f"Referencia: {reference_code}\n"
                         f"Marca: {brand}\n"
                         f"Modelo: {model}\n"
                         f"Categoría: {category}\n"
                         f"Precio: ${price:.2f}\n"
                         f"Stock: {stock}"
                    ),
                    font=('Bahnscrift', 13),
                    bg="gray19",
                    fg="white",
                    anchor="w",
                    justify=LEFT
               )
               product_label.pack(side="left", fill="x", expand=True, padx=10)

               # Botón para agregar stock
               add_stock_button = Button(
                    product_frame,
                    text="Agregar Stock",
                    font=('Bahnscrift', 13),
                    bg="MediumPurple3",
                    fg="white",
                    command=lambda code=reference_code: self.update_stock(code)
               )
               add_stock_button.pack(side="right", padx=10)
