from django.shortcuts import render
from .models import Producto

# Create your views here.
def store(request):
    productos = Producto.objects.all()
    return render(request, 'store.html', {
        'productos': productos
    })