from django import forms
from localflavor.br.forms import BRCNPJField, BRCNPJValidator

class Contato_form(forms.Form):
    nome          = forms.CharField()
    nomeempresa   = forms.CharField()
    cargo         = forms.CharField()
    telefone      = forms.CharField()
    email         = forms.EmailField()

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField()
    razao_social = forms.CharField()
    cnpj = BRCNPJField(validators=[BRCNPJValidator])
    telefone = forms.CharField()
    email = forms.EmailField()
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