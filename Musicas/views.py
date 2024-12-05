from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Musicas, Playlist, MusicasPlaylist
from Usuarios.models import User
from .serializers import (
    
    MusicasSerializer, 
    PlaylistSerializer, 
    UserSerializer, 
    MusicasPlaylistSerializer, 
)

#  são responsáveis por lidar com as requisições HTTP (GET, POST, PUT, DELETE). Elas conectam os dados do banco de dados (através dos models) 
# com o que o usuário final vê e interage.


# Importando modelos e serializers

class MusicasView(APIView):
    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = MusicasSerializer(data=request.data)
        
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
class PlaylistViews(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        playlist = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PlaylistReadUpdateDeleteView(APIView):
    
    # View para recuperar, atualizar ou deletar uma Playlist específica.

    def get(self, request, pk):
        # Busca a playlist pelo 'pk' e retorna um erro 404 se não encontrada.
        playlist = get_object_or_404(Playlist, pk=pk)

        # Serializa os dados da playlist.
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # Busca a playlist pelo 'pk' e retorna um erro 404 se não encontrada.
        playlist = get_object_or_404(Playlist, pk=pk)

        # Inicializa o serializer com os dados recebidos na requisição.
        serializer = PlaylistSerializer(playlist, data=request.data)

        if serializer.is_valid():
            # Se os dados forem válidos, salva a playlist com as atualizações.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Se o serializer não for válido, retorna os erros de validação.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Busca a playlist pelo 'pk' e retorna um erro 404 se não encontrada.
        playlist = get_object_or_404(Playlist, pk=pk)

        # Deleta a playlist.
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViews(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'detail': 'Usuario não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Classe dos Albuns de Musicas.

class MusicasPlaylistReadUpdateDeleteView(APIView):
   #  View para recuperar, atualizar ou deletar um Musicas dentro de Albuns específico.

    def get(self, request, pk):
        MusicasPlaylist = get_object_or_404(MusicasPlaylist, pk=pk)

        try:
            musicasPlaylist = MusicasPlaylist.objects.get(pk=pk)
        except MusicasPlaylist.DoesNotExist:
            return Response({'detail': 'Musicas da playlisy não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MusicasPlaylistSerializer(musicasPlaylist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        musicasPlaylist = get_object_or_404(MusicasPlaylist, pk=pk)
        serializer = MusicasPlaylistSerializer(musicasPlaylist, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        musicasPlaylist = get_object_or_404(MusicasPlaylist, pk=pk)
        musicasPlaylist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        return Response(status=status.HTTP_204_NO_CONTENT)
