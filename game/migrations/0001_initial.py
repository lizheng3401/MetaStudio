# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 08:57
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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('excrept', models.TextField(blank=True, max_length=300)),
                ('times', models.PositiveIntegerField(default=0)),
                ('icon', models.ImageField(default='default/icon.jpg', upload_to='')),
                ('version', models.CharField(max_length=30)),
                ('game', models.FileField(upload_to='')),
                ('inTro', models.TextField(blank=True)),
                ('foreImg', models.ImageField(default='default/foreImg.jpg', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.GameCategory'),
        ),
    ]