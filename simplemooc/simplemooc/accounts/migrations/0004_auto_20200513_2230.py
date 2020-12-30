# Generated by Django 2.2.4 on 2020-05-13 22:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200513_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O nome de usuário só pode conter letras, dígitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário'),
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(blank=True, default=False, verbose_name='Confirmado?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Nova Senha',
                'verbose_name_plural': 'Novas Senhas',
                'ordering': ['-created_at'],
            },
        ),
    ]
