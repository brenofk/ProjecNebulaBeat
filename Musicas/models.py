from django.db import models

# Os models representam as tabelas no banco de dados. Cada classe no arquivo models.py mapeia para uma tabela no banco de dados e define os campos e suas propriedades.
# Função:
# Criar, ler, atualizar e excluir registros no banco de dados.
# Fornecer a lógica de negócio para manipulação de dados.

# Create your models here.

    # Modelo Playlist.
class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return self.nome # Retorna nome da Playlist.
    
    # Modelo musicas
class Musicas(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="musicas") # Referencia a playlist.
    genero = models.CharField(max_length=100)
    url_reproducao = models.URLField(max_length=200)  # Valida URL automaticamente.

    def __str__(self):
        return self.titulo
    
    # Modelo de Relacao Musica-Albun.
class MusicasPlaylist(models.Model):
    musicas = models.ForeignKey(Musicas, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.musicas.titulo} - {self.playlist.nome}'  # Exibe título da música e nome da playlist.

