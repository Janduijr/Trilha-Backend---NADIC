from rest_framework.routers import SimpleRouter
from .views import CursoView, AvaliacaoView

router = SimpleRouter()
router.register('cursos', CursoView)
router.register('avaliacoes', AvaliacaoView)

