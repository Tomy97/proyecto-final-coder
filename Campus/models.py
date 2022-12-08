from django.db import models
from django.db.models import CharField, DateField, DateTimeField, TextField, IntegerField, EmailField

class UniversidadModels(models.Model):
    nombre = CharField(max_length=50)
    localizacion = CharField(max_length=100)
    zip_code = IntegerField()
    description = TextField(max_length=2000)
    contacto = EmailField(max_length=100)
    
class AlumnoModels(models.Model):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    email = TextField(max_length=100)
    localidad = CharField(max_length=100)
    fecha_nac = DateField()
    contacto = IntegerField()

class ProfesorModels(models.Model):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    email = TextField(max_length=100)
    materia_a_cargo = CharField(max_length=50)
    
class UsuarioModels(models.Model):
    email = CharField(max_length=100)
    contraseña = CharField(max_length=50)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    localidad = CharField(max_length=50)
    edad = IntegerField()
    
    
    
class MateriaModels(models.Model):
    nombre = CharField(max_length=50)
    nota = CharField(max_length=5)
    promedio = CharField(max_length=5)
