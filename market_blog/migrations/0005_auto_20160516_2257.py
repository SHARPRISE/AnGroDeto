# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_blog', '0004_auto_20160516_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autolink',
            name='transmission',
            field=models.CharField(choices=[('1', 'automatique'), ('2', 'shift')], default=('2', 'shift'), max_length=255),
        ),
    ]
