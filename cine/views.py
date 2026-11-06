from django.shortcuts import render

# Create your views here.
from .models import Pelicula

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()

    context = {
        'peliculas': peliculas,
        'total_peliculas': peliculas.count()
    }

    return render(request, 'cine/index.html', context)
