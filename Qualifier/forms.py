from django import forms
from localflavor.br.forms import BRCNPJField, BRCNPJValidator

from Qualifier.models import Cadastro_empresa

class Contato_form(forms.Form):
    nome_contato          = forms.CharField(label="Nome do Contato")
    nome_empresa_contato  = forms.ModelChoiceField(label="Empresa do Contato",queryset=Cadastro_empresa.objects.values_list('nome_fantasia',flat=True).distinct())
    cargo_contato         = forms.CharField(label="Cargo do Contato")
    telefone_contato      = forms.CharField(label="Telefone do Contato")
    email_contato         = forms.EmailField(label="E-mail do Contato")

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField(label="Nome Fantasia")
    razao_social = forms.CharField(label="Razão Social")
    cnpj = BRCNPJField(label="CNPJ", max_length=14,validators=[BRCNPJValidator])
    telefone_empresa = forms.CharField(label="Telefone da Empresa")
    email_empresa = forms.EmailField(label="E-mail Empresa")
    site = forms.CharField(label="Site")
    endereco = forms.CharField(label="Endereço")
    pais_sede = forms.CharField(label="Pais Sede")

    SETOR = (
        ('Primário', 'Primário'),
        ('Secundário', 'Secundário'),
        ('Terciário', 'Terciário'),
    )
    CAPITAL = (
        ('Privado', 'Privado'),
        ('Público', 'Público'),
        ('Misto', 'Misto'),
    )
    ABRANGENCIA = (
        ('Municipal', 'Municipal'),
        ('Regional', 'Regional'),
        ('Estadual', 'Estadual'),
        ('Nacional', 'Nacional'),
        ('Multinacional', 'Multinacional'),
    )
    
    n_funcionarios = forms.IntegerField()
    setor = forms.ChoiceField(choices=SETOR)
    categoria = forms.CharField()
    capital = forms.ChoiceField(choices=CAPITAL)
    abrangencia = forms.ChoiceField(choices=ABRANGENCIA)