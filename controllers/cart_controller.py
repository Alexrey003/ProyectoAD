#=================================================================
# LIBRARIES
from models.order import Card
from utils.validations import (validate_card_number, validate_ccv, validate_cardholder_name, validate_expiration_date)
import hashlib

#================================================================
def register_card(user_id, card_number, cardholder_name, expiration_date, ccv):
    validation_errors = []
    
    if not validate_card_number(card_number):
        validation_errors.append("Numero de tarjeta invalido.")
    if not validate_cardholder_name(cardholder_name):
        validation_errors.append("Nombre del titular invalido")
    if not validate_expiration_date(expiration_date):
        validation_errors.append("Fecha de expiracion invalida.")
    if not validate_ccv(ccv):
        validation_errors.append("CCV invalido.")
        
    if validation_errors:
        return "Errores de validacion: " + ", ".join(validation_errors)
    
    
    # hashed_card_number = hashlib.sha256(card_number.encode()).hexdigest()
    # hashed_ccv = hashlib.sha256(ccv.encode()).hexdigest()
    try:
        card = Card(user_id)
        card.link_card(card_number, cardholder_name, expiration_date, ccv)
        return "Tarjeta registrada correctamente\nEn caso de error de uso de tarjeta vuelva a atrás para refrescar."
    except Exception as e:
        return f"Error al registrar la tarjeta: {e}"