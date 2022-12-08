from django.contrib import admin
from django.urls import path
from Campus.views import LoginViews, InicioViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioViews, name="home"),
    path('login/', LoginViews, name="login")
]
