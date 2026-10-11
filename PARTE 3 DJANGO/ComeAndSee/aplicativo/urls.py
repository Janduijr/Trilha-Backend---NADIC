
from django.urls import path
from .views import listar_filme, filme_detalhes

urlpatterns = [
    path('listar/filme', listar_filme, name='listar_filmes'),
    path('listar/filme/detalhes/<int:id>', filme_detalhes, name='filme_detalhes'),
]
