# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-03 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191029_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('V', 'Video cards'), ('H', 'Hard drives'), ('M', 'Memory'), ('C', 'CPU'), ('CL', 'Cooling'), ('MB', 'Motherboards')], max_length=20),
        ),
    ]