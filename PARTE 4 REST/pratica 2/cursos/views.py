from django.shortcuts import render
from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializers, CursoSerializer
from rest_framework import viewsets
# Create your views here.

class AvaliacaoView(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer