from django.db import models

#modelos

class Curso(models.Model):
    nombre = models.CharField(max_length=45)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email  = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.especialidad}"
    


