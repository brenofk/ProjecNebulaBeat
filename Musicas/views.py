from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Musicas
from .serializers import MusicasSerializer

# Importando modelos e serializers

class MusicasView(APIView):
    def get(self, request):
        musicas = Musicas.objects.all()
        serializer = MusicasSerializer(musicas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
