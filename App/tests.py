from django.test import TestCase
from .models import Categoria, Producto, Cliente

class ModeloTests(TestCase):
    def test_creacion_categoria(self):
        categoria = Categoria.objects.create(nombre='Electrónicos')
        self.assertEqual(str(categoria), 'Electrónicos')

    def test_creacion_producto(self):
        categoria = Categoria.objects.create(nombre='Electrónicos')
        producto = Producto.objects.create(nombre='Teléfono', precio=500, categoria=categoria)
        self.assertEqual(str(producto), 'Teléfono')

    def test_creacion_cliente(self):
        cliente = Cliente.objects.create(nombre='Juan', email='juan@gmail.com')
        self.assertEqual(str(cliente), 'Juan')
