from datetime import datetime

class Producto:
    def __init__(self, nombre, cantidad, fecha_compra, fecha_vencimiento):
        self.nombre = nombre
        self.cantidad = cantidad
        self.fecha_compra = datetime.strptime(fecha_compra, "%Y-%m-%d")
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def __str__(self):
        return f"{self.nombre}: Cantidad: {self.cantidad}, Fecha de compra: {self.fecha_compra.strftime('%Y-%m-%d')}, Fecha de vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

    def esta_vencido(self):
        fecha_actual = datetime.now()
        return fecha_actual > self.fecha_vencimiento