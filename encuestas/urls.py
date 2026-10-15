from django.urls import path, include
from rest_framework import routers
from encuestas import views

enrutador = routers.DefaultRouter()

enrutador.register(r'categorias', views.CategoriaViewSet)
enrutador.register(r'encuestas', views.EncuestaViewSet)
enrutador.register(r'preguntas', views.PreguntaViewSet)
enrutador.register(r'opciones', views.OpcionViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]
