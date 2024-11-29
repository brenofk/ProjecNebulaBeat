from django.db import models
from Usuarios.models import User

# Create your models here.

    # novos albuns
class Albuns(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()

    #novas musicas
class Musicas(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    albuns = models.ForeignKey(Albuns, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    url_reproducao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
    # novas musicas dentro dos albuns.
class MusicasAlbuns(models.Model):
    musicas = models.ForeignKey(Musicas, on_delete=models.CASCADE)
    albuns = models.ForeignKey(Albuns, on_delete=models.CASCADE)

    # novas playlist
class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    # novos comentrarios
class Comentario(models.Model):
    nota = models.CharField(max_length=10)
    data = models.DateField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nota
