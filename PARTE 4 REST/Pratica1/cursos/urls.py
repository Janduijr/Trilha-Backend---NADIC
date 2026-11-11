from rest_framework.routers import SimpleRouter
from .views import CursosViewSet, AvaliacaoViewSet

routers = SimpleRouter()
routers.register('cursos', CursosViewSet)
routers.register('avaliacoes', AvaliacaoViewSet)