#======================================================================
# MAIN LIBRARY
from views.login import LoginWindow
# from views.reports import ReportAndSuggestionsWindow

#=====================================================================================
# APPLICATION STARTUP
if __name__ == "__main__":
    app = LoginWindow()
    # app = ReportAndSuggestionsWindow()
    app.mainloop()  