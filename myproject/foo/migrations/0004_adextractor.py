# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-27 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0003_auto_20181227_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdExtractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostname', models.CharField(blank=True, max_length=2048, null=True)),
                ('Os_title', models.CharField(blank=True, max_length=2048, null=True)),
                ('Password_Last_set', models.DateTimeField(auto_now_add=True)),
                ('Logon', models.DateTimeField(auto_now_add=True)),
                ('When_created', models.DateTimeField(auto_now_add=True)),
                ('When_changed', models.DateTimeField(auto_now_add=True)),
                ('Active_Directory_path', models.CharField(max_length=2048)),
            ],
        ),
    ]
