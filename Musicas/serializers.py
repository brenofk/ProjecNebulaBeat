from rest_framework import serializers
from .models import Musicas, Albuns, Usuarios, MusicasAlbuns
 
class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'

class AlbunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albuns
        fields = '__all__' 

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'  

class MusicasAlbunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicasAlbuns
        fields = '__all__'  
