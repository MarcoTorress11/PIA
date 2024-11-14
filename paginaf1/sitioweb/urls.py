# miapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('circuitos/', views.circuitos, name='circuitos'),
    path('escuderias/', views.escuderias, name='escuderias'),
    path('funcionamiento/', views.funcionamiento, name='funcionamiento'),
    path('pilotos/', views.pilotos, name='pilotos'),
    path('guardar_respuesta/', views.guardar_respuesta, name='guardar_respuesta'),
]
