from django.shortcuts import render
from tarea.models import Family

# Create your views here.
def hola(request):
    return render(request, "miarchivo.html", context={}) 

def family(request):
    family_context = {
        'members': Family.objects.all()
    }

    return render(request, "family.html", family_context)

# Template -> View -> URL
# Primero creo el template (HTML)
# Despues creo una view en views.py y le paso el template .html (y le puedo pasar mas cosas)
# Finalmente creo la direccion URL del servidor (el /...)