from django import forms

class Contato_form(forms.Form):
    nome          = forms.CharField()
    nomeempresa   = forms.CharField()
    cargo         = forms.CharField()
    telefone      = forms.IntegerField()
    email         = forms.EmailField()
