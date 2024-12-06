#===================================================================================
# LIBRARIES
from tkinter import *

#===================================================================================
# FORGOT PASSWORD APPLICATION
class ForgotPasswordWindow(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id