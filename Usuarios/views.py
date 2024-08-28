from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Usuarios
from .serializers import UsuariosSerializer

# Importando modelos e serializers

class UsuariosView(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuariosReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        usuarios = get_object_or_404(Usuarios, pk=pk)
        serializer = UsuariosSerializer(usuarios)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        usuarios = get_object_or_404(Usuarios, pk=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        usuarios = get_object_or_404(Usuarios, pk=pk)
        usuarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)