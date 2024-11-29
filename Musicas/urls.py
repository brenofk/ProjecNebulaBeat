from django.urls import path

from .views import (
    MusicasView, 
    MusicasReadUpdateDeleteView,
    AlbunsViews, 
    AlbunsReadUpdateDeleteView,
    UserViews, 
    UserReadUpdateDeleteView,
    PlaylistViews,
    PlaylistReadUpdateDeleteView,
)

urlpatterns = [
    # Rotas para músicas
    path('', MusicasView.as_view(), name='musica-list'),  # Lista/cria músicas.
    path('musicas/<int:pk>/', MusicasReadUpdateDeleteView.as_view(), name='musica-detail'),  # Detalhes de uma música.

    # Rotas para álbuns
    path('albuns/', AlbunsViews.as_view(), name='albuns-list'),  # Lista/cria álbuns.
    path('albuns/<int:pk>/', AlbunsReadUpdateDeleteView.as_view(), name='albuns-detail'),  # Detalhes de um álbum.

    # Rotas para usuários
    path('usuarios/', UserViews.as_view(), name='usuarios-list'),  # Lista/cria usuários.
    path('usuarios/<int:pk>/', UserReadUpdateDeleteView.as_view(), name='usuarios-detail'),  # Detalhes de um usuário.

    # Rotas para Playlist
    path('playlist/',PlaylistViews.as_view(), name='playlist-list'), # cria playlist.
    path('playlist/<int:pk>/', PlaylistReadUpdateDeleteView.as_view(), name='playlist-detail') # Detalhes de uma playlist.
]
