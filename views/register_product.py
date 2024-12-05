#========================================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from utils.config import APP_TITLE
from models.product import Products

#==========================================================================================
# REGISTER PRODUCT APPLICATION
class RegisterProduct(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        # self.user_id = user_id
#============================================================================================
        # FRAME PROPERTIES
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0, row=0)
        
        self.frame2 = Frame(master, bg="MediumPurple4")
        self.frame2.grid(column=0, row=1)
        
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)
        
        self.frame4 = Frame(master, bg="black")
        self.frame4.grid(row=0, column=0)
        
        self.reference_code = StringVar()
        self.brand = StringVar()
        self.model = StringVar()
        self.category = StringVar()
        self.price = DoubleVar()
        # self.stock = IntVar()
        
        self.database = Products()
        
#==============================================================================================
        self.create_widget()

#========= METHODS ============================================================================
    def create_widget(self):
        #TITLE
        Label(
            self.frame1,
            text= "R E G I S T R O \t D E \t D A T O S",
            bg="MediumPurple4",
            fg="white",
            font=('Bahnscrift', 15, 'bold'),
        ).grid(column=0, row=0)
        
        # SUBTITLE
        Label(
            self.frame2,
            text = 'Agregar Nuevos Datos',
            fg='white',
            bg ='MediumPurple3',
            font=('Bahnscrift',12,'bold')
        ).grid(columnspan=2, column=0,row=0, pady=5)
        
        
#==============================================================================================
# LABEL FIELDS
        # REFERENCE CODE
        Label(
            self.frame2,
            text = 'Codigo',
            fg='white',
            bg ='gray20',
            font=('Bahnscrift',13,'bold')
        ).grid(column=0,row=1, pady=15)
        
        # BRAND
        Label(
            self.frame2,
            text = 'Marca',
            fg='white',
            bg ='gray20',
            font=('Bahnscrift',13,'bold')
        ).grid(column=0,row=2, pady=15)
        
        # MODEL
        Label(
            self.frame2,
            text = 'Modelo',
            fg='white',
            bg ='gray20',
            font=('Bahnscrift',13,'bold')
        ).grid(column=0,row=3, pady=15)
        
        # PRECIO
        Label(
            self.frame2,
            text = 'Categoria',
            fg='white',
            bg ='gray20',
            font=('Bahnscrift',13,'bold')
        ).grid(column=0,row=4, pady=15)
        
        # STOCK
        Label(
            self.frame2,
            text = 'Precio',
            fg='white',
            bg ='gray20',
            font=('Bahnscrift',13,'bold')
        ).grid(column=0,row=5, pady=15)
        
        
#=======================================================================================
# ENTRIE FIELDS
        Entry(
            self.frame2,
        textvariable=self.reference_code,
        font=('Bahnscrift',12)
        ).grid(column=1,row=1, padx =5)
        
        Entry(
            self.frame2,
        textvariable=self.brand,
        font=('Bahnscrift',12)
        ).grid(column=1,row=2)
        
        Entry(
            self.frame2,
        textvariable=self.model,
        font=('Bahnscrift',12)
        ).grid(column=1,row=3)
        
        Entry(
            self.frame2,
        textvariable=self.price,
        font=('Bahnscrift',12)
        ).grid(column=1,row=4)
        
        Entry(
            self.frame2,
        textvariable=self.category,
        font=('Bahnscrift',12)
        ).grid(column=1,row=5)
        
        
#========================================================================================
# OPTIONS FIELDS
        Label(
            self.frame4,
            text = 'Control',
            fg='white',
            bg ='black',
            font=('Bahnscrift',12,'bold')
        ).grid(columnspan=3, column=0,row=0, pady=1, padx=4)
        
        Button(
            self.frame4,
            # command= self.agregar_datos,
            text='REGISTRAR',
            font=('Bahnscrift',10,'bold'),
            bg='magenta2'
        ).grid(column=0,row=1, pady=10, padx=4)
        
        Button(
            self.frame4,
            # command = self.limpiar_datos,
            text='LIMPIAR',
            font=('Bahnscrift',10,'bold'),
            bg='orange red'
        ).grid(column=1,row=1, padx=10) 

        Button(
            self.frame4,
            # command = self.eliminar_fila,
            text='ELIMINAR',
            font=('Bahnscrift',10,'bold'),
            bg='yellow'
        ).grid(column=2,row=1, padx=4)
        
        Button(
            self.frame4,
            # command = self.buscar_nombre,
            text='BUSCAR POR NOMBRE',
            font=('Bahnscrift',8,'bold'),
            bg='orange'
        ).grid(columnspan=2,column = 1, row=2)
        
        Entry(
            self.frame4,
            # textvariable=self.buscar ,
            font=('Bahnscrift',12),
            width=10
        ).grid(column=0,row=2, pady=1, padx=8)
        
        Button(
            self.frame4,
            # command = self.mostrar_todo,
            text='MOSTRAR DATOS',
            font=('Bahnscrift',10,'bold'),
            bg='green2'
        ).grid(columnspan=3,column=0,row=3, pady=8)
