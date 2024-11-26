# LIBRARIES
from tkinter import *
from PIL import ImageTk

#===============================
# Admin window class
class AdminWindow(TopLevel):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          
          # WINDOWS PROPERTIES
          self.title(APP_TITLE + "Modo administrator V1.0")
           # self.geometry() definitely luego geometria 
           self.configure(bg="black")
           self.rezisable(False, False)

           # Load background image
           try:
                self.bg_image = ImageTk.PhotoImage(file="assets/adminbg.jpg")
           except FileNotFoundError:
                print("Background image not found!")

                 self.bg_image = None

                 if self.bg_image;
                      self.bg_label = Label(self, image=self.bg_image)
                      self.bg_label.pack(fill=BOTH, expand=True)
                 else:
                      self.configure(bg="gray")