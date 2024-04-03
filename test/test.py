import sys

sys.path.append("D:\\Nueva carpeta\\Entrega-tecnicas-de-programacion-main\\models")

from producto import Producto
from datetime import datetime, timedelta
import unittest

class TestProducto(unittest.TestCase):
    def test_esta_vencido(self):
        # Caso 1: producto vencido
        producto_vencido = Producto("Producto vencido", 10, "2025-01-03", "2022-01-02")
        self.assertTrue(producto_vencido.esta_vencido())

        # Caso 2: producto no vencido
        fecha_actual = datetime.now()
        fecha_vencimiento = fecha_actual + timedelta(days=1)  # Vence mañana
        producto_no_vencido = Producto("Producto no vencido", 5, "2022-01-01", fecha_vencimiento.strftime("%Y-%m-%d"))
        self.assertFalse(producto_no_vencido.esta_vencido())

if __name__ == '__main__':
    unittest.main()