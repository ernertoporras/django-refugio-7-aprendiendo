from django.contrib import admin
from django.urls import path
from app_adopcion.views import adopcion

urlpatterns = [
    path('', adopcion),  #'index' es la ruta en navegador
                            #index es el nombre del archivo que va a abrir'

]