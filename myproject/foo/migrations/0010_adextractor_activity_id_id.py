# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-28 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0009_activity_activity_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='adextractor',
            name='activity_id_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foo.Activity'),
        ),
    ]
