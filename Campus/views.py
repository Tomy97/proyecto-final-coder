from django.shortcuts import render


def InicioViews(request):
    return render(request, 'index.html')


def LoginViews(request):
    return render(request, 'login.html')
