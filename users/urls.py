from django.urls import path
from users import views
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', TemplateView.as_view(template_name='AppNueva/padre.html'), name="Logout")
]