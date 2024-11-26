from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Musicas, Albuns, Usuarios, MusicasAlbuns
from .serializers import MusicasSerializer, AlbunsSerializer, UsuariosSerializer, MusicasAlbunsSerializer

# Importando modelos e serializers

class MusicasView(APIView):
    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = MusicasSerializer(data=request.data, many=True)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()
            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        musicas = Musicas.objects.all()
        serializer = MusicasSerializer(musicas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MusicasReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        musicas = get_object_or_404(Musicas, pk=pk)
        serializer = MusicasSerializer(musicas)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        musicas = get_object_or_404(Musicas, pk=pk)
        
        serializer = MusicasSerializer(musicas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        musicas = get_object_or_404(Musicas, pk=pk)
        musicas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# TUDO ABAIXO E UM TESTE DA RELACAO DE 1XN
class AlbunsViews(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = AlbunsSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        albuns = Albuns.objects.all()
        serializer = AlbunsSerializer(albuns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class AlbunsReadUpdateDeleteView(APIView):
    
   #  View para recuperar, atualizar ou deletar um professor específico.

    def get(self, request, pk):
        albuns = get_object_or_404(Albuns, pk=pk)

        try:
            albuns = Albuns.objects.get(pk=pk)
        except Albuns.DoesNotExist:
            return Response({'detail': 'Albun não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AlbunsSerializer(albuns)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        albuns = get_object_or_404(Albuns, pk=pk)
        serializer = AlbunsSerializer(albuns, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        albuns = get_object_or_404(Albuns, pk=pk)
        albuns.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class UsuariosViews(APIView):

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UsuariosReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        usuarios = get_object_or_404(Usuarios, pk=pk)
        try:
            usuarios = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response({'detail': 'Usuario não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
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


# Classe dos Albuns de Musicas.

class MusicasAlbunsReadUpdateDeleteView(APIView):
   #  View para recuperar, atualizar ou deletar um professor específico.

    def get(self, request, pk):
        musicasAlbuns = get_object_or_404(MusicasAlbuns, pk=pk)

        try:
            musicasAlbuns = MusicasAlbuns.objects.get(pk=pk)
        except MusicasAlbuns.DoesNotExist:
            return Response({'detail': 'Musicas Albuns não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MusicasAlbunsSerializer(musicasAlbuns)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        musicasAlbuns = get_object_or_404(MusicasAlbuns, pk=pk)
        serializer = MusicasAlbunsSerializer(musicasAlbuns, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        musicasAlbuns = get_object_or_404(MusicasAlbuns, pk=pk)
        musicasAlbuns.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


