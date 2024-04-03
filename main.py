import logging
from models.mercado import Mercado
from utils.validaciones import validar_fecha, validar_cantidad

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    mercado = Mercado()
    mercado.cargar_desde_archivo("productos.txt")

    while True:
        logger.info("\n1. Agregar producto")
        logger.info("\n2. Exportar a archivo")
        logger.info("\n3. buscar producto")
        logger.info("\n4. Salir")

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
            logger.info("Producto agregado correctamente.")

        elif opcion == "2":
            mercado.exportar_a_texto()
            logger.info("Exportación completada.")
            
        elif opcion == "3":
            nombre_busqueda = input("Ingrese el nombre del producto a buscar: ")
            if mercado.buscar_producto(nombre_busqueda):
                logger.info("El producto existe en el mercado.")
            else:
                logger.info("El producto no existe en el mercado.")

        elif opcion == "4":
            logger.info("Saliendo del programa...")
            break

        else:
            logger.warning("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
