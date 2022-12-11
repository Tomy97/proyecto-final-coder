from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Campus.forms import *


def InicioViews(request):
    return render(request, 'inicio.html')


def LoginViews(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email'),
            contraseña = request.POST.get('contraseña')
            user = authenticate(request, email=email, contraseña=contraseña)
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
            contraseña=register.cleaned_data['contraseña'],
            nombre=register.cleaned_data['nombre'],
            apellido=register.cleaned_data['apellido'],
            localidad=register.cleaned_data['localidad'],
            edad=register.cleaned_data['edad'],
        )
        register = CreateUsuarioForms()
        return redirect('login')
    context = {
        'register': register
    }
    return render(request, "registro.html", context)


def AboutViews(request):
    return render(request, 'about.html')
