from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from AppNueva.models import Curso

def saludo (request):
    return HttpResponse("Hola Django que tal")

def otra_vista (request):
    return HttpResponse("Hola de nuevo, en que andas")

def dia_de_hoy (request):
    hoy = date.today()
    return HttpResponse(f"hoy es {hoy}")

def muestra_nombre(self, nombre):
     return HttpResponse(f"buenos dias {nombre}, bienvenido a bordo")



def probando_template(request):

    nom = "Alexis"
    ap = "Stabile"

    diccionario = {"nombre":nom, "apellido": ap, "hoy":datetime.now()}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def agregar_curso(request, nom, com):
    curso = Curso (nombre=nom, comision=com)
    curso.save()

    return HttpResponse ("Curso Agregado")

   
