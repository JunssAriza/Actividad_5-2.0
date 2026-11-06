from django.contrib import admin

# Register your models here.

from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sala_horario', 'precio_boleta', 'estreno')
    search_fields = ('titulo', 'sala_horario')
    list_filter = ('titulo',)