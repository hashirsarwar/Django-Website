# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_auto_20180106_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='folder',
            name='files',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='files',
        ),
        migrations.DeleteModel(
            name='FileSegment',
        ),
        migrations.DeleteModel(
            name='folder',
        ),
        migrations.AddField(
            model_name='uploadfragment',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='one.Upload'),
        ),
    ]