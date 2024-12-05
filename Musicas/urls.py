from django.urls import path

from .views import (
    MusicasView, 
    MusicasReadUpdateDeleteView,
    PlaylistViews, 
    PlaylistReadUpdateDeleteView,
    UserViews, 
    UserReadUpdateDeleteView,
)

# mapeiam as requisições para as views. Elas conectam os endpoints (como /musicas/ ou /usuarios/) com as funcionalidades apropriadas.
urlpatterns = [
    # Rotas para músicas
    path('', MusicasView.as_view(), name='musica-list'),  # Lista/cria músicas.
    path('musicas/<int:pk>/', MusicasReadUpdateDeleteView.as_view(), name='musica-detail'),  # Detalhes de uma música.

    # Rotas para álbuns
    path('playlist/', PlaylistViews.as_view(), name='playlist-list'),  # Lista/cria álbuns.
    path('playlist/<int:pk>/', PlaylistReadUpdateDeleteView.as_view(), name='playlist-detail'),  # Detalhes das playlist.

    # Rotas para usuários
    path('usuarios/', UserViews.as_view(), name='usuarios-list'),  # Lista/cria usuários.
    path('usuarios/<int:pk>/', UserReadUpdateDeleteView.as_view(), name='usuarios-detail'),  # Detalhes de um usuário.

]
