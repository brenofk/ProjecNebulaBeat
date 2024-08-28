from django.db import models

# Create your models here.

class Musicas(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    url_reproducao = models.CharField(max_length=200)

def __str__(self):
    return self.titulo
