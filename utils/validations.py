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