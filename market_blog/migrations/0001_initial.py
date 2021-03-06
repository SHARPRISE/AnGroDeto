# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-11 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non_pwodui', models.CharField(default='Non Pwodui a', max_length=100)),
                ('slug', models.SlugField(default='slug', max_length=255, unique=True)),
                ('deskripsyon', models.TextField(default='Deskripsyon pwodui a')),
                ('specs', models.CharField(default='Kek lot detay sou pwodui a', max_length=255)),
                ('uploaded', models.DateField(auto_now_add=True, verbose_name='Pwodui sa online depi')),
                ('published', models.BooleanField(default=True)),
                ('seller', models.CharField(default='Moun kap vann nan', max_length=75)),
                ('kontak', models.CharField(default='Nimewo telefon ou', max_length=11)),
                ('pri', models.IntegerField(default='Pri pwodui a an HTG')),
                ('foto_atik', models.ImageField(blank=True, upload_to='img_atik/', verbose_name='img')),
            ],
            options={
                'ordering': ['uploaded'],
            },
        ),
    ]
