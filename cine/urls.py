from django.urls import path

from . import views

app_name = "cine"

urlpatterns = [
    path("", views.lista_peliculas, name="lista_peliculas"),
]
