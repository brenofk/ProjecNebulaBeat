from django.urls import path
from .views import (
    MusicasView, 
    MusicasReadUpdateDeleteView,
    AlbunsViews, 
    AlbunsReadUpdateDeleteView,
    UsuariosViews, 
    UsuariosReadUpdateDeleteView
)

urlpatterns = [
    # Rotas para músicas
    path('', MusicasView.as_view(), name='musica-list'),  # Lista/cria músicas
    path('musicas/<int:pk>/', MusicasReadUpdateDeleteView.as_view(), name='musica-detail'),  # Detalhes de uma música

    # Rotas para álbuns
    path('albuns/', AlbunsViews.as_view(), name='albuns-list'),  # Lista/cria álbuns
    path('albuns/<int:pk>/', AlbunsReadUpdateDeleteView.as_view(), name='albuns-detail'),  # Detalhes de um álbum

    # Rotas para usuários
    path('usuarios/', UsuariosViews.as_view(), name='usuarios-list'),  # Lista/cria usuários
    path('usuarios/<int:pk>/', UsuariosReadUpdateDeleteView.as_view(), name='usuarios-detail'),  # Detalhes de um usuário
]
