from django.contrib import admin
from django.urls import path
from Campus.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioViews, name="home"),
    path('login/', LoginViews, name="login"),
    path('registro/', RegistroViews, name="register")
]

