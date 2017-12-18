# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 16:51
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('travel_date', models.DateField(blank=True, null=True, verbose_name='Data da Viagem')),
                ('image', models.ImageField(default='media/images/1.jpg', upload_to='package/images', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Pacote',
                'verbose_name_plural': 'Pacotes',
                'ordering': ['title'],
            },
        ),
    ]
