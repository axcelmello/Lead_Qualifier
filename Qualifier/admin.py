from django.contrib import admin

# Register your models here.

from .models import Cadastro_empresa
from .models import Cadastro_contato
from .models import Dados_empresa

admin.site.register(Cadastro_empresa)
admin.site.register(Cadastro_contato)
admin.site.register(Dados_empresa)
