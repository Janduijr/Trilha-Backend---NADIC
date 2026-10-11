from django.shortcuts import render
from .models import Filme

# Create your views here.

def listar_filme(request):
    filmes = Filme.objects.all().order_by('id')
    context = {
        'filmes': filmes,
    }
    return render(request, 'aplicativo/listar_filmes.html', context)

def filme_detalhes(request, id):
    filme = Filme.objects.get(id=id)
    context = {
        'filme': filme
    }
    return render(request, 'aplicativo/filme_detalhes.html', context)