from rest_framework import serializers
from .models import Musicas, Albuns, User, MusicasAlbuns, Comentario
 
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

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'  
