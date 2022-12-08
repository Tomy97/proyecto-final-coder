from django import forms
from django.forms import CharField, IntegerField, EmailField


class LoginForm(forms.Form):
    email = CharField(max_length=100)
    password = CharField(max_length=50)