from django.shortcuts import render

# Vista principal de la aplicación.
# Esta función carga el archivo home.html cuando el usuario entra a la página principal.
def inicio(request):
    return render(request, 'encuestas/home.html')

# Vista personalizada para el error 404.
# Se ejecuta cuando el usuario intenta entrar a una dirección que no existe.
# El status=404 indica que la respuesta corresponde a una página no encontrada.
def error_404(request, exception):
    return render(request, 'encuestas/404.html', status=404)