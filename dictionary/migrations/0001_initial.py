# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30, verbose_name='перевод слова')),
            ],
            options={
                'verbose_name': 'перевод',
                'verbose_name_plural': 'переводы',
            },
        ),
        migrations.CreateModel(
            name='UserDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, verbose_name='название')),
                ('quantity', models.SmallIntegerField(max_length=32000, verbose_name='количество')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'словарь пользователя',
                'verbose_name_plural': 'словари пользователя',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30, verbose_name='слово')),
                ('transcription', models.CharField(max_length=35, verbose_name='транскрипция')),
            ],
            options={
                'verbose_name': 'слово',
                'verbose_name_plural': 'слова',
            },
        ),
        migrations.AddField(
            model_name='userdictionary',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.Word', verbose_name='словарь'),
        ),
        migrations.AddField(
            model_name='translation',
            name='word_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.Word', verbose_name='слово'),
        ),
    ]
