#===================================================================================
# LIBRARIES
from tkinter import *

#===================================================================================
# REPORT AND SUGGESTIONS APPLICATION
class ReportAndSuggestionsWindow(Tk):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id