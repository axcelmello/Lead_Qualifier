from django import forms

class Contato_form(forms.Form):
    nome          = forms.CharField()
    nomeempresa   = forms.CharField()
    cargo         = forms.CharField()
    telefone      = forms.IntegerField()
    email         = forms.EmailField()

class Empresa_form(forms.Form):
    nome_fantasia = forms.CharField(label="Nome Fantasia", widget=forms.TextInput(attrs={'class':'form-control'}))
    razao_social = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pais_sede = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

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

    #Dados empresa
    n_funcionarios = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    setor = forms.ChoiceField(choices=SETOR,widget=forms.TextInput(attrs={'class':'form-control'}))
    categoria = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    capital = forms.ChoiceField(choices=CAPITAL,widget=forms.TextInput(attrs={'class':'form-control'}))
    abrangencia = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control'}),choices=ABRANGENCIA)