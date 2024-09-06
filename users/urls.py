from django.urls import path
from users import views
#from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import custom_logout



urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', custom_logout, name="Logout"),
]