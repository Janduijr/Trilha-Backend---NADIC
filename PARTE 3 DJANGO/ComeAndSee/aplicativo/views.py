from django.shortcuts import render
from .models import Filme, MeusFilmes
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request, 'aplicativo/index.html')


def listar_filme(request):
    filmes = Filme.objects.filter().order_by('id')
    context = {
        'filmes': filmes,
    }
    return render(request, 'aplicativo/listar_filmes.html', context)

def filme_detalhes(request, id):
    filme_detalhe = get_object_or_404(Filme, id=id)
    review = None
    
    if request.user.is_authenticated:
        review = MeusFilmes.objects.filter(filme=filme_detalhe, dono=request.user)
        
    context = {
        'filme': filme_detalhe,
        'review': review
    }
    return render(request, 'aplicativo/filme_detalhes.html', context)

@login_required
def review(request, id):
    filme_escolhido = get_object_or_404(Filme, id=id)
    
    MeusFilmes.objects.get_or_create(
        filme = filme_escolhido,
        dono = request.user,
    )
    
    return redirect('filme_detalhes', id=id)

@login_required
def listar_filme_meu(request):
    filmes = MeusFilmes.objects.filter(dono=request.user).order_by('id')
    
    context = {
        'filmes':filmes
    }
    return render(request, 'aplicativo/listar_filmes_meus.html', context)

@login_required
def deletar_review(request, id):
    filme_escolhido = get_object_or_404(MeusFilmes, filme_id=id, dono= request.user)
    
    
    filme_escolhido .delete()
    return redirect('filme_detalhes', id=id)
    