#======================================================================
# MAIN LIBRARY
from views.login import LoginWindow

#=====================================================================================
# APPLICATION STARTUP
if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()