from django.shortcuts import render


def InicioViews(request):
    return render(request, 'Campus/inicio.html')


def LoginViews(request):
    return render(request, 'Campus/login.html')

