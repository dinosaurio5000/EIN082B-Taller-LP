from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    #return HttpResponse("Hola Mundo")
    return render(request,'core/index.html')

def profesores(request):
    return HttpResponse("Profesores")

def carreras(request):
    return HttpResponse("Carreras")

