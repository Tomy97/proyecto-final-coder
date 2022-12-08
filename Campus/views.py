from django.shortcuts import render


def LoginViews(request):
    return render(request, 'login.html')