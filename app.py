#======================================================================
# MAIN LIBRARY
from views.login import LoginWindow
from views.admin import AdminWindow
from views.register_product import RegisterProduct

#=====================================================================================
# APPLICATION STARTUP
if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()