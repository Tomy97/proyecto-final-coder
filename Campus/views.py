from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Campus.forms import LoginForm


def InicioViews(request):
    return render(request, 'inicio.html')


def LoginViews(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print('El usuario esta registrado')
            login(request, user)
            return redirect('inicio')
        else:
            print('El usuario no esta registrado')
            return render(request, 'login', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')
