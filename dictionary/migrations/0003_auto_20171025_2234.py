# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-25 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20171025_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='first_letter',
            field=models.CharField(default=-1, max_length=1, verbose_name='первая буква'),
        ),
        migrations.AddField(
            model_name='word',
            name='first_letter',
            field=models.CharField(default=-1, max_length=1, verbose_name='первая буква'),
        ),
    ]
