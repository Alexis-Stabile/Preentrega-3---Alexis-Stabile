from AppNueva import views
from django.urls import path

urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('curso/',views.curso, name= 'cursos'),
    path('profesores/',views.profesores, name= 'profesores'),
    path('estudiantes/',views.estudiantes, name= 'estudiantes'),
    path('cursoformulario/',views.cursoformulario, name= 'cursoformulario'),
    path('profesorformulario/',views.profesorformulario, name= 'profesorformulario'),
    path('estudianteformulario/',views.estudianteformulario, name= 'estudianteformulario'),
    path('cursoformulario_2/',views.cursoformulario_2, name= 'cursoformulario_2'),
    path('busquedacomision/',views.busquedacomision, name= 'busquedacomision'),
    path('buscar/',views.buscar),

]
