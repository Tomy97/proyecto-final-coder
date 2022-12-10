from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
    if request.method == 'POST':  
        form = UsuarioForms(request.POST)
        usuario = UsuarioModels(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            localidad = request.POST['localidad'],
            edad = request.POST['edad'],
            email = request.POST['email'],
            contraseña = request.POST['contraseña'],
        )
        usuario.save()
        formulario = UsuarioForms()
    return render(request, "formulario_usuario.html", {"formulario": formulario})


