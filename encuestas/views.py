from django.shortcuts import render


def inicio(request):
    return render(request, 'encuestas/home.html')


def error_404(request, exception):
    return render(request, 'encuestas/404.html', status=404)