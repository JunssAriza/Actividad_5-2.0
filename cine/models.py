from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(
        max_length= 120,
        verbose_name= "Titulo de la pelicula"
    )
    sala_horario = models.DateField(
        verbose_name= "Fecha y Hora"
    )
    precio_boleta = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Precio de la boleta"
    )
    estreno = models.DateField(
        verbose_name= "Fecha de estreno"
    )

    class Meta:
        verbose_name = "Pelicula",
        verbose_name_plural = "Peliculas"
        ordering =['-estreno']

    def __str__(self):
        return self.titulo