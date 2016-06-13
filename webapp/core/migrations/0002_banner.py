# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='título')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True, verbose_name='descrição')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='link')),
                ('texto_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='texto do link')),
                ('imagem', stdimage.models.StdImageField(default='img/no-img.jpg', help_text='Tamanho da imagem: 1600x1038 pixeis.', max_length=200, upload_to='uploads/banners/', validators=[stdimage.validators.MinSizeValidator(1600, 933), stdimage.validators.MaxSizeValidator(1600, 1038)], verbose_name='imagem')),
                ('ordem', models.IntegerField(default=1, verbose_name='ordem')),
                ('ativo', models.BooleanField(default=True, verbose_name='diponível')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'banner',
                'ordering': ('-criado_em',),
                'verbose_name_plural': 'banners',
            },
        ),
    ]
