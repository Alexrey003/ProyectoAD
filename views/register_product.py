#====================================================================================
# LIBRARIES
from tkinter import *
from tkinter import ttk
from utils.config import APP_TITLE
from models.product import Products

#======================================================================================
# REGISTER PRODUCTS APPLICATION
class RegisterProduct(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
#=========================================================================================
        # INITIALIZE VARIABLES
        self.reference_code = StringVar()
        self.brand = StringVar()
        self.model = StringVar()
        self.category = StringVar()
        self.price = DoubleVar()
        self.stock = IntVar()
        self.search = StringVar()
        
#============================================================================================
        # DATABASE CONNECTION
        self.database = Products()
        
#=============================================================================================
        # CATEGORY OPTIONS
        self.category_options = [
            'Monitor',
            'Teclado',
            'Mouse',
            'Mousepad',
            'Headset',
            'Gabinete',
            'Motherboard',
            'Targeta grafica(GPU)',
            'Procesador(CPU)',
            'Ram',
            'Almacenamiento(HDD)',
            'Almacenamiento(SSD)',
            'Refrigeracion aire',
            'Refrigeracion liquida'
        ]
        
#========================================================================================
        # CRATE WIDGETS
        self.create_widget()
        
#===== METHODS ===========================================================================
    def create_widget(self):
        # FRAME PROPERTIES
        self.frame1 = Frame(self.master, bg="MediumPurple4", padx=10, pady=10)
        self.frame1.grid(column=0, row=0, sticky="nsew")

        self.frame2 = Frame(self.master, bg="gray20", padx=10, pady=10)
        self.frame2.grid(column=0, row=1, sticky="nsew")

        self.frame3 = Frame(self.master, bg="MediumPurple4", padx=10, pady=10)
        self.frame3.grid(column=1, row=0, rowspan=2, sticky="nsew")
        
#=================================================================================
        # TITLE
        Label(
            self.frame1,
            text="R E G I S T R O   D E   P R O D U C T O S",
            bg="MediumPurple4",
            fg="white",
            font=('Bahnschrift', 15, 'bold')
        ).pack(fill=BOTH)

        # SUBTITLE
        Label(
            self.frame2,
            text='Agregar Nuevos Datos',
            fg='white',
            bg='gray20',
            font=('Bahnschrift', 12, 'bold')
        ).grid(column=0, row=0, columnspan=2, pady=5)
        
#==========================================================================================
        # LABEL FIELDS
        labels = ["Código:", "Marca:", "Modelo:", "Categoría:", "Precio:", "Stock:"]
        for i, label_text in enumerate(labels):
            Label(
                self.frame2,
                text=label_text,
                fg='white',
                bg='gray19',
                font=('Bahnschrift', 12, 'bold')
            ).grid(column=0, row=i+1, pady=5, sticky="e")
            
#===========================================================================================
        # ENTRY FIELDS
        Entry(
            self.frame2,
            textvariable=self.reference_code,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        ).grid(column=1, row=1, padx=5, pady=5)
        
        Entry(
            self.frame2,
            textvariable=self.brand,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        ).grid(column=1, row=2, padx=5, pady=5)
        
        Entry(
            self.frame2,
            textvariable=self.model,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        ).grid(column=1, row=3, padx=5, pady=5)
        
#============================================================================================
        # CATEGORY FIELD (ttk.Combobox)
        self.category_combobox = ttk.Combobox(
            self.frame2, 
            textvariable=self.category, 
            values=self.category_options,
            state='readonly',
            font=('Bahnschrift', 12),
        )
        self.category_combobox.grid(column=1, row=4, padx=5, pady=5)
        self.category_combobox.set("Seleccione una categoría")  # Default placeholder
        
#============================================================================================
        # PRICE AND STOCK
        Entry(
            self.frame2,
            textvariable=self.price,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        ).grid(column=1, row=5, padx=5, pady=5)
        
        Entry(
            self.frame2,
            textvariable=self.stock,
            font=('Bahnschrift', 12),
            fg="white",
            bg="gray19",
            bd=0
        ).grid(column=1, row=6, padx=5, pady=5)
        
#============================================================================================
        # OPTIONS
        Button(
            self.frame2,
            command=self.add_data,
            text='Registrar',
            font=('Bahnschrift', 10, 'bold'),
            bg='MediumPurple3',
            fg="white",
            activebackground="SlateBlue1",
            cursor="hand2"
        ).grid(column=0, row=7, pady=10)

        Button(
            self.frame2,
            command=self.clean_data,
            text='Limpiar',
            font=('Bahnschrift', 10, 'bold'),
            bg='MediumPurple3',
            fg="white",
            activebackground="SlateBlue1",
            cursor="hand2"
        ).grid(column=1, row=7, pady=10)
        
#============================================================================================
        # SEARCH
        Label(
            self.frame2,
            text='Buscar Producto',
            fg='white',
            bg='gray19',
            font=('Bahnschrift', 12)
        ).grid(column=0, row=8, pady=5, sticky="e")

        Entry(
            self.frame2,
            textvariable=self.search,
            font=('Bahnschrift', 12),
            width=15,
            fg="white",
            bg="gray19"
        ).grid(column=1, row=8, padx=5)
        
#===========================================================================================
        Button(
            self.frame2,
            command=self.search_names,
            text='Buscar',
            font=('Bahnschrift', 10, 'bold'),
            bg='MediumPurple3',
            fg="white",
            activebackground="SlateBlue1",
            cursor="hand2"
        ).grid(column=1, row=9, pady=5)

        Button(
            self.frame2,
            command=self.show_everything,
            text='Mostrar Datos',
            font=('Bahnschrift', 10, 'bold'),
            bg='MediumPurple',
            fg="white",
            activebackground="SlateBlue1",
            cursor="hand2"
        ).grid(column=0, row=9, pady=5)
        
#===========================================================================================
        # DATA TABLE
        self.table = ttk.Treeview(
            self.frame3,
            height=20,
        )
        self.table.grid(column=0, row=0, sticky="nsew")

        scrollbar_y = Scrollbar(
            self.frame3,
            orient=VERTICAL,
            command=self.table.yview
        )
        scrollbar_y.grid(column=1, row=0, sticky='ns')
        
        self.table.configure(yscrollcommand=scrollbar_y.set)
        self.table['columns'] = ('brand', 'model', 'category', 'price', 'stock')
        
        self.table.column('#0', width=120, anchor='center')
        self.table.column('brand', width=120, anchor='center')
        self.table.column('model', width=120, anchor='center')
        self.table.column('category', width=120, anchor='center')
        self.table.column('price', width=100, anchor='center')
        self.table.column('stock', width=100, anchor='center')
        
        self.table.heading('#0', text='Código')
        self.table.heading('brand', text='Marca')
        self.table.heading('model', text='Modelo')
        self.table.heading('category', text='Categoría')
        self.table.heading('price', text='Precio')
        self.table.heading('stock', text='Stock')

    def add_data(self):
        reference_code = self.reference_code.get()
        brand = self.brand.get()
        model = self.model.get()
        category = self.category.get()
        price = self.price.get()
        stock = self.stock.get()

        if reference_code and brand and model and category and price and stock:
            self.table.insert('', 'end', text=reference_code, values=(brand, model, category, price, stock))
            self.database.insert_product(reference_code, brand, model, category, price, stock)

    def clean_data(self):
        self.reference_code.set('')
        self.brand.set('')
        self.model.set('')
        self.category.set('')
        self.price.set(0.0)
        self.stock.set(0)
        self.category_combobox.set("Seleccione una categoría")

    def search_names(self):
        search_term = self.search.get()
        if not search_term:
            return
        results = self.database.search_product(search_term, search_term)
        self.table.delete(*self.table.get_children())
        for result in results:
            self.table.insert('', 'end', text=result[0], values=result[1:])

    def show_everything(self):
        records = self.database.show_products()
        self.table.delete(*self.table.get_children())
        for record in records:
            self.table.insert('', 'end', text=record[0], values=record[1:])


def main():
    window = Tk()
    window.wm_title(APP_TITLE + 'Registro productos v1.5')
    window.config(bg="MediumPurple4")
    window.geometry('1100x500')
    window.resizable(0,0)
    app = RegisterProduct(window)
    app.mainloop()
