#========================================================================
# LIBRARIES
from models.report_suggest import ReportAndSuggest
from utils.validations import validate_report_title, validate_report_description

#========================================================================
def create_report_suggest(user_id, title, description, report_date):
    if not validate_report_title(title):
        return "El titulo del informe no puede estar vacio."
    if not validate_report_description(description):
        return "La descripcion del informe no puede estar vacia."
    
    try:
        report = ReportAndSuggest(user_id)
        report.generate_report_suggest(title, description, report_date)
        return "Reporte/Sugerencia enviado correctamente.\nGracias por si tiempop."
    except Exception as e:
        return f"Error al generar el reporte/sugerencia: {e}"