from django.shortcuts import render
from django.http import HttpResponse


from pendientes.models import Tarea #importar la clase tarea de mode

from random import randint
# Create your views here.

def index(request):
    listita=Tarea.objects.all()#consulta la BD y guardamos todos
                                  #los reguistro de la tabla tarea
                                  


    persona={
        "nombre":"nestor",
        "edad":27,
        "hobbies":["futbol","tenis","futsal","bailar"],
        "lista_tarea":listita,}

    return render(request,"inicio.html",persona)

def tarea(request):
    return HttpResponse("este es una tarea")
