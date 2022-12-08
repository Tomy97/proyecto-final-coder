from django import forms
from django.forms import CharField, IntegerField, EmailField, DateField


class LoginForm(forms.Form):
    email = CharField(max_length=100)
    password = CharField(max_length=50)
    
class UsuarioForms(forms.Form):
    email = CharField(max_length=100)
    contraseña = CharField(max_length=50)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    localidad = CharField(max_length=50)
    edad = IntegerField()