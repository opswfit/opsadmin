# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-23 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opstask', '3443_auto_20180728_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ansibletaskrecord',
            name='release_version',
        ),
        migrations.AddField(
            model_name='ansibletaskrecord',
            name='release_tag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u53d1\u884c\u7248\u672ctag'),
        ),
    ]
