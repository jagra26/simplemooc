# Generated by Django 2.2.3 on 2019-08-17 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(blank=True, default=0, verbose_name='Visualizações')),
                ('answers', models.IntegerField(blank=True, default=0, verbose_name='Respostas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='threads', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(blank=True, default=False, verbose_name='Correta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['-correct', 'created'],
            },
        ),
    ]