from django.db import models 
from localflavor.br.models import BRCNPJField

# Create your models here.

class Cadastro_empresa(models.Model):
    nome_fantasia             = models.CharField(max_length=65)
    razao_social              = models.CharField(max_length=65)
    cnpj                      = BRCNPJField(max_length=14,unique=True)
    telefone_empresa          = models.CharField(max_length=14)
    email_empresa             = models.EmailField(max_length=65)
    site                      = models.CharField(max_length=65)
    endereco                  = models.CharField(max_length=65)
    pais_sede                 = models.CharField(max_length=65)
    SETOR = (
        ('', 'Selecione...'),
        ('1', 'Primário'),
        ('2', 'Secundário'),
        ('3', 'Terciário'),
    )
    CAPITAL = (
        ('', 'Selecione...'),
        ('1', 'Privado'),
        ('2', 'Público'),
        ('3', 'Misto'),
    )
    ABRANGENCIA = (
        ('', 'Selecione...'),
        ('1', 'Municipal'),
        ('2', 'Regional'),
        ('3', 'Estadual'),
        ('4', 'Nacional'),
        ('5', 'Multinacional'),
    )
    n_funcionarios    = models.IntegerField(null=True)
    setor             = models.CharField(max_length=65, choices=SETOR)
    categoria         = models.CharField(max_length=120)
    capital           = models.CharField(max_length=65, choices=CAPITAL)
    abrangencia       = models.CharField(max_length=65, choices=ABRANGENCIA)

    def __str__(self):
        return self.cnpj



class Cadastro_contato(models.Model):
    nome_contato              = models.CharField(max_length=65)
    id_empresa_FK             = models.ForeignKey('Cadastro_empresa', on_delete=models.CASCADE, null=True)
    nome_empresa_contato      = models.CharField(max_length=65)
    cargo_contato             = models.CharField(max_length=65)
    telefone_contato          = models.CharField(max_length=14)
    email_contato             = models.EmailField(max_length=65)

    def __str__(self):
        return self.nome_contato