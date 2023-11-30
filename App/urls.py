from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar/', views.buscar, name='buscar'),
]
