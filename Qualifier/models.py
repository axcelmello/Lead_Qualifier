from django.db import models 
from localflavor.br.models import BRCNPJField

# Create your models here.

class Cadastro_empresa(models.Model):
    nome_fantasia             = models.CharField(max_length=65)
    razao_social              = models.CharField(blank=True,max_length=65)
    cnpj                      = BRCNPJField(blank=True,max_length=14,unique=True)
    telefone_empresa          = models.CharField(blank=True,max_length=14)
    email_empresa             = models.EmailField(blank=True,max_length=65)
    site                      = models.CharField(blank=True,max_length=65)
    endereco                  = models.CharField(blank=True,max_length=65)
    pais_sede                 = models.CharField(blank=True,max_length=65)
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
    n_funcionarios    = models.IntegerField(blank=True,)
    setor             = models.CharField(max_length=65, choices=SETOR)
    categoria         = models.CharField(blank=True,max_length=120)    #tecnologia, saúde, produtos, industria
    capital           = models.CharField(max_length=65, choices=CAPITAL)
    abrangencia       = models.CharField(max_length=65, choices=ABRANGENCIA)

    def __str__(self):
        return self.cnpj



class Cadastro_contato(models.Model):
    nome_contato              = models.CharField(max_length=65)
    id_empresa_FK             = models.ForeignKey('Cadastro_empresa', on_delete=models.CASCADE, null=True)
    nome_empresa_contato      = models.CharField(max_length=65)
    cargo_contato             = models.CharField(blank=True,max_length=65)
    telefone_contato          = models.CharField(blank=True,max_length=14)
    email_contato             = models.EmailField(blank=True,max_length=65)

    def __str__(self):
        return self.nome_contato