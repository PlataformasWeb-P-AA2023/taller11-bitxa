from django.urls import path
from .views import *

urlpatterns = [
    path('listar_edificios/', listar_edificios, name='listar_edificios'),
    path('listar_departamentos/', listar_departamentos, name='listar_departamentos'),
    path('crear_edificio/', crear_edificio, name='crear_edificio'),
    path('crear_departamento/', crear_departamento, name='crear_departamento'),
    path('editar_departamento/<int:id>/', editar_departamento, name='editar_departamento'),
    path('editar_edificio/<int:id>/', editar_edificio, name='editar_edificio'),
    path('eliminar_departamento/<int:id>/', eliminar_departamento, name='eliminar_departamento'),
    path('eliminar_edificio/<int:id>/', eliminar_edificio, name='eliminar_edificio'),
]
