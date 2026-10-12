from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    


class Filme(models.Model):
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=200)
    sinopse = models.TextField(max_length=500, blank=True, default='Sem Sinopse')
    duracao = models.IntegerField(blank=True, default=0)
    generos = models.ManyToManyField(Genero)
    
    def __str__(self):
            return f'{self.titulo}({self.ano})'
    
class MeusFilmes(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
         return f'{self.filme}({self.dono})'
    