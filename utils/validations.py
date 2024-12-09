#LIBRARIES
import re

#============================================================================
#VALIDATIONS FOR THE USER REGISTER
def validate_name(name):
    return name.strip() != ""

def validate_lastname(lastname):
    return lastname.strip() != ""

def validate_direction(direction):
    return direction.strip()!= ""

def validate_phone(phone):
    return re.match(r"^\d{10}$", phone) 
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

def validate_username(username):
    return username.strip()!= "" and len(username) >= 5

def validate_password(password):
    return len(password) >= 8

#==============================================================================
# # VALIDATIONS FOR THE PAYPEMT
def validate_card_number(card_number):
    return bool(re.match(r"^\d{16}$", card_number))

def validate_cardholder_name(cardholder_name):
    return cardholder_name.strip() != ""

def validate_expiration_date(expiration_date):
    import datetime

    try:
        month, year = map(int, expiration_date.split('/'))
        
        if not (1 <= month <= 12):
            return False
        
        now = datetime.datetime.now()
        current_year = now.year
        current_month = now.month
        
        year += 2000
        
        if year < current_year or (year == current_year and month < current_month):
            return False
        
        return True
    except ValueError:
        return False
def validate_ccv(ccv):
    return bool(re.match(r"^\d{3}$", ccv))

#=============================================================================
# VALIDATIONS FOR REPORT AND SUGGEST PAGE

def validate_report_title(title):
    return isinstance(title, str) and title.strip() != ""

def validate_report_description(description):
    return isinstance(description, str) and description.strip() != ""