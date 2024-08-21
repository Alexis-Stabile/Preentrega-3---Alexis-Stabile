from django.shortcuts import render
from django.http import HttpResponse
from AppNueva.forms import CursoFormulario, Buscar
from AppNueva.models import Curso, Estudiante, Profesor

# Views

def inicio(req):
    return render(req,'appnueva/padre.html/')

def curso(req):
    return render(req,'appnueva/cursos.html/')

def profesores(req):
    return render(req,'appnueva/profesores.html/')

def estudiantes(req):
    return render(req,'appnueva/estudiantes.html/')


def cursoformulario(req):

    if req.method == 'POST':

            curso =  Curso(nombre=req.POST['curso'],comision=req.POST['comision'])

            curso.save()

            return render(req,'appnueva/padre.html/')

    return render(req,"AppNueva/cursoformulario.html")

def estudianteformulario(req):

    if req.method == 'POST':

            estudiante =  Estudiante(nombre=req.POST['nombre'],apellido=req.POST['apellido'],email=req.POST['email'])

            estudiante.save()

            return render(req,'appnueva/padre.html/')

    return render(req,"AppNueva/estudianteformulario.html")

def profesorformulario(req):

    if req.method == 'POST':

            profesor =  Profesor(nombre=req.POST['nombre'],apellido=req.POST['apellido'],especialidad=req.POST['especialidad'])

            profesor.save()

            return render(req,'appnueva/padre.html/')

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



          








