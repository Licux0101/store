from django.shortcuts import render

def home(request):
    return render(request, 'base.html')  # O mejor 'home.html' si tienes una plantilla separada

def productos(request):
    productos_list = [
        {'nombre': 'Producto 1', 'precio': 100},
        {'nombre': 'Producto 2', 'precio': 200},
    ]
    return render(request, 'productos.html', {'productos': productos_list})

def contactos(request):
    return render(request, 'contactos.html')  # Usa la ruta directa si 'contactos.html' está en la carpeta templates
