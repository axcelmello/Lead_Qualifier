from django.db import models 
from localflavor.br.models import BRCNPJField

# Create your models here.

class Cadastro_empresa(models.Model):
    nome_fantasia     = models.CharField(max_length=65)
    razao_social      = models.CharField(max_length=65)
    cnpj              = BRCNPJField(unique=True)
    telefone          = models.IntegerField()
    email             = models.EmailField(max_length=65)
    site              = models.CharField(max_length=65)
    endereco          = models.CharField(max_length=65)
    pais_sede         = models.CharField(max_length=65)
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
    n_funcionarios    = models.IntegerField()
    setor             = models.CharField(max_length=65, choices=SETOR)
    categoria         = models.CharField(max_length=120)    #tecnologia, saúde, produtos, industria
    capital           = models.CharField(max_length=65, choices=CAPITAL)
    abrangencia       = models.CharField(max_length=65, choices=ABRANGENCIA)

    def __str__(self):
        return self.cnpj



class Cadastro_contato(models.Model):
    nome              = models.CharField(max_length=65)
    nomeempresa       = models.CharField(max_length=65)
    cargo             = models.CharField(max_length=65)
    telefone          = models.IntegerField()
    email             = models.EmailField(max_length=65)

    def __str__(self):
        return self.nome

"""class Dados_empresa(models.Model):
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
    cnpj              = BRCNPJField(unique=True)
    n_funcionarios    = models.IntegerField()
    setor             = models.CharField(max_length=65, choices=SETOR)
    categoria         = models.CharField(max_length=120)    #tecnologia, saúde, produtos, industria
    capital           = models.CharField(max_length=65, choices=CAPITAL)
    abrangencia       = models.CharField(max_length=65, choices=ABRANGENCIA)

    def __str__(self):
        return self.cnpj
"""