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
    cnpj = forms.IntegerField()
    telefone = forms.IntegerField()
    email = forms.EmailField()
    site = forms.CharField()
    endereco = forms.CharField()
    pais_sede = forms.CharField()