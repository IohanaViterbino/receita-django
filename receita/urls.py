from .views import AvaliacaoViewSet, CategoriaViewSet, ReceitaViewSet, UserViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'receitas', ReceitaViewSet, basename='receitas')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacoes')
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('api/', include(router.urls)),
]