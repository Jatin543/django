# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-28 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0008_auto_20181227_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
