from django.shortcuts import render
from mi_aplicacion.models import Clase1, Clase2, Clase3

def index(request):
    return render(request, 'mi_aplicacion/index.html')

def agregar_datos(request):
    if request.method == 'POST':
        campo1 = request.POST.get('campo1')
        campo2 = request.POST.get('campo2')
        campo3 = request.POST.get('campo3')
        campo4 = request.POST.get('campo4')
        campo5 = request.POST.get('campo5')
        campo6 = request.POST.get('campo6')

        objeto1 = Clase1(campo1=campo1, campo2=campo2)
        objeto1.save()

        objeto2 = Clase2(campo3=campo3, campo4=campo4)
        objeto2.save()

        objeto3 = Clase3(campo5=campo5, campo6=campo6)
        objeto3.save()

    return render(request, 'mi_aplicacion/agregar_datos.html')

def buscar_datos(request):
    if request.method == 'POST':
        campo_busqueda = request.POST.get('campo_busqueda')
        resultados = Clase1.objects.filter(campo1__icontains=campo_busqueda)
        return render(request, 'mi_aplicacion/resultados_busqueda.html', {'resultados': resultados})

    return render(request, 'mi_aplicacion/buscar_datos.html')
