# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-24 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_auto_20171223_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='item',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
