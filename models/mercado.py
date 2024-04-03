from models.producto import Producto
import os


class Mercado:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, fecha_compra, fecha_vencimiento):
        self.productos.append(Producto(nombre, cantidad, fecha_compra, fecha_vencimiento))

    def exportar_a_texto(self):
        with open("productos.txt", "w") as archivo:
            for producto in self.productos:
                archivo.write(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Fecha de compra: {producto.fecha_compra.strftime('%Y-%m-%d')}, Fecha de vencimiento: {producto.fecha_vencimiento.strftime('%Y-%m-%d')}, {'Vencido' if producto.esta_vencido() else 'No vencido'}\n")

    def cargar_desde_archivo(self, nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(", ")
                    nombre = datos[0].split(": ")[1]
                    cantidad = int(datos[1].split(": ")[1])
                    fecha_compra = datos[2].split(": ")[1]
                    fecha_vencimiento = datos[3].split(": ")[1]
                    self.agregar_producto(nombre, cantidad, fecha_compra, fecha_vencimiento)
                    
    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return True
            
        return False
    