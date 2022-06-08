# Generated by Django 4.0.5 on 2022-06-08 15:47

from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('Qualifier', '0002_rename_cargo_cadastro_contato_cargo_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_contato',
            name='cargo_contato',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_contato',
            name='email_contato',
            field=models.EmailField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_contato',
            name='id_empresa_FK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Qualifier.cadastro_empresa'),
        ),
        migrations.AlterField(
            model_name='cadastro_contato',
            name='telefone_contato',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='categoria',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(blank=True, max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='email_empresa',
            field=models.EmailField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='endereco',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='n_funcionarios',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='pais_sede',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='razao_social',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='site',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='telefone_empresa',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
