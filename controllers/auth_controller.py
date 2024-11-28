#LIBRARIES
from models.user import User
from utils.validations import (validate_name, validate_email, validate_phone, 
                            validate_password, validate_lastname, validate_direction, validate_username)
import hashlib
import mariadb

#============================================================================
def register_user(name, lastname, direction, phone, email, username, password):
    if not validate_name(name):
        return "El nombre no puede estar vacio"
    if not validate_lastname(lastname):
        return "El apellido no puede estar vacio"
    if not validate_direction(direction):
        return "La dirección no puede estar vacia"
    if not validate_phone(phone):
        return "El teléfono no puede estar vacio"
    if not validate_email(email):
        return "El correo electrónico no es válido"
    if not validate_username(username):
        return "El usuario no puede estar vacio"
    if not validate_password(password):
        return "La contraseña debe tener al menos 8 caracteres"
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        User.create_user(name, lastname, direction, phone, email, username, hashed_password)
        return "Usuario registrado exitosamente"
    except mariadb.DatabaseError as e:
        return f"Error al registrar el usuario: {str(e)}, {name} {lastname} {direction} {phone} {email} {username} {password}"
