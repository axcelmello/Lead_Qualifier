# Generated by Django 4.0.3 on 2022-04-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qualifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_contato',
            name='telefone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='cnpj',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='telefone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dados_empresa',
            name='n_funcionarios',
            field=models.IntegerField(),
        ),
    ]
