# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 12:59
from __future__ import unicode_literals

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.AccountUserManager()),
            ],
        ),
    ]
