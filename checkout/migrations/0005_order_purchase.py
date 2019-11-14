# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-14 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('checkout', '0004_remove_order_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='purchase',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.Profile'),
            preserve_default=False,
        ),
    ]
