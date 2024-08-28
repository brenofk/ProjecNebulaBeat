from rest_framework import serializers
from .models import Musicas

class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = '__all__'