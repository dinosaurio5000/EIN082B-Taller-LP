from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera
from .models import Docente
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
    #lista_carreras = [
    #   "Técnico Universitario en Informática",
    #   "Ingeniería en Informática",
    #   "Ingeniería de Ejecución de Software"
    #]
    lista_carreras = Carrera.objects.all()

    data = {
        "titulo":titulo,
        "lista_carreras":lista_carreras,
    }
    return render(request,'core/carreras.html', data)

def docentes(request):
    #return HttpResponse("Hola Mundo")
    titulo="Aqui estan los profesores"
    lista_docentes = Docente.objects.all()
    data = {
        "titulo":titulo,
        "lista_docentes":lista_docentes,
    }
    return render(request,'core/docentes.html', data)