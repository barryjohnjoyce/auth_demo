# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161107_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
