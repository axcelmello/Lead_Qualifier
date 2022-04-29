from django import forms

class Contato_form(forms.Form):
    nome          = forms.CharField()
    nomeempresa   = forms.CharField()
    cargo         = forms.CharField()
    telefone      = forms.IntegerField()
    email         = forms.EmailField()

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField()
    razao_social = forms.CharField()
    cnpj = forms.CharField()
    telefone = forms.IntegerField()
    email = forms.EmailField()
    site = forms.CharField()
    endereco = forms.CharField()
    pais_sede = forms.CharField()

    #Dados empresa
    n_funcionarios = forms.IntegerField()
    setor = forms.CharField()
    categoria = forms.CharField()
    capital = forms.CharField()
    abrangencia = forms.CharField()