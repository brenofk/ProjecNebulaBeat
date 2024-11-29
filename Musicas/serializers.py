from rest_framework import serializers
from .models import Musicas, Albuns, Playlist, User, MusicasAlbuns
 
class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'

class AlbunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albuns
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class MusicasAlbunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicasAlbuns
        fields = '__all__'  

class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'
