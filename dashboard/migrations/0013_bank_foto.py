# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-16 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20180516_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='bancos'),
        ),
    ]
