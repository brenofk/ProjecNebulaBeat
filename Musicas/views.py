from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Musicas, Albuns, User, MusicasAlbuns, Comentario
from .serializers import (
    
    MusicasSerializer, 
    AlbunsSerializer, 
    UserSerializer, 
    MusicasAlbunsSerializer, 
    ComentarioSerializer,
)
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
    
   #  View para recuperar, atualizar ou deletar um Albuns específico.

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

class MusicasAlbunsReadUpdateDeleteView(APIView):
   #  View para recuperar, atualizar ou deletar um Musicas dentro de Albuns específico.

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

class ComentariosView(APIView):
    def post(self, request):
        # Instancia o serializer com os dados recebidos no 'request'
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            # Se o formato recebido estiver correto, salva os dados no banco
            serializer.save()
            # Retorna com o código 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se o serializer não for válido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ComentariosReadUpdateDeleteView(APIView):
    def get(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
