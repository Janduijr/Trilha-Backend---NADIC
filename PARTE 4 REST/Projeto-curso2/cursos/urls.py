from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AvaliacoesAPIView, CursosAPIView, AvaliacaoAPIView, CursoAPIView, AvaliacaoViewSet, CursoViewSet

routers = SimpleRouter()
routers.register('cursos', CursoViewSet)
routers.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
]