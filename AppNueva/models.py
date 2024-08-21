from django.db import models

#modelos

class Curso(models.Model):
    nombre = models.CharField(max_length=45)
    comision = models.IntegerField()
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email  = models.EmailField()
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=60)
    


