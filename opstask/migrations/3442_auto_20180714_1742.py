# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-14 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opstask', '0003441_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ansibletaskrecord',
            name='app_type',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u9879\u76ee\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='ansibletaskrecord',
            name='state',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='\u56de\u9000\u72b6\u6001'),
        ),
    ]
