from asyncio.windows_events import NULL
from django import forms
from localflavor.br.forms import BRCNPJField, BRCNPJValidator

from Qualifier.models import Cadastro_empresa

class Contato_form(forms.Form):
    nome_contato          = forms.CharField()
    nome_empresa_contato  = forms.ModelChoiceField(queryset=Cadastro_empresa.objects.values_list('nome_fantasia',flat=True).distinct())
    cargo_contato         = forms.CharField(required=False)
    telefone_contato      = forms.CharField(required=False)
    email_contato         = forms.EmailField(required=False)

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField()
    razao_social = forms.CharField(required=False)
    cnpj = BRCNPJField(max_length=14,validators=[BRCNPJValidator])
    telefone_empresa = forms.CharField()
    email_empresa = forms.EmailField(required=False)
    site = forms.CharField(required=False)
    endereco = forms.CharField(required=False)
    pais_sede = forms.CharField(required=False)

    SETOR = (
        ('', 'Selecione...'),
        ('1', 'Primário'),
        ('2', 'Secundário'),
        ('3', 'Terciário'),
    )
    CAPITAL = (
        ('', 'Selecione...'),
        ('1', 'Privado'),
        ('2', 'Público'),
        ('3', 'Misto'),
    )
    ABRANGENCIA = (
        ('', 'Selecione...'),
        ('1', 'Municipal'),
        ('2', 'Regional'),
        ('3', 'Estadual'),
        ('4', 'Nacional'),
        ('5', 'Multinacional'),
    )
    
    n_funcionarios = forms.IntegerField(required=False,initial=0)
    setor = forms.ChoiceField(choices=SETOR,required=False)
    categoria = forms.CharField(required=False)
    capital = forms.ChoiceField(required=False,choices=CAPITAL)
    abrangencia = forms.ChoiceField(required=False,choices=ABRANGENCIA)