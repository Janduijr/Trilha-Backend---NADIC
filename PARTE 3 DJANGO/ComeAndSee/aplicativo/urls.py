
from django.urls import path
from .views import listar_filme, filme_detalhes, index, review, listar_filme_meu, deletar_review

urlpatterns = [
    path('', index, name='index'),
    path('listar/filme', listar_filme, name='listar_filmes'),
    path('listar/filme/meus', listar_filme_meu, name='listar_filmes_meus'),
    path('listar/filme/detalhes/<int:id>', filme_detalhes, name='filme_detalhes'),
    path('listar/filme/detalhes/<int:id>/review', review, name='review'),
    path('listar/filme/detalhes/<int:id>/deletar', deletar_review, name='deletar_review'),
]
