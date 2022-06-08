from django import forms
from localflavor.br.forms import BRCNPJField, BRCNPJValidator

from Qualifier.models import Cadastro_empresa

class Contato_form(forms.Form):
    nome_contato          = forms.CharField()
    nome_empresa_contato  = forms.ModelChoiceField(queryset=Cadastro_empresa.objects.values_list('nome_fantasia',flat=True).distinct())
    cargo_contato         = forms.CharField()
    telefone_contato      = forms.CharField()
    email_contato         = forms.EmailField()

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField()
    razao_social = forms.CharField()
    cnpj = BRCNPJField(max_length=14,validators=[BRCNPJValidator])
    telefone_empresa = forms.CharField()
    email_empresa = forms.EmailField()
    site = forms.CharField()
    endereco = forms.CharField()
    pais_sede = forms.CharField()

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