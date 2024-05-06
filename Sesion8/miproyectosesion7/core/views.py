from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Hola Mundo")
    titulo = "Casita"
    data = {
        "titulo":titulo,
    }
    return render(request,'core/home.html', data)

def carreras(request):
    #return HttpResponse("Hola Mundo")
    titulo = "Aqui estan las carreras"
    lista_carreras = [
        "Técnico Universitario en Informática",
        "Ingeniería en Informática",
        "Ingeniería de Ejecución de Software"

    ]
    data = {
        "titulo":titulo,
        "lista_carreras":lista_carreras,
    }
    return render(request,'core/carreras.html', data)

def docentes(request):
    #return HttpResponse("Hola Mundo")
    titulo="Aqui estan los profesores"
    data = {
        "titulo":titulo,
    }
    return render(request,'core/docentes.html', data)