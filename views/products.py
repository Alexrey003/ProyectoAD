#Libraries
from tkinter import *
from PIL import ImageTk
from utils.config import APP_TITLE, APP_BG, FONT_HEADING, FONT_MAIN

#============================================================================
#Products aplication
class ProductsWindow(Tk):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Window properties
        self.title(APP_TITLE + "Ventana Productos v1.0")
        self.geometry("1000x650+180+30")
        self.configure(bg=APP_BG)
        self.resizable(False, False)

        # load background image
        try:
            self.bg_image = ImageTk.PhotoImage(file="assets/productsbg.png") 
        except FileNotFoundError:
            print("Background images not found! Using default background color")
            self.bg_image = None

        if self.bg_image:
            self.bg_label = Label(self, image=self.bg_image)
            self.bg_label.pack(fill=BOTH, expand=True)
        else:
            self.configure(bg="gray")

        # Product heading
        self.products_heading = Label(
            self,
            text="Productos",
            font=FONT_HEADING,
            bg="firebrick1",
            fg="black",
            width= 60,
            height=2
        )
        self.products_heading.place(x=-19, y=20)

#================================================================================================
if __name__ == "__main__":
    app = ProductsWindow()
    app.mainloop()