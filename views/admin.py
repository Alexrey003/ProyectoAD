from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from utils.config import APP_TITLE
from database.connection import connect_to_database


class AdminWindow(Toplevel):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
     
          self.title(APP_TITLE + " - Modo administrador V1.5")
          self.geometry("1150x650+120+10")
          self.configure(bg="black")
          self.resizable(False, False)
     
          # ADMIN HEADING
          self.admin_heading = Label(
               self,
               text="Modo administrador",
               font=('Bahscrift', 15, 'bold'),
               bg='gray60',
               fg='black'
          )
          self.admin_heading.place(x=1, y=20)
     
          # FRAME CON SCROLL
          self.scrollable_frame = Frame(
               self,
               bg="gray60",
               width=1070,
               height=500,
               bd=10
          )
          self.scrollable_frame.place(x=20, y=100)
     
          # Canvas para scroll
          self.canvas = Canvas(
               self.scrollable_frame,
               bg="gray60",
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
               bg="gray60",
               width=1070,
          )
     
          # Configuración de la barra de desplazamiento
          self.scrollable_inner_frame.bind(
               "<Configure>",
               lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
          )
     
          self.canvas.create_window((0, 0), window=self.scrollable_inner_frame, anchor="nw")
          self.canvas.configure(yscrollcommand=self.scrollbar.set)
          
          self.canvas.pack(side="left", fill="both", expand=True)
          self.scrollbar.pack(side="right", fill="y")
          
          # Cargar productos y dibujarlos
          self.display_products()

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

     def display_products(self):
          for widget in self.scrollable_inner_frame.winfo_children():
               widget.destroy()  # Limpiar el frame antes de redibujar

          products = self.fetch_products()
          if not products:
               Label(
                    self.scrollable_inner_frame,
                    text="No hay productos disponibles.",
                    font=('Bahnscrift', 13),
                    bg="gray60"
               ).pack(pady=10)
               return

          for i, product in enumerate(products):
               reference_code, brand, model, category, price, stock = product

               # Crear frame para cada producto
               product_frame = Frame(self.scrollable_inner_frame, bg="gray73", pady=5, padx=5, bd=1, relief="solid")
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
                    bg="gray73",
                    anchor="w",
                    justify=LEFT
               )
               product_label.pack(side="left", fill="x", expand=True, padx=10)

               # Botón para agregar stock
               add_stock_button = Button(
                    product_frame,
                    text="Agregar Stock",
                    font=('Bahnscrift', 13),
                    bg="green",
                    fg="white",
                    command=lambda code=reference_code: self.update_stock(code)
               )
               add_stock_button.pack(side="right", padx=10)
