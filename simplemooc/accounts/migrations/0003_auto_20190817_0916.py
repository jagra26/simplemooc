# Generated by Django 2.2.3 on 2019-08-17 12:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190816_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O nome do usuário só pode conter letras, dígitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário'),
        ),
    ]
