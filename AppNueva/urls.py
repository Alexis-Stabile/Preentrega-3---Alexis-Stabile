from AppNueva import views
from django.urls import path
from AppNueva import views_clases

urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('curso/',views.curso, name= 'cursos'),
    path('profesores/',views.profesores, name= 'profesores'),
    path('estudiantes/',views.estudiantes, name= 'estudiantes'),
    path('About_me/',views.About_me, name= 'About_me'),
    path('cursoformulario/',views.cursoformulario, name= 'cursoformulario'),
    path('profesorformulario/',views.profesorformulario, name= 'profesorformulario'),
    path('estudianteformulario/',views.estudianteformulario, name= 'estudianteformulario'),
    path('cursoformulario_2/',views.cursoformulario_2, name= 'cursoformulario_2'),
    path('busquedacomision/',views.busquedacomision, name= 'busquedacomision'),
    path('buscar/',views.buscar),
    path('form-comun/', views.form_comun, name="Form-Comun"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),

]


urls_vistas_clases = [
    path('clases/lista/', views_clases.CursoListView.as_view(), name='Lista'),
    path('clases/detalle/<int:pk>/', views_clases.CursoDetalle.as_view(), name='Detalle'),
    path('clases/nuevo/', views_clases.CursoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.CursoUpdateView.as_view(), name='Editar'),
    path('clases/eliminar/<int:pk>', views_clases.CursoDeleteView.as_view(), name='Borrar'),
]

urlpatterns += urls_vistas_clases