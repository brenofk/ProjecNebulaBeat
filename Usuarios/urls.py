from django.urls import path
from .views import UserRegisterAPIView

urlpatterns = [
    
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('<int:pk>/', UserRegisterAPIView.as_view(), name='user-update'),
    path('', UserRegisterAPIView.as_view(), name='user-list'),  # Adiciona esta linha
]
