from django.contrib import admin
from .models import Musicas

# Register your models here.

@admin.register(Musicas)
class MusicasAdmin(admin.ModelAdmin):
    list_display = ('titulo','artista','album','genero','url_reproducao')
