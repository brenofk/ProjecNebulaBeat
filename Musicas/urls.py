from django.urls import path

from .views import (
    MusicasView, 
    MusicasReadUpdateDeleteView,
    AlbunsViews, 
    AlbunsReadUpdateDeleteView,
    UserViews, 
    UserReadUpdateDeleteView,
    ComentariosView,
    ComentariosReadUpdateDeleteView,
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

    # Rotas para comentários
    path('comentarios/', ComentariosView.as_view(), name='comentarios-list-create'),  # Para criar/listar
    path('comentarios/<int:pk>/', ComentariosReadUpdateDeleteView.as_view(), name='comentarios-detail'),  # Para editar/visualizar/excluir

]
