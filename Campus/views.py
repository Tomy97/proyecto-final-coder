from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from Campus.forms import *


def InicioViews(request):
    return render(request, 'inicio.html')


def LoginViews(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('No se pudo autenticar el usuario')
        else:
            print('no se pudo validar')
    form = LoginForm()
    context = {
        "login": form
    }
    return render(request, 'login.html', context)


def RegistroViews(request):
    register = CreateUsuarioForms(request.POST or None)
    if register.is_valid():
        usuario = UsuarioModels(
            email=register.cleaned_data['email'],
            username=register.cleaned_data['email'],
            password=make_password(register.cleaned_data['password']),
            first_name=register.cleaned_data['nombre'],
            last_name=register.cleaned_data['apellido'],
            localidad=register.cleaned_data['localidad'],
            edad=register.cleaned_data['edad'],
        )
        usuario.save()
        register = CreateUsuarioForms()
        return redirect('login')
    context = {
        'register': register
    }
    return render(request, "registro.html", context)


def AboutViews(request):
    return render(request, 'about.html')
