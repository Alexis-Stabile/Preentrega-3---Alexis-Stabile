from django.shortcuts import render
from django.http import HttpResponse
import locale
from datetime import datetime
from AppNueva.forms import CursoFormulario, Buscar
from AppNueva.models import Curso, Estudiante, Profesor
from .forms import UserRegisterForm
from AppNueva.forms import CursoFormulario, BuscaCursoForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Views

def inicio(req):
    return render(req,'AppNueva/padre.html/')

@login_required
def curso(req):
    return render(req,'AppNueva/cursos.html/')

@login_required
def profesores(req):
    return render(req,'AppNueva/profesores.html/')

@login_required
def estudiantes(req):
    return render(req,'AppNueva/estudiantes.html/')

def About_me(req):
     return render(req,'AppNueva/About_me.html/')

def About_me(request):
     locale.setlocale(locale.LC_ALL, 'es_ES')
     hoy = datetime.now().strftime("%A %d de %B, %Y")
     return render(request, 'AppNueva/About_me.html/', {'hoy': hoy})


def cursoformulario(req):

    if req.method == 'POST':

            curso =  Curso(nombre=req.POST['curso'],comision=req.POST['comision'])

            curso.save()

            return render(req,'AppNueva/padre.html/')

    return render(req,"AppNueva/cursoformulario.html")

def estudianteformulario(req):

    if req.method == 'POST':

            estudiante =  Estudiante(nombre=req.POST['nombre'],apellido=req.POST['apellido'],email=req.POST['email'])

            estudiante.save()

            return render(req,'AppNueva/padre.html/')

    return render(req,"AppNueva/estudianteformulario.html")

def profesorformulario(req):

    if req.method == 'POST':

            profesor =  Profesor(nombre=req.POST['nombre'],apellido=req.POST['apellido'],especialidad=req.POST['especialidad'])

            profesor.save()

            return render(req,'AppNueva/padre.html/')

    return render(req,"AppNueva/profesorformulario.html")



def cursoformulario_2(request):

      if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])

                  curso.save()

                  return render(request,'appnueva/padre.html/')
      else:
            miFormulario = CursoFormulario()


      return render(request, "AppNueva/cursoformulario_2.html", {"miFormulario": miFormulario})

def busquedacomision(request):
     return render (request, "AppNueva/busquedacomision.html")



def buscar(request):
    if request.GET['comision']:

        comision = request.GET['comision']

        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, "AppNueva/resultadobusqueda.html", {"cursos": cursos, "comision": comision})           
    else:

        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def form_comun(request):

    if request.method == 'POST':

        curso =  Curso(nombre=request.POST['curso'],camada=request.POST['comision'])
        curso.save()

        return render(request, "AppNueva/padre.html")

    return render(request,"AppNueva/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["comision"])
            curso.save()
            return render(request, "AppNueva/padre.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppNueva/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppNueva/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppNueva/buscar_form_con_api.html", {"miFormulario": miFormulario})

def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"AppNueva/padre.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})
          








