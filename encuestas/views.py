from django.shortcuts import render
from rest_framework import viewsets

from .models import Categoria
from .models import Encuesta
from .models import Pregunta
from .models import Opcion

from .serializer import CategoriaSerializer
from .serializer import EncuestaSerializer
from .serializer import PreguntaSerializer
from .serializer import OpcionSerializer


# Vista principal de la aplicación.
# Carga home.html cuando el usuario entra a la página principal.
def inicio(request):
    return render(request, 'encuestas/home.html')


# Vista personalizada para el error 404.
# Muestra una página cuando la dirección solicitada no existe.
def error_404(request, exception):
    return render(request, 'encuestas/404.html', status=404)


# Vista para las categorías de encuestas.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# Vista para las encuestas.
class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


# Vista para las preguntas.
class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


# Vista para las opciones de respuesta.
class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
