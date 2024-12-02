from rest_framework import serializers
from .models import Musicas, Playlist, User, MusicasPlaylist

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