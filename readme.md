#Version de python 3.12.14

#django==5.1

#Funcionamiento de esta pre entrega: 

#Instalacion de Django y puesta en marcha de entorno virtual. 

#Creacion de Database.

#Creacion de Views y Conexion con Urls a traves de importacion y creacion de paths.

#Plantillas HTML.

#Configuracion de Loader

#Creacion de app (python manage.py startapp AppNueva)

#creacion de modelos para nuestras BB.DD (clases)

#activamos la app en settings.py en Proyecto1 (python manage.py check AppNueva)

#hacemos la migracion (python manage.py makemigrations)

#crear nuestros modelos en BB.DD (python manage.py sqlmigrate AppNueva 0001), complementamos con (python manage.py migrate)

#si queremos agregar info a nuestra BB.DD a traves de python manage.py shell e importando el modelo que necesitemos en views del proyecto creamos una funcion para poder agregar parametros por enlaces

#Actualizamos los cambios en urls creando la importacion del modulo desde (AppNueva.models) y creamos el path

#views

#creacion de vistas dentro de nuestra app

#creacion de un modulo llamado "urls.py" dentro de nuestra app (inicio, cursos, profesores, estudiantes)

#hacemos las importaciones correspondientes

#creacion de paths dentro de urls.py

#conexion de urls de mi app con las del proyecto (dentro de urls.py en proyecto y en urlpatterns agregamos path('AppNueva/',include('AppNueva.urls')))

#creamos una carpeta de templates en nuestra app (C:\Users\azulg\Desktop\3 pre entrega\AppNueva\templates), y una sub carpeta(C:\Users\azulg\Desktop\3 pre entrega\AppNueva\templates\AppNueva), donde agregaremos todas las paginas html segun las vistas que tenga mi app

#Renderizado, en nuesrta carpeta view modificamos los return, asignandole las nuevas rutas de los archivos html que hemos creado

#Mejore el estilo con Boodstrap, para ello descargamos el template que elegi

#Creacion de carpeta Static done pego todos los archivos del template que descarge de Boodstrap

#Muevo el archivo index.html a mis \templates\appnueva remplazando al de inicio.

#configuramos {% load static %} y linkeamos con el archivo CSS

#agregue imagenes acordes a lo que queria mostras en la paginaweb, como asi tambien modifique el texto para ello modifique el codigo en el archivo index.html

#Herencias de template, creo un nuevo template en mi app (padre.html), donde pego todo el contenido de index.html seleccionando la parte que quiero que quede estática, para ello hago uso de los siguientes comandos:

{% load static %}
{% block contenidoquecambia %}
{% endblock %}

#Actualizacion de los renderizados en views de la app y comandos desde urls.py agregando las nuevas rutas que hagan el nexo al archivo padre:


#Superusuario: a traves del comando python manage.oy createsuperuser hago la creacion de un super usuario que tendra todos los privilegios para administrar la BB.DD

#Adicionalmente, desde Html puedo agregar usuarios alternativos y asignarles los respectivos permisos (ver o editar)

#El proximo paso, es darle a mi front end todos mis modelos, para ello importo los modelos en la carpeta de admin y les otorgo los register:

from django.contrib import admin
from AppNueva.models import Curso, Estudiante, Profesor

#Aqui hago el registro de mis modelos:
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)

#formularios: en views, hacemos las importaciones de nuestros modelos, para poder dar luego accion a nuestros formularios, seguidamente, configuramos los path en urls y finalmente mi archivo html, de esta manera cada modelo contiene su propio formulario

#creacion de formularios appi from django -> forms.py from django import forms

#importamos forms from django y creamos clase

#busqueda con form creamos nuevas views, urls y archivos html para poder buscar comisiones a traves de html:

#http://127.0.0.1:8000/AppNueva/inicio/

#http://127.0.0.1:8000/AppNueva/estudianteformulario/

#http://127.0.0.1:8000/AppNueva/cursoformulario/

#http://127.0.0.1:8000/AppNueva/profesorformulario/

#formulario para buscar en nuestra BBDD:

#http://127.0.0.1:8000/AppNueva/cursoformulario_2/

    


    


