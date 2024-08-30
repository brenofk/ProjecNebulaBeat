from django.db import models
from Usuarios.models import Usuarios

# Create your models here.

class Musicas(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    url_reproducao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    nota = models.CharField(max_length=10)
    data = models.DateField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.nota

