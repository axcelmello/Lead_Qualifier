from django.shortcuts import render

from Qualifier.models import Cadastro_empresa
from Qualifier.models import Cadastro_contato
from Qualifier.models import Dados_empresa

# Create your views here.

def homepage(request, *args, **kwargs):
    # print(request.POST)
    # print(request.GET)
    return render(request, "Homepage.html", {})