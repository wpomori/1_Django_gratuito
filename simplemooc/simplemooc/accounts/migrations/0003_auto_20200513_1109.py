# Generated by Django 2.2.10 on 2020-05-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200513_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_activate',
            field=models.BooleanField(blank=True, default=True, verbose_name='Está ativo?'),
        ),
    ]
