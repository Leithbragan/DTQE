# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdictionary',
            name='quantity',
            field=models.SmallIntegerField(verbose_name='количество'),
        ),
    ]