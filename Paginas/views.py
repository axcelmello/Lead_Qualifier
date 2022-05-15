from django.shortcuts import render

from Qualifier.models import Cadastro_empresa
from Qualifier.models import Cadastro_contato
from Qualifier.models import Dados_empresa

from Qualifier.forms import Contato_form, Empresa_form
# Create your views here.

# print(request.POST)
# print(request.GET)

def homepage(request, *args, **kwargs):
    return render(request, "Homepage.html", {})

def painel(request, *args, **kwargs):

    list_empresas = Cadastro_empresa.objects.all()
    list_contatos = Cadastro_contato.objects.all()
    list_dados = Dados_empresa.objects.all()

    context = {
        'empresas' : list_empresas,
        'contatos' : list_contatos,
        'dados' : list_dados,
    }

    return render(request, "Painel.html", context)

def cadastro_empresa(request, *args, **kwargs):
    form = Empresa_form
    context = {
        "form": form,
    }

    if request.method == 'POST':
        #print(request.POST.get)

        contato = Cadastro_empresa(
            nome_fantasia   = request.POST.get("nome_fantasia"),
            razao_social    = request.POST.get("razao_social"),
            cnpj            = request.POST.get("cnpj"),
            telefone        = request.POST.get("telefone"),
            email           = request.POST.get("email"),
            site            = request.POST.get("site"),
            endereco        = request.POST.get("endereco"),
            pais_sede       = request.POST.get("pais_sede"),
        )
        contato.save()

        dados = Dados_empresa(
            cnpj = contato.cnpj,
            n_funcionarios  = request.POST.get("n_funcionarios"),
            setor = request.POST.get("setor"),
            categoria = request.POST.get("categoria"),
            capital = request.POST.get("capital"),
            abrangencia = request.POST.get("abrangencia"),
        )
        dados.save()


    return render(request, "Cadastro_empresa.html", context)

def cadastro_contato(request, *args, **kwargs):
    form = Contato_form
    context = {
        "form": form,
    }

    if request.method == 'POST':
        # print(request.POST.get)

        contato = Cadastro_contato(
            nome = request.POST.get("nome"),
            nomeempresa = request.POST.get("nomeempresa"),
            cargo = request.POST.get("cargo"),
            telefone = request.POST.get("telefone"),
            email = request.POST.get("email"),
        )
        contato.save()

    return render(request, "Cadastro_contato.html", context)