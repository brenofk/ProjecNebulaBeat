from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializers(serializers.ModelSerializers):
    class Meta:
        model = Usuarios
        fields = '__all__'