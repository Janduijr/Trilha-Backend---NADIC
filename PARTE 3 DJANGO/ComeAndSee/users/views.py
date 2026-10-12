from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            novo_user = form.save()
            authenticated_user = authenticate(username=novo_user.username, password= request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    
    else:
        form = UserCreationForm()
        
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)
        
    