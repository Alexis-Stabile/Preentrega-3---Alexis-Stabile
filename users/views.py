from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, Userform
from django.urls import reverse_lazy
from users.models import Imagen
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppNueva/padre.html")

        msg_login = "Usuario o Contraseña Incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


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


def custom_logout(request):

    logout(request)
    return redirect('inicio')


@login_required
def editar_perfil(request):
    
    usuario = request.user

    if request.method == 'POST': 
      
        miFormulario = Userform(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():  
            if miFormulario.cleaned_data.get('imagen'):
                
                if Imagen.objects.filter(user=usuario).exists():
                   
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()  
                else:
                
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()  

            
            miFormulario.save()

           
            return render(request, "AppNueva/padre.html")

    else: 
        miFormulario = Userform(instance=usuario)

    
    return render(request, "users/editor_perfil.html", {"mi_form": miFormulario, "usuario": usuario})    




class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")
