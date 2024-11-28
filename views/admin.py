# LIBRARIES
from tkinter import *
from PIL import ImageTk
from utils.config import APP_TITLE, FONT_HEADING

#===============================
FONT_HEADING = ("Bahnschrift", 23, "bold")
# Admin window class
class AdminWindow(Toplevel):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          
          self.screen_width = self.winfo_screenwidth()
          self.screen_height = self.winfo_screenheight()
          
          self.window_width = int(self.screen_width * 0.8)
          self.window_height = int(self.screen_height * 0.8)
          
          # WINDOWS PROPERTIES
          self.title(APP_TITLE + "Modo administrator V1.0") #APP_TITLE
          self.geometry("1000x650+180+30")
          self.configure(bg="black")
          self.resizable(False, False)

          # Load background image
          try:
               self.bg_image = ImageTk.PhotoImage(file="assets/adminbg.jpg")
          except FileNotFoundError:
               print("Background image not found!")

               self.bg_image = None

          if self.bg_image:
               self.bg_label = Label(self, image=self.bg_image)
               self.bg_label.pack(fill=BOTH, expand=True)
          else:
               self.configure(bg="gray")
          
          # ADMIN HEADING
          self.admin_heading = Label(
               self,
               text="Modo administrator",
               font=FONT_HEADING,
               bg='gray60',
               fg='black'
          )
          self.admin_heading.place(x=1, y=20)
          
          # FRAME 1
          self.frame_p1 = Frame(
               self,
               bg="white",
               width=450,
               height=500,
               bd=10
          )
          self.frame_p1.place(x=20, y=100)
          
          self.frame_p2 = Frame(
               self,
               bg="white",
               width=450,
               height=500,
               bd=10
          )
          self.frame_p2.place(x=520, y=100)


if __name__ == "__main__":
     app = AdminWindow()
     app.mainloop()