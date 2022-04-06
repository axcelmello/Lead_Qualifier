from django.db import models

# Create your models here.

class Cadastro_empresa(models.Model):
    nome_fantasia     = models.CharField(max_length=50)
    razao_social      = models.CharField(max_length=50)
    cnpj              = models.IntegerField()
    telefone          = models.IntegerField()
    email             = models.EmailField(max_length=25)
    site              = models.CharField(max_length=25)
    endereco          = models.CharField(max_length=30)
    pais_sede         = models.CharField(max_length=25)

class Cadastro_contato(models.Model):
    nome              = models.CharField(max_length=50)
    nomeempresa       = models.ForeignKey(Cadastro_empresa, on_delete=models.CASCADE)
    cargo             = models.CharField(max_length=25)
    telefone          = models.IntegerField()
    email             = models.EmailField(max_length=25)

class Dados_empresa(models.Model):
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
    cnpj              = models.ForeignKey(Cadastro_empresa, on_delete=models.CASCADE)
    n_funcionarios    = models.IntegerField()
    setor             = models.CharField(max_length=15, choices=SETOR)
    categoria         = models.CharField(max_length=120)    #tecnologia, saúde, produtos, industria
    capital           = models.CharField(max_length=15, choices=CAPITAL)
    abrangencia       = models.CharField(max_length=25, choices=ABRANGENCIA)