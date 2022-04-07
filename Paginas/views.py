from django.shortcuts import render

from Qualifier.models import Cadastro_empresa
from Qualifier.models import Cadastro_contato
from Qualifier.models import Dados_empresa

# Create your views here.

# print(request.POST)
# print(request.GET)

def homepage(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "Homepage.html", {})

def painel(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "Painel.html", {})

def cadastro_empresa(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "Cadastro_empresa.html", {})

def cadastro_contato(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "Cadastro_contato.html", {})