from django.shortcuts import render


def InicioViews(request):
    return render(request, 'inicio.html')


def LoginViews(request):
    return render(request, 'login.html')

