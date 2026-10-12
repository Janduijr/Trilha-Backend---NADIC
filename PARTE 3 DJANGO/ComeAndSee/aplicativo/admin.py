from django.contrib import admin
from .models import Genero, Filme, MeusFilmes
# Register your models here.

admin.site.register(Genero)
admin.site.register(Filme)
admin.site.register(MeusFilmes)