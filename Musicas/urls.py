from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MusicasView, MusicasReadUpdateDeleteView

urlpatterns = [
    path('', MusicasView.as_view(), name='musica-list'), # Cria uma nova musica
    path('<int:pk>/', MusicasReadUpdateDeleteView.as_view(), name='musicas-detail'),
]
