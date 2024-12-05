from rest_framework import serializers
from .models import Musicas, Playlist, MusicasPlaylist
from Usuarios.models import User

# Serializers, são responsáveis por converter dados complexos (como objetos Python ou queryset) em 
# formatos mais simples (como JSON) e vice-versa.

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__' 

class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class MusicasPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicasPlaylist
        fields = '__all__'  