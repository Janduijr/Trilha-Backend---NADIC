from django.contrib import admin
from .models import Avaliacao, Curso
# Register your models here.

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo']

@admin.register(Curso)
class CursooAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'criacao', 'atualizacao', 'ativo']
    