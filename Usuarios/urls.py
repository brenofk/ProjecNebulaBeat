from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsuariosView, UsuariosReadUpdateDeleteView

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuarios-list'), # Cria um novo usuario.
    path('<int:pk>/', UsuariosReadUpdateDeleteView.as_view(), name='usuarios-detail'),
]