#========================================================================================
# LIBRARIES
from tkinter import *
from tkinter import messagebox
from database.connection import connect_to_database
from utils.config import APP_TITLE

#==========================================================================================
# REGISTER PRODUCT APPLICATION
class RegisterProduct(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        
#============================================================================================
        # WINDOW PROPERTIES
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
        self.stock = IntVar()
        