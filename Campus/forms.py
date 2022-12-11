from django import forms
from django.forms import CharField, IntegerField, EmailField, DateField
from Campus.models import UsuarioModels


class LoginForm(forms.ModelForm):
    email = EmailField(label='', widget=forms.EmailInput(
        attrs={"class": 'form-control'}))
    contraseña = CharField(label='', widget=forms.PasswordInput(
        attrs={"class": 'form-control'}))

    class Meta:
        model = UsuarioModels
        fields = [
            'email',
            'contraseña'
        ]


class CreateUsuarioForms(forms.ModelForm):
    nombre = CharField(label='', widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    apellido = CharField(label='', widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    edad = IntegerField(label='', widget=forms.NumberInput(
        attrs={"class": 'form-control'}))
    localidad = CharField(label='', widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    email = EmailField(label='', widget=forms.EmailInput(
        attrs={"class": 'form-control'}))
    contraseña = CharField(label='', widget=forms.PasswordInput(
        attrs={"class": 'form-control'}))

    class Meta:
        model = UsuarioModels
        fields = [
            'nombre',
            'apellido',
            'edad',
            'localidad',
            'email',
            'contraseña'
        ]
