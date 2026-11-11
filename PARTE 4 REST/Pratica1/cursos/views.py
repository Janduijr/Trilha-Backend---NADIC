from django.shortcuts import render
from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializers, CursoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(methods=['get'], detail=True)
    def avaliacoes(self, request, pk=None ):
        cursos = self.get_object()
        serializer = AvaliacaoSerializers(cursos.avaliacoes.all(), many=True)
        return Response(serializer.data)
    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
    
