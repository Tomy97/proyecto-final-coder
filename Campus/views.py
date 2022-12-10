from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from Campus.forms import UsuarioForms
from Campus.models import UsuarioModels


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

def RegistroViews(request):
    register = UserCreationForm()
    print(register)
    if request.method == "POST":
        register = UserCreationForm(request.POST)
        if  register.is_valid():
            register.save()
            return redirect('login')
    return render(request, "registro.html", {"register": register})


