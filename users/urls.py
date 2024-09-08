from django.urls import path
from users import views
from django.views.generic import TemplateView
from .views import custom_logout



urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', custom_logout, name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarContrasenia.as_view(), name="CambiarPass")
]