# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-27 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0007_auto_20181227_1222'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='adextractor',
            table='adextractor',
        ),
        migrations.AlterModelTable(
            name='company',
            table='company',
        ),
        migrations.AlterModelTable(
            name='subscriptions',
            table='subscriptions',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]