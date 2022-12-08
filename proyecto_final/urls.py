from django.contrib import admin
from django.urls import path
from Campus.views import LoginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginViews)
]
