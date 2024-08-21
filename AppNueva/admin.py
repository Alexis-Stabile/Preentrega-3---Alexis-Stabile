from django.contrib import admin
from AppNueva.models import Curso, Estudiante, Profesor

# Aqui hago el registro de mis modelos

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)