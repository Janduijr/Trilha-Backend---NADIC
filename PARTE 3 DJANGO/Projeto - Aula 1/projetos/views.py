from django.shortcuts import render
from .models import topic

# Create your views here.

def index(request):
    return render(request, 'projetos/index.html')

def topics(request):
    topics = topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'projetos/topic.html', context)
