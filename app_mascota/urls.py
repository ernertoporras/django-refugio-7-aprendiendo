from django.contrib import admin
from django.urls import path,include
from app_mascota.views import index,mascota_view,mascota_list



urlpatterns = [
    path('', index, name='index'),  #'index' es la ruta en navegador
    path('nuevo',mascota_view ,name='mascota_crear'),
    path('listar',mascota_list ,name='mascota_listar'),
]




