from datetime import datetime


# Valida si la fecha fue puesta correctamente en formato año, mes, día

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


#Valida si la cantidad fue puesta correctamente, debe ser mayor a 0.

def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            return True
        else:
            return False
    except ValueError:
        return False
