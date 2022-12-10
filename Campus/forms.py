from django import forms
from django.forms import CharField, IntegerField, EmailField, DateField
from django.contrib.auth.forms import UserCreationForm
from Campus.models import *


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


class RegisterForm(UserCreationForm):
    model = UsuarioModels
    fields = ['email', 'contraseña', 'nombre',
              'apellido', 'localidad', 'edad']
