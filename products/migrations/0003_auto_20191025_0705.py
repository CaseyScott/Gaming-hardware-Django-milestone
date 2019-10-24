# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-24 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Video Cards', 'video cards'), ('H', 'hard drives'), ('M', 'memory'), ('C', 'cpu'), ('CL', 'cooling'), ('MB', 'mother boards'), ('P', 'power supplies')], max_length=2),
        ),
    ]