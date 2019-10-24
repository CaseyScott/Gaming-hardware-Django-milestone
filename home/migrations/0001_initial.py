# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-23 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]