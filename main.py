from models.mercado import Mercado
from utils.validaciones import validar_fecha, validar_cantidad


def main():
    mercado = Mercado()
    mercado.cargar_desde_archivo("productos.txt")

    while True:
        print("\n1. Agregar producto")
        print("2. Exportar a archivo")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad: ")
            fecha_compra = input("Ingrese la fecha de compra (YYYY-MM-DD): ")
            while not validar_fecha(fecha_compra):
                fecha_compra = input("Fecha inválida. Ingrese la fecha de compra nuevamente (YYYY-MM-DD): ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            while not validar_fecha(fecha_vencimiento):
                fecha_vencimiento = input("Fecha inválida. Ingrese la fecha de vencimiento nuevamente (YYYY-MM-DD): ")

            while not validar_cantidad(cantidad):
                cantidad = input("Cantidad inválida. Ingrese la cantidad nuevamente: ")

            mercado.agregar_producto(nombre, cantidad, fecha_compra, fecha_vencimiento)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            mercado.exportar_a_texto()
            print("Exportación completada.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
