from rest_framework import serializers
from .models import Avaliacao, Curso

class AvaliacaoSerializers(serializers.ModelSerializer):
    
    class Meta:
        args_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        fields = [
            'id'
            'curso',
            'ativo',
            'nome',
            'email',
            'avaliacao',
        ]
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = [
            'id',
            'criacao',
            'titulo',
            'url',
            'ativo',            
        ]