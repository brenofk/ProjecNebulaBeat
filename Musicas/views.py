from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Musicas
from .serializers import MusicasSerializer

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
