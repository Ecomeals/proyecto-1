from datetime import datetime

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            return True
        else:
            return False
    except ValueError:
        return False