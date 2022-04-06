from django.db import models

# Create your models here.


class Cadastro_empresa(models.Model):
    nome_fantasia     = models.CharField(max_length=120)
    razao_social      = models.CharField(max_length=120)
    cnpj              = models.CharField(max_length=120)
    telefone          = models.CharField(max_length=120)
    email             = models.CharField(max_length=120)
    site              = models.CharField(max_length=120)
    endereco          = models.CharField(max_length=120)
    pais_sede         = models.CharField(max_length=120)

class Cadastro_contato(models.Model):
    nome              = models.CharField(max_length=120)
    nomeempresa       = models.CharField(max_length=120)
    cargo             = models.CharField(max_length=120)
    telefone          = models.CharField(max_length=120)
    email             = models.CharField(max_length=120)

class Dados_empresa(models.Model):
    cnpj              = models.CharField(max_length=120)    #info de vinculação com classe Cadastro_empresa
    n_funcionarios    = models.CharField(max_length=120)    #definir tamanho da empresa?
    setor             = models.CharField(max_length=120)    #primário, secundário, terciário
    categoria         = models.CharField(max_length=120)    #tecnologia, saúde, produtos, industria
    capital           = models.CharField(max_length=120)    #privado, público, cooperativa, associação, misto etc.
    abrangencia       = models.CharField(max_length=120)    #Municipal, Regional, Estadual, Nacional, Multinacional

