from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Genero)
admin.site.register(models.Marca)
admin.site.register(models.Categoria)
admin.site.register(models.Producto)