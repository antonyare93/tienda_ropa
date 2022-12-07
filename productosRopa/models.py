from email.policy import default
from django.db import models

# Create your models here.
class Genero(models.Model):
    genero_inicial = models.CharField(max_length=1)
    genero_detalle = models.CharField(max_length=30)

    def __str__(self):
        return self.genero_detalle

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_categoria

class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=70)
    precio_compra = models.FloatField(null=False, blank=False, default=0.0)
    precio_venta = models.FloatField(null=False, blank=False, default=0.0)
    link_to_origin = models.CharField(max_length=120)
    link_to_image = models.CharField(max_length=120)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero, null=False)

    def __str__(self):
        return self.nombre_producto + " - " + str(self.marca)